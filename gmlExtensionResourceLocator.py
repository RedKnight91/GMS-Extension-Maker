import utilities as utils
import gmsUtilities as gms
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
		childViewPaths = utils.makeFilePathList(sourceViewsDir, childViews, 'yy')

		for view in childViewPaths:
			childViewJson = utils.readFileJson(view)
			childViewResources = getChildResourcesRecursively(viewUuids, childViewJson)
			resources.extend(childViewResources)

		return resources

	def getScopedResources(extChildrenPaths, scopedViewName, viewUuids):
		resourcePaths = []
		resourceUuids = []

		sourceProjectJson = utils.readFileJson(workPaths.sourceProject.file)
		scopedViewJson = extractViewByName(extChildrenPaths, scopedViewName)

		if ('children' in scopedViewJson):
			resourceUuids = getChildResourcesRecursively(viewUuids, scopedViewJson)
		
		resourcePaths = makeResourcePathsFromUuids(workPaths.sourceProject.dir, sourceProjectJson, resourceUuids)
		return resourcePaths




	print('\nLOCATING RESOURCES\n')

	viewFiles = utils.getDirectoryExtensionFiles(sourceViewsDir, '.yy')
	viewFiles = gms.filterViewsByType(viewFiles, filterType)
	viewUuids = utils.extractFileNames(viewFiles, True)

	rootView = gms.locateRootResourceView(viewFiles, resourceType)
	rootViewJson = utils.readFileJson(rootView)
	resourceViewFiles = utils.makeFilePathList(sourceViewsDir, rootViewJson['children'], 'yy')
	resourceExtensionViewJson = locateResourceExtensionView(resourceViewFiles, extensionName)
	#E.g. scripts/GMS_ext_name, objects/GMS_ext_name

	assert 'children' in resourceExtensionViewJson, 'Could not find {} group for {} resource type'.format(extensionName, filterType)

	childResourcePaths = utils.makeFilePathList(sourceViewsDir, resourceExtensionViewJson['children'], 'yy')
	
	externalResources = getScopedResources(childResourcePaths, workPaths.externalGroupName, viewUuids)
	internalResources = getScopedResources(childResourcePaths, workPaths.internalGroupName, viewUuids)

	print('\nRESOURCES LOCATED\n')

	resources = {'external' : externalResources, 'internal' : internalResources}
	return resources