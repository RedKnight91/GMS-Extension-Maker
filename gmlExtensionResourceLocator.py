import utilities as utils
import gmsUtilities as gms
import os


def locateInternalScripts(workPaths):
	viewPath = os.path.join('scripts', workPaths.internalGroupName)
	scripts = locateScripts(workPaths, viewPath)
	return scripts

def locateExternalScripts(workPaths):
	viewPath = os.path.join('scripts', workPaths.externalGroupName)
	scripts = locateScripts(workPaths, viewPath)
	return scripts

def locateScripts(workPaths, viewPath):
	scripts = locateResourceType(workPaths, 'GMScript', 'ResourceTree_Scripts', viewPath)
	return scripts

def locateObjects(workPaths):
	objects = locateResourceType(workPaths, 'GMObject', 'ResourceTree_Objects', 'objects')
	return objects

def locateExtensions(workPaths):
	extensions = locateResourceType(workPaths, 'GMExtension', 'ResourceTree_Extensions', 'extensions')
	return extensions


def locateResourceType(workPaths, filterType, resourceType, viewPath):

	extensionName = workPaths.extension.name
	sourceViewsDir = workPaths.sourceProject.viewsDir

	def separateChildrenViewsAndResources(viewJson):
		views = []
		resources = []

		for uuid in viewJson['children']:
			viewPath = utils.makeFilePath(sourceViewsDir, uuid, 'yy')

			if (os.path.exists(viewPath)):
				views.append(uuid)
			else:
				resources.append(uuid)

		return {'views' : views, 'resources' : resources}

	def filterViewByName(resourceViews, name):
		for view in resourceViews:
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

	def makeViewPathsFromUuids(viewsDir, uuids):
		viewPaths = [os.path.join(viewsDir, uuid) + '.yy' for uuid in uuids ]
		viewPaths = [path for path in viewPaths if os.path.exists(path)]
		return viewPaths

	def getViewResourcesRecursive(viewJson):
		resources = []

		children = separateChildrenViewsAndResources(viewJson)

		childResources = children['resources']
		resources.extend(childResources)

		childViews = children['views']
		childViewPaths = utils.makeFilePathList(sourceViewsDir, childViews, 'yy')

		for view in childViewPaths:
			childViewJson = utils.readFileJson(view)
			childViewResources = getViewResourcesRecursive(childViewJson)
			resources.extend(childViewResources)

		return resources

	def getViewResources(viewPath):
	# def getScopedResources(extChildrenPaths, scopedViewName, viewUuids):
		resourcePaths = []
		resourceUuids = []

		sourceProjectJson = utils.readFileJson(workPaths.sourceProject.file)
		# scopedViewJson = extractViewByName(extChildrenPaths, scopedViewName)
		viewJson = utils.readFileJson(viewPath)

		if ('children' in viewJson):
			resourceUuids = getViewResourcesRecursive(viewJson)
		
		resourcePaths = makeResourcePathsFromUuids(workPaths.sourceProject.dir, sourceProjectJson, resourceUuids)
		return resourcePaths


	print('\nLOCATING RESOURCES\n')

	viewFiles = utils.getDirectoryExtensionFiles(sourceViewsDir, '.yy')
	viewFiles = gms.filterViewsByType(viewFiles, filterType)

	rootView = gms.locateRootResourceView(viewFiles, resourceType)
	rootViewJson = utils.readFileJson(rootView)

	viewPath = utils.splitPath(viewPath)
	currentViewPath = [rootViewJson['folderName']]
	currentViewJson = rootViewJson

	while (currentViewPath != viewPath):
		viewChildren = currentViewJson['children']
		viewChildren = makeViewPathsFromUuids(workPaths.sourceProject.viewsDir, viewChildren)
		nextViewPath = viewPath[len(currentViewPath)]
		currentViewJson = filterViewByName(viewChildren, nextViewPath)

		assert 'children' in currentViewJson, 'Could not find {} group for {} resource type'.format(extensionName, filterType)
		
		currentViewPath.append(currentViewJson['folderName'])

	viewUuid = currentViewJson['id']
	viewPath = utils.makeFilePath(sourceViewsDir, viewUuid, 'yy')
	resources = getViewResources(viewPath)
	# resources = getViewResources(childResourcePaths, viewPath, viewUuids)

	print('\nRESOURCES LOCATED\n')

	return resources