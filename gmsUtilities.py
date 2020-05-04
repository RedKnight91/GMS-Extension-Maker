import utilities as utils
import os

class File:
	def __init__(self, name, dir, extension):
		self.name	= name
		self.dir	= dir
		self.file	= os.path.join(dir, name) + '.' + extension

	def __str__(self):
		return 'name: {},\ndir : {},\nfile: {}\n'.format(self.name, self.dir, self.file)

class Project(File):
	def __init__(self, name, dir):
		File.__init__(self, name, dir, 'yyp')
		self.scriptsDir		= os.path.join(dir, 'scripts')
		self.objectsDir		= os.path.join(dir, 'objects')
		self.viewsDir		= os.path.join(dir, 'views')
		self.extensionsDir	= os.path.join(dir, 'extensions')

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nviewsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.viewsDir, self.extensionsDir)




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
	name = os.path.basename(path)
	dir = utils.removeExtension(path)
	yyPath = os.path.join(dir, name) + '.yy'

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
	path = os.path.join(projectDir, partialResourcePath)
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
		name = os.path.basename(resource)

		if (not isResourceInProjectFile(name, filterType, projectJson)):
			resourceUuid = includeResourceToProject(resource, filterType, projectJson)
			newResourceUuids.append(resourceUuid)
			
	utils.writeJson(projectFile, projectJson)
	return newResourceUuids