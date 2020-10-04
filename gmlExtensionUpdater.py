import os
import utilities as utils
import gmsUtilities as gms
from gmsUtilities import Project
import gmlExtensionResourceLocator as locator
import gmlExtensionFileCopier as copier

def listProjectDirectories(projectsDir):
	projectDirs = []
	directories = utils.getSubDirectoriesRecursive(projectsDir)

	for dir in directories:
		if (utils.dirContainsFileType(dir, '.yyp')):
			projectDirs.append(dir)

	return projectDirs

def projectUsesExtension(projectDir, extensionName):
	projectExtensionPath = projectDir + r'\extensions\{}'.format(extensionName)
	hasMatchingExtensionDir = (os.path.exists(projectExtensionPath))

	if (hasMatchingExtensionDir):
		name = os.path.basename(projectDir)
		print('Project match: {}'.format(name))

	return hasMatchingExtensionDir

def listProjectsUsingExtension(projectsDir, assetProjectDir, extensionName):
	projectDirs = utils.getDirectoriesContainingFileType(projectsDir, 'yyp')
	matchingProjects = []

	for dir in projectDirs:
		isSameProject = (dir == assetProjectDir)
		usesExtension = projectUsesExtension(dir, extensionName)

		if (usesExtension and not isSameProject):
			yypFile = utils.getDirectoryExtensionFiles(dir, 'yyp')[0]
			name = utils.getFileName(yypFile, True)

			project = Project(name, dir)
			matchingProjects.append(project)

	return matchingProjects

def promptExtensionUpdateAll():
	prompt = 'Update all projects at once? (Y/N)'
	updateAll = utils.promptChoice(prompt)
	return updateAll

def confirmProjectUpdate(dir):
	prompt = 'Update this project? (Y/N) {}'.format(dir)
	return utils.promptChoice(prompt)

def updateResourcesToProject(workPaths, project, scriptDirs, objectDirs, extensionDirs):
	copier.copyScriptsToProject(workPaths, project, scriptDirs)
	copier.copyObjectsToProject(workPaths, project, objectDirs)
	copier.copyExtensionsToProject(workPaths, project, extensionDirs)

def updateExtensionToProjects(workPaths):
	print('\nPUSHING EXTENSION\n')

	projectsDir = workPaths.projectsDir
	assetProjectDir = workPaths.assetProject.dir
	assetProjectName = workPaths.assetProject.name

	print('\n[1/3] Looking for projects using {} extension'.format(assetProjectName))
	projectsUsingExt = listProjectsUsingExtension(projectsDir, assetProjectDir, assetProjectName)

	if not projectsUsingExt:
		print('\n[2/3] No projects found')
		return

	print('\n[2/3] Retrieving extension files\n')
	assetScriptDirs= locator.locateScripts(workPaths)
	assetObjectDirs= locator.locateObjects(workPaths)
	assetExtensionDirs	= locator.locateExtensions(workPaths)

	print('\n[3/3] Pushing extension to projects')
	updateAll = promptExtensionUpdateAll()

	for project in projectsUsingExt:
		if (updateAll or confirmProjectUpdate(project)):
			updateResourcesToProject(workPaths, project, assetScriptDirs, assetObjectDirs, assetExtensionDirs)

	print('\nUPDATE COMPLETED\n')