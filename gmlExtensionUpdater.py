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

def projectUsesExtension(project, extensionName):
	projectExtensionPath = project + r'\extensions\{}'.format(extensionName)
	hasMatchingExtensionDir = (os.path.exists(projectExtensionPath))

	if (hasMatchingExtensionDir):
		print('Project match: {}'.format(project))

	return hasMatchingExtensionDir

def listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName):
	projectDirs = utils.getDirectoriesContainingFileType(projectsDir, 'yyp')
	matchingProjects = []

	for dir in projectDirs:
		isSameProject = (dir == extensionProjectDir)
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

def copyResourcesToProject(workPaths, project, scriptDirs, objectDirs, extensionDirs):
	copier.copyScriptsToProject(workPaths, project, scriptDirs)
	copier.copyObjectsToProject(workPaths, project, objectDirs)
	copier.copyExtensionsToProject(workPaths, project, extensionDirs)

def updateExtensionToProjects(workPaths):
	print('\nPUSHING EXTENSION\n')

	projectsDir = workPaths.projectsDir
	extensionProjectDir = workPaths.extensionProject.dir
	extensionName = workPaths.extension.name

	print('\n[1/3] Looking for projects using {} extension'.format(extensionName))
	projectsUsingExt = listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName)

	if not projectsUsingExt:
		print('\n[2/3] No projects found')
		exit

	print('\n[2/3] Retrieving extension files\n')
	sourceScriptDirs= locator.locateScripts(workPaths)
	sourceObjectDirs= locator.locateObjects(workPaths)
	sourceExtensionDirs	= locator.locateExtensions(workPaths)

	print('\n[3/3] Pushing extension to projects')
	updateAll = promptExtensionUpdateAll()

	for project in projectsUsingExt:
		if (updateAll or confirmProjectUpdate(project)):
			copyResourcesToProject(workPaths, project, sourceScriptDirs, sourceObjectDirs, sourceExtensionDirs)

	print('\nUPDATE COMPLETED\n')