from os.path import exists
from workPaths import workPaths, makeProjectFromDir
import utilities as utils

def projectUsesAsset(dir, extensionName):
	projectExtensionPath = dir + r'\extensions\{}'.format(extensionName)
	hasMatchingExtensionDir = (exists(projectExtensionPath))

	return hasMatchingExtensionDir

def validProject(dir):
	asset = workPaths.assetProject

	sameProject = (dir == asset.dir)
	usesExtension = projectUsesAsset(dir, asset.name)
	valid = usesExtension and not sameProject

	return valid

def listProjectsUsingAsset():
	projectDirs = utils.getDirectoriesContainingFileType(workPaths.projectsDir, 'yyp')
	assetName = workPaths.assetProject.name
	matches = [makeProjectFromDir(dir, assetName) for dir in projectDirs if validProject(dir)]

	return matches