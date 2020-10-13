from os.path import normpath, basename, dirname, join
import utilities as utils

class File:
	def __init__(self, name, dir, extension):
		self.name	= name
		self.dir	= dir
		self.file	= join(dir, name) + '.' + extension

	def __str__(self):
		return 'name: {},\ndir : {},\nfile: {}\n'.format(self.name, self.dir, self.file)

class Resource(File):
	def __init__(self, path, type):
		name= utils.getFileName(path, True)
		dir = dirname(path)
		self.type = type

		File.__init__(self, name, dir, 'yy')

class Project(File):
	def __init__(self, name, dir, assetName):
		dir = normpath(dir)

		File.__init__(self, name, dir, 'yyp')

		self.assetScriptsGroup	= name
		self.assetObjectsGroup	= name
		self.assetExtensionsGroup = name

		self.scriptsDir		= join(dir, 'scripts')
		self.objectsDir		= join(dir, 'objects')
		self.extensionsDir	= join(dir, 'extensions')

		self.scripts = [Resource(script, 'script') for script in self.findScripts('')]
		self.objects = [Resource(object, 'object') for object in self.findObjects('')]
		self.extensions = [Resource(extension, 'extension') for extension in self.findExtensions('')]

		assetBranchTail = '/' + assetName
		self.assetScripts = [Resource(script, 'script') for script in self.findScripts(assetBranchTail)]
		self.assetObjects = [Resource(object, 'object') for object in self.findObjects(assetBranchTail)]
		self.assetExtensions = [Resource(extension, 'extension') for extension in self.findExtensions(assetBranchTail)]

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.extensionsDir)

	#TODO 'Scripts' and 'Objects' should not be fixed in here, as resource folders can now be renamed

	def findScripts(self, branchTail):
		scripts = self.findResourceType('Scripts', branchTail, self.scriptsDir)
		return scripts

	def findObjects(self, branchTail):
		objects = self.findResourceType('Objects', branchTail, self.objectsDir)
		return objects

	def findExtensions(self, branchTail):
		extensions = self.findResourceType('Extensions', branchTail, self.extensionsDir)
		return extensions

	def validResource(self, resourcesJson, resource, branch):
		resourceJson = utils.readJson(resource)
		resourcePath = resourceJson['parent']['path']

		valid = branch in resourcePath
		
		return valid

	
	def findResourceType(self, type, branchTail, resourcesDir):
		print('\nLOCATING RESOURCES\n')

		projectJson = utils.readJson(self.file)
		resourcesJson = projectJson['resources']
		resources = utils.getDirExtensionFilesRecursive(resourcesDir, '.yy')

		branch = 'folders/' + type + branchTail
		okResources = [res for res in resources if self.validResource(resourcesJson, res, branch)]

		print('\nRESOURCES LOCATED\n')

		return okResources

class WorkPaths():
	def __init__(self, projectsDir, assetProjectDir):
		assetName = basename(assetProjectDir)

		self.projectsDir	= normpath(projectsDir)
		self.assetProject	= Project(assetName, assetProjectDir, assetName)

def makeProjectFromDir(dir, assetName):
	yypFile = utils.getDirExtensionFiles(dir, 'yyp')[0]
	name = utils.getFileName(yypFile, True)
	project = Project(name, dir, assetName)

	return project



workPaths = ''

def initWorkPaths(paths):
	global workPaths #This lets the function know we're referencing the module-level variable workPaths
	workPaths = WorkPaths(
		paths['projectsDir'],
		paths['assetProjectDir']
	)