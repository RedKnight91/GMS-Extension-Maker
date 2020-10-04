import os
from gmsUtilities import Project, File

def printWorkPaths(workPaths):
	print('WORK PATHS:\n')
	print('Source Project:\n', workPaths.assetProject, '\n')
	print('Combined Functions:\n', workPaths.combinedScripts, '\n')
	print('Asset Scripts Group:\n', workPaths.assetScriptsGroup, '\n')
	print('Asset Objects Group:\n', workPaths.assetObjectsGroup, '\n')


def validateFile(file):
	assert os.path.exists(file.dir), '{} dir not found:\n {}'.format(file.name, file.dir)


def validateWorkPaths(workPaths):
	validateFile(workPaths.assetProject)

	return workPaths