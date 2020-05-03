import os
import utilities as utils
import gmsUtilities as gms
from gmsUtilities import Project
import gmlExtensionFileCopier as copier
import gmlExtensionResourceIncluder as resourceIncluder

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
		return True

	return False

def listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName):
	projectDirs = utils.getSubDirectoriesContainingFileType(projectsDir, 'yyp')
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

#Pushes an updated extension to all the projects which use it
def pushExtension(workPaths):
	print('\nPUSHING EXTENSION\n')

	projectsDir = workPaths.projectsDir
	extensionProjectDir = workPaths.extensionProject.dir
	extensionName = workPaths.extension.name
	extensionProject = workPaths.extensionProject

	print('[1/3] Retrieving extension files\n')
	scriptDirs = utils.getSubDirectories(extensionProject.scriptsDir)
	objectDirs = utils.getSubDirectories(extensionProject.objectsDir)
	extensionDirs = utils.getSubDirectories(extensionProject.extensionsDir)

	print('[2/3] Looking for projects using {} extension'.format(extensionName))
	projectsUsingExt = listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName)

	if (len(projectsUsingExt) == 0):
		print('\n[3/3] No projects found')
	else:
		print('\n[3/3] Pushing extension to projects')
		updateAll = promptExtensionUpdateAll()

		for project in projectsUsingExt:
			if (updateAll or confirmProjectUpdate(project)):
				copier.copyScriptsToProject(workPaths, project, scriptDirs)
				copier.copyObjectsToProject(workPaths, project, objectDirs)
				copier.copyExtensionsToProject(workPaths, project, extensionDirs)

				#TODO is this already done in copyXtoProject?
				# resourceIncluder.includeScriptsToProject(workPaths, project)
				# resourceIncluder.includeObjectsToProject(workPaths, project)
				# resourceIncluder.includeExtensionsToProject(workPaths, project)

	print('\nUPDATE COMPLETED\n')