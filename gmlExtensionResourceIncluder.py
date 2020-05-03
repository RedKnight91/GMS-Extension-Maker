import utilities as utils
import gmsUtilities as gms

def includeScriptsToProject(workPaths, project):
	includeResourcesToProject(workPaths, project, project.scriptsDir, 'GMScript')

def includeObjectsToProject(workPaths, project):
	includeResourcesToProject(workPaths, project, project.objectsDir, 'GMObject')
	
def includeExtensionsToProject(workPaths, project):
	includeResourcesToProject(workPaths, project, project.extensionsDir, 'GMExtension')

def includeResourceToProject(dir, type, projectJson):
	name = utils.getDirName(dir)
	inProject = gms.isResourceInProjectFile(name, type, projectJson)
	
	if (not inProject):
		json = gms.createResourceJson(dir, type)
		uuid = json['Key']

		projectJson['resources'].append(json)

		if (type == 'GMScript'):
			projectJson['scripts_order'].append(uuid)

def includeResourcesToProject(workPaths, project, resourceRootDir, resourceType):
	projectJson = utils.readFileJson(workPaths.extensionProject.file)

	resourceDirs = utils.getDirectoryExtensionFilesRecursive(resourceRootDir, 'yy')

	for resourceDir in resourceDirs:
		includeResourceToProject(resourceDir, resourceType, projectJson)
	
	utils.writeFileJson(workPaths.extensionProject.file, projectJson)