import utilities as utils
import os


def locateScripts(workPaths):
	scripts = locateResourceType(workPaths, 'GMScript', 'ResourceTree_Scripts')
	return scripts

def locateObjects(workPaths):
	objects = locateResourceType(workPaths, 'GMObject', 'ResourceTree_Objects')
	return objects


def locateResourceType(workPaths, filterType, resourceType):

	extensionName = workPaths.extension.name
	sourceViewsDir = workPaths.sourceProject.viewsDir

	def separateChildrenViewsAndResources(filteredViewUuids, viewJson):
		views = []
		resources = []

		for uuid in viewJson['children']:
			if (uuid in filteredViewUuids):
				views.append(uuid)
			else:
				resources.append(uuid)

		return {'views' : views, 'resources' : resources}

	def makeChildrenPathList(dir, view, appendExt):
		uuids = view['children']
		paths = makePathList(dir, uuids, appendExt)
		return paths

	def makePathList(dir, names, appendedExt):
		paths = []

		for name in names:
			path = os.path.join(dir, name) + '.' + appendedExt
			paths.append(path)

		return paths

	def filterViewsByType(viewPaths, filterType):
		for view in viewPaths:
			viewJson = utils.readFileJson(view)
			filter = viewJson['filterType']

			if (filter != filterType):
				viewPaths.remove(view)

		return viewPaths

	def locateRootResourceView(viewPaths, resourceType):
		for view in viewPaths:
			viewJson = utils.readFileJson(view)
			internalName = viewJson['localisedFolderName']

			if (internalName == resourceType):
				return viewJson
		
		return {}

	def locateResourceExtensionView(resourceViews, name):
		for view in resourceViews:
			viewJson = utils.readFileJson(view)
			visibleName = viewJson['folderName']

			if (visibleName == name):
				return viewJson

		return {}

	def extractViewByName(views, name):
		for view in views:
			viewJson = utils.readFileJson(view)
			visibleName = viewJson['folderName']

			if (visibleName == name):
				return viewJson

		return {}

	def makeResourcePathsFromUuids(sourceProjectDir, projectJson, uuids):
		projectResources = projectJson['resources']
		resourcePaths = []

		for resource in projectResources:
			key = resource['Key']
			if (key in uuids):
				path = resource['Value']['resourcePath']
				fullPath = os.path.join(sourceProjectDir, path)
				dirPath = os.path.dirname(fullPath)

				resourcePaths.append(dirPath)

		return resourcePaths

	def getChildResourcesRecursively(viewUuids, viewJson):
		resources = []

		children = separateChildrenViewsAndResources(viewUuids, viewJson)

		childResources = children['resources']
		resources.extend(childResources)

		childViews = children['views']
		childViewPaths = makePathList(sourceViewsDir, childViews, 'yy')

		for view in childViewPaths:
			childViewJson = utils.readFileJson(view)
			childViewResources = getChildResourcesRecursively(viewUuids, childViewJson)
			resources.extend(childViewResources)

		return resources

	def getScopedResources(extChildrenPaths, scopedViewName, viewUuids):
		resourcePaths = []

		sourceProjectJson = utils.readFileJson(workPaths.sourceProject.file)
		scopedViewJson = extractViewByName(extChildrenPaths, scopedViewName)

		if ('children' in scopedViewJson):
			resourceUuids = getChildResourcesRecursively(viewUuids, scopedViewJson)
		
		resourcePaths = makeResourcePathsFromUuids(workPaths.sourceProject.dir, sourceProjectJson, resourceUuids)
		return resourcePaths




	print('\nLOCATING RESOURCES\n')

	viewFiles = utils.getDirectoryExtensionFiles(sourceViewsDir, '.yy')
	viewFiles = filterViewsByType(viewFiles, filterType)
	viewUuids = utils.extractFileNames(viewFiles, True)

	rootViewJson = locateRootResourceView(viewFiles, resourceType)
	resourceViewFiles = makeChildrenPathList(sourceViewsDir, rootViewJson, 'yy')
	resourceExtensionViewJson = locateResourceExtensionView(resourceViewFiles, extensionName)
	#E.g. scripts/GMS_ext_name, objects/GMS_ext_name

	assert 'children' in resourceExtensionViewJson, 'Could not find {} group for {} resource type'.format(extensionName, filterType)

	childResourcePaths = makeChildrenPathList(sourceViewsDir, resourceExtensionViewJson, 'yy')
	
	externalResources = getScopedResources(childResourcePaths, workPaths.externalGroupName, viewUuids)
	internalResources = getScopedResources(childResourcePaths, workPaths.internalGroupName, viewUuids)

	print('\nRESOURCES LOCATED\n')

	resources = {'external' : externalResources, 'internal' : internalResources}
	return resources