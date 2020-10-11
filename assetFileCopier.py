import utilities as utils
from paths import workPaths
from os.path import join, exists, normpath
from os import mkdir

def ensureResourceDirExists(project, resourceDir):
	if (not exists(resourceDir)):
		print('"{}" folder not found for project {}'.format(utils.getDirName(resourceDir), project.name))
		print('Creating "{}" folder'.format(utils.getDirName(resourceDir)))
		mkdir(resourceDir)


def copyResourceTypeToProject(project, type, resourcesDir, resources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	ensureResourceDirExists(project, resourcesDir)

	resourceDirs = [res.dir for res in resources]
	utils.replaceDirectoriesToDir(resourceDirs, resourcesDir)
	
	print('\nRESOURCE DIRECTORIES COPIED\n')

def copyScriptsToProject(project, scripts):
	copyResourceTypeToProject(project, 'scripts', project.scriptsDir, scripts)

def copyObjectsToProject(project, objects):
	copyResourceTypeToProject(project, 'objects', project.objectsDir, objects)

def copyExtensionsToProject(project, extensions):
	copyResourceTypeToProject(project, 'extensions', project.extensionsDir, extensions)


def copyResourcesToProject(targetProject):
	sourceProject = workPaths.assetProject
	copyScriptsToProject(targetProject, sourceProject.scripts)
	copyObjectsToProject(targetProject, sourceProject.objects)
	copyExtensionsToProject(targetProject, sourceProject.extensions)