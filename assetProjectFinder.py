from os.path import exists
from paths import workPaths
from classes import makeProjectFromDir
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
	matches = [makeProjectFromDir(dir) for dir in projectDirs if validProject(dir)]

	return matches