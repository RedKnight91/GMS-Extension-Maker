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
		self.extensionsDir	= join(dir, 'extensions')

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.extensionsDir)

class ProductionPaths():
	def __init__(self, projectsDir, sourceProjectDir, extensionName, combinedDir, externalScriptsGroup, internalScriptsGroup, externalObjectsGroup):
		self.projectsDir		= normpath(projectsDir)

		sourceProjectName		= basename(sourceProjectDir)
		self.sourceProject		= Project(sourceProjectName, sourceProjectDir)

		# extensionProjectName	= basename(extensionProjectDir)
		# self.extensionProject	= Project(extensionProjectName, extensionProjectDir)

		self.combinedDir		= join(normpath(combinedDir), sourceProjectName)
		functionsName			= sourceProjectName + '_functions'

		# extensionDir			= join(self.extensionProject.extensionsDir, extensionName)
		# self.extension			= File(extensionName, extensionDir, 'yy')
		# self.extension.functions= File(functionsName, extensionDir, 'gml')

		self.combinedScripts	= File(functionsName, combinedDir, 'gml')
		self.combinedJsdocs		= File('jsdocs', combinedDir, 'gml')

		self.externalScriptsGroup	= externalScriptsGroup
		self.internalScriptsGroup	= internalScriptsGroup

		self.externalObjectsGroup	= externalObjectsGroup

def createResourceJson(path):
	# name = basename(path)
	# dir = utils.removeExtension(path)
	# yyPath = join(dir, name) + '.yy'

	#TODO check that the path is correct (e.g. scripts/doThing/doThing.yy)
	json = {
		'id': {
			'name': basename(path),
			'path': path
		},
		'order': 0
	}

	return json

def makeResourcePath(projectDir, partialResourcePath):
	path = join(projectDir, partialResourcePath)
	return path

def makeResourceDirPath(projectDir, partialResourcePath):
	fullPath = makeResourcePath(projectDir, partialResourcePath)
	dirPath = utils.getDir(fullPath)
	return dirPath

# def isResourceInProjectFile(name, projectJson):
# 	resources = projectJson['resources']

# 	for resource in resources:
# 		path = resource['Value']['resourcePath']
# 		type = resource['Value']['resourceType']

# 		if (resourceType == type and name in path):
# 			return True
	
# 	return False

def includeResourceToProject(resPath, projectJson):
	json = createResourceJson(resPath)
	projectJson['resources'].append(json)

def includeResourcesToProject(resourcePaths, projectFile):
	projectJson = utils.readJson(projectFile)

	for path in resourcePaths:
		# TODO Is this check necessary?
		# name = basename(path)
		# if (not isResourceInProjectFile(name, projectJson)):
		includeResourceToProject(path, projectJson)
			
	utils.writeJson(projectFile, projectJson)