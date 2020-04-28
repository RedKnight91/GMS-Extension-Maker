import os

class File:
	def __init__(self, name, dir, extension):
		self.name	= name
		self.dir	= dir
		self.file	= os.path.join(dir, name) + '.' + extension

	def __str__(self):
		return 'name: {},\ndir : {},\nfile: {}\n'.format(self.name, self.dir, self.file)

class Project(File):
	def __init__(self, name, dir, extension):
		File.__init__(self, name, dir, extension)
		self.scriptsDir		= os.path.join(dir, 'scripts')
		self.objectsDir		= os.path.join(dir, 'objects')
		self.viewsDir		= os.path.join(dir, 'views')
		self.extensionsDir	= os.path.join(dir, 'extensions')

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nviewsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.viewsDir, self.extensionsDir)

def printWorkPaths(workPaths):
	print('WORK PATHS:\n')
	print('Source Project:\n', workPaths.sourceProject, '\n')
	print('Extension Project:\n', workPaths.extensionProject, '\n')
	print('Extension:\n', workPaths.extension, '\n')
	print('Extension Functions:\n', workPaths.extension.functions, '\n')
	print('Combined Functions:\n', workPaths.combinedFunctions, '\n')
	print('Combined Jsdocs:\n', workPaths.combinedJsdocs, '\n')
	print('External Group:\n', workPaths.externalGroupName, '\n')
	print('Internal Group:\n', workPaths.internalGroupName, '\n')


def validateFile(file):
	assert os.path.exists(file.dir), '{} dir not found:\n {}'.format(file.name, file.dir)


def initExtensionPaths(paths):
	sourceProjectDir	= os.path.join(paths.projectsDir, paths.extensionsSubDir, paths.sourceProjectName, paths.sourceProjectName)
	extensionProjectDir = os.path.join(paths.projectsDir, paths.extensionsSubDir, paths.sourceProjectName, paths.extensionProjectName)

	combinedDir		= os.path.join('C:/Users/mikec/Desktop/GMLCombinerResults', paths.sourceProjectName)
	functionsName	= paths.sourceProjectName + '_functions'
	jsdocsName		= 'jsdocs'


	class Paths:
		pass

	workPaths = Paths()
	
	workPaths.sourceProject			= Project(paths.sourceProjectName, sourceProjectDir, 'yyp')
	workPaths.extensionProject		= Project(paths.extensionProjectName, extensionProjectDir, 'yyp')

	extensionDir					= os.path.join(workPaths.extensionProject.extensionsDir, paths.extensionName)
	workPaths.extension				= File(paths.extensionName, extensionDir, 'yy')
	workPaths.extension.functions	= File(functionsName, extensionDir, 'gml')

	workPaths.combinedFunctions		= File(functionsName, combinedDir, 'gml')
	workPaths.combinedJsdocs		= File(jsdocsName, combinedDir, 'gml')

	workPaths.externalGroupName		= paths.externalResourcesGroup
	workPaths.internalGroupName		= paths.internalResourcesGroup

	# printWorkPaths(workPaths)

	validateFile(workPaths.sourceProject)
	validateFile(workPaths.extensionProject)
	validateFile(workPaths.extension)

	return workPaths