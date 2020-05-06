import utilities as utils
from os.path import join, basename, normpath

class File:
	def __init__(self, name, dir, extension):
		self.name	= name
		self.dir	= dir
		self.file	= join(dir, name) + '.' + extension

	def __str__(self):
		return 'name: {},\ndir : {},\nfile: {}\n'.format(self.name, self.dir, self.file)

class Project(File):
	def __init__(self, name, dir):
		dir = normpath(dir)

		File.__init__(self, name, dir, 'yyp')
		self.scriptsDir		= join(dir, 'scripts')
		self.objectsDir		= join(dir, 'objects')
		self.viewsDir		= join(dir, 'views')
		self.extensionsDir	= join(dir, 'extensions')

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nviewsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.viewsDir, self.extensionsDir)

class ProductionPaths():
	def __init__(self, projectsDir, sourceProjectDir, extensionProjectDir, extensionName, combinedDir, externalScriptsGroup, internalScriptsGroup, externalObjectsGroup):
		self.projectsDir		= normpath(projectsDir)

		sourceProjectName		= basename(sourceProjectDir)
		self.sourceProject		= Project(sourceProjectName, sourceProjectDir)

		extensionProjectName	= basename(extensionProjectDir)
		self.extensionProject	= Project(extensionProjectName, extensionProjectDir)

		self.combinedDir		= join(normpath(combinedDir), sourceProjectName)
		functionsName			= sourceProjectName + '_functions'

		extensionDir			= join(self.extensionProject.extensionsDir, extensionName)
		self.extension			= File(extensionName, extensionDir, 'yy')
		self.extension.functions= File(functionsName, extensionDir, 'gml')

		self.combinedFunctions	= File(functionsName, combinedDir, 'gml')
		self.combinedJsdocs		= File('jsdocs', combinedDir, 'gml')

		self.externalScriptsGroup	= externalScriptsGroup
		self.internalScriptsGroup	= internalScriptsGroup

		self.externalObjectsGroup	= externalObjectsGroup



def getRootResourceView(project, filterType, resourceType):
	viewsDir = project.viewsDir
	viewFiles = utils.getDirectoryExtensionFiles(viewsDir, '.yy')
	viewFiles = filterViewsByType(viewFiles, filterType)
	rootResourceView = locateRootResourceView(viewFiles, resourceType)

	return rootResourceView

def addResourcesToRootView(resourceUuids, project, filterType, resourceType):
	rootResourceView = getRootResourceView(project, filterType, resourceType)
	rootResourceViewJson = utils.readJson(rootResourceView)

	for uuid in resourceUuids:
		rootResourceViewJson['children'].append(uuid)

	utils.writeJson(rootResourceView, rootResourceViewJson)

def locateRootResourceView(viewPaths, resourceType):
	for view in viewPaths:
		viewJson = utils.readJson(view)
		internalName = viewJson['localisedFolderName']

		if (internalName == resourceType):
			return view
	
	return None

def filterViewsByType(viewPaths, filterType):
	for view in viewPaths:
		viewJson = utils.readJson(view)
		filter = viewJson['filterType']

		if (filter != filterType):
			viewPaths.remove(view)

	return viewPaths

def createResourceJson(path, type):
	name = basename(path)
	dir = utils.removeExtension(path)
	yyPath = join(dir, name) + '.yy'

	json = {
		'Key': str(utils.makeUuidV4()),
		'Value': {
			'id': str(utils.makeUuidV4()),
			'resourcePath': yyPath,
			'resourceType': type
		}
	}

	return json

def makeResourcePath(projectDir, partialResourcePath):
	path = join(projectDir, partialResourcePath)
	return path

def makeResourceDirPath(projectDir, partialResourcePath):
	fullPath = makeResourcePath(projectDir, partialResourcePath)
	dirPath = utils.getDir(fullPath)
	return dirPath

def isResourceInProjectFile(name, resourceType, projectJson):
	resources = projectJson['resources']

	for resource in resources:
		path = resource['Value']['resourcePath']
		type = resource['Value']['resourceType']

		if (resourceType == type and name in path):
			return True
	
	return False

def includeResourceToProject(resPath, resType, projectJson):
	json = createResourceJson(resPath, resType)
	uuid = json['Key']

	projectJson['resources'].append(json)

	return uuid

def includeResourcesToProject(resources, projectFile, filterType):
	projectJson = utils.readJson(projectFile)
	newResourceUuids = []

	for resource in resources:
		name = basename(resource)

		if (not isResourceInProjectFile(name, filterType, projectJson)):
			resourceUuid = includeResourceToProject(resource, filterType, projectJson)
			newResourceUuids.append(resourceUuid)
			
	utils.writeJson(projectFile, projectJson)
	return newResourceUuids