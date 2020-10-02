import os
from gmsUtilities import Project, File

def printWorkPaths(workPaths):
	print('WORK PATHS:\n')
	print('Source Project:\n', workPaths.sourceProject, '\n')
	print('Extension Project:\n', workPaths.extensionProject, '\n')
	print('Extension:\n', workPaths.extension, '\n')
	print('Extension Functions:\n', workPaths.extension.functions, '\n')
	print('Combined Functions:\n', workPaths.combinedScripts, '\n')
	print('Combined Jsdocs:\n', workPaths.combinedJsdocs, '\n')
	print('External Group:\n', workPaths.externalScriptsGroup, '\n')
	print('Internal Group:\n', workPaths.internalScriptsGroup, '\n')


def validateFile(file):
	assert os.path.exists(file.dir), '{} dir not found:\n {}'.format(file.name, file.dir)


def validateWorkPaths(workPaths):
	validateFile(workPaths.sourceProject)
	validateFile(workPaths.extensionProject)
	validateFile(workPaths.extension)

	return workPaths