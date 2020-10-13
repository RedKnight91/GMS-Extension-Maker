from os.path import normpath, basename, dirname, join
import utilities as utils
from assetResourceFinder import findScripts, findObjects, findExtensions


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

		self.scripts = [Resource(script, 'script') for script in findScripts(self, assetName)]
		self.objects = [Resource(object, 'object') for object in findObjects(self, assetName)]
		self.extensions = [Resource(extension, 'extension') for extension in findExtensions(self, assetName)]

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.extensionsDir)


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