import utilities as utils
from workPaths import workPaths
from os.path import join, exists, normpath
from os import mkdir

def ensureResourceDirExists(project, resourceDir):
	if (not exists(resourceDir)):
		mkdir(resourceDir)


def copyResourceTypeToProject(project, type, resourcesDir, resources):
	ensureResourceDirExists(project, resourcesDir)

	resourceDirs = [res.dir for res in resources]
	utils.replaceDirectoriesToDir(resourceDirs, resourcesDir)
	
def copyScriptsToProject(project, scripts):
	copyResourceTypeToProject(project, 'scripts', project.scriptsDir, scripts)

def copyObjectsToProject(project, objects):
	copyResourceTypeToProject(project, 'objects', project.objectsDir, objects)

def copyExtensionsToProject(project, extensions):
	copyResourceTypeToProject(project, 'extensions', project.extensionsDir, extensions)


def copyResourcesToProject(targetProject):
	sourceProject = workPaths.assetProject
	copyScriptsToProject(targetProject, sourceProject.assetScripts)
	copyObjectsToProject(targetProject, sourceProject.assetObjects)
	copyExtensionsToProject(targetProject, sourceProject.assetExtensions)