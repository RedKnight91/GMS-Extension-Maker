import os
import utilityScripts as utils

def getUpToDateExtensionFiles(extensionDir):
	return utils.getDirectoryFiles(extensionDir)

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
		foundLogStr = 'Found project using {} extension: {}'.format(extensionName, project)
		print(foundLogStr)
		return True

	return False

def listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName):
	projectDirs = listProjectDirectories(projectsDir)
	matchingProjects = []

	for project in projectDirs:
		isSameProject = (project == extensionProjectDir)
		usesExtension = projectUsesExtension(project, extensionName)

		if (usesExtension and not isSameProject):
			projectExtensionPath = project + r'\extensions\{}'.format(extensionName)
			matchingProjects.append(projectExtensionPath)

	return matchingProjects

def confirmExtensionUpdate(dir):
	prompt = 'Update this extension (Y/N)? {}'.format(dir)
	return utils.promptChoice(prompt)

#Pushes an updated extension to all the projects which use it
def pushExtension(extPaths):
	print('\nPUSHING EXTENSION\n')

	projectsDir = extPaths['projectsDir']
	extensionProjectDir = extPaths['extensionProjectDir']
	extensionName = extPaths['extensionName']
	extensionDir = extPaths['extensionDir']

	print('[1/3] Finding extension files\n')
	extensionFiles = getUpToDateExtensionFiles(extensionDir)

	print('[2/3] Looking for projects using extension')
	matchingExtensionDirs = listProjectsUsingExtension(projectsDir, extensionProjectDir, extensionName)

	if (len(matchingExtensionDirs) == 0):
		print('\n[3/3] No projects found')
	else:
		print('\n[3/3] Pushing extension to projects')
		for extensionDir in matchingExtensionDirs:
			if (confirmExtensionUpdate(extensionDir)):
				utils.replaceDirFiles(extensionDir, extensionFiles)

	print('\nUPDATE COMPLETED\n')