from os.path import exists, basename
from workPaths import workPaths, makeProjectFromDir
import utilities as utils

def projectUsesAsset(dir, extensionName):
	projectExtensionPath = dir + r'\extensions\{}'.format(extensionName)
	hasMatchingExtensionDir = (exists(projectExtensionPath))

	return hasMatchingExtensionDir

def v2dot3Project(dir):
	projectYyp = utils.getDirExtensionFiles(dir, 'yyp')[0]
	projectJson = utils.readJson(projectYyp)

	isV23 = 'MetaData' in projectJson
	return isV23

def validProject(dir):
	asset = workPaths.assetProject

	sameProject = (dir == asset.dir)
	usesExtension = projectUsesAsset(dir, asset.name)

	valid = usesExtension and not sameProject

	if valid and not v2dot3Project(dir):
		print('Project {} uses extension but was not updated to v2.3'.format(basename(dir)))
		valid = False

	return valid

def listProjectsUsingAsset():
	projectDirs = utils.getDirectoriesContainingFileType(workPaths.projectsDir, 'yyp')
	assetName = workPaths.assetProject.name
	matches = [makeProjectFromDir(dir, assetName) for dir in projectDirs if validProject(dir)]

	return matches