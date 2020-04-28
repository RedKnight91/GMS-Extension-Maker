import utilities as utils

def copyFunctionsFileToExtensionDir(workPaths):
	print('\nCOPYING FUNCTIONS FILE\n')

	extensionDir = workPaths.extension.dir

	prompt = 'Would you like to copy the combined functions file to the extension folder? (Y/N)\n {}'.format(extensionDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		functions = [workPaths.combinedFunctions.file]
		utils.replaceFilesToDir(functions, extensionDir)

	print('\nFUNCTIONS FILE COPIED\n')


def copyExternalResourcesToExtensionDir(resourceDir, externalResources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	prompt = 'Copy external resources to this folder? (Y/N)\n{}'.format(resourceDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		utils.replaceDirectoriesToDir(externalResources, resourceDir)

	#TODO Include files in project .yyp

	print('\nRESOURCE DIRECTORIES COPIED\n')