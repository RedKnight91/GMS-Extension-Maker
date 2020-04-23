import utilityScripts as utils

def copyCombinedFilesToExtensionDir(extPaths):
	print('\nCOPY FILE\n')

	extensionDir = extPaths['extensionDir']
	functionsFile = extPaths['combinedFunctionsFile']

	prompt = 'Would you like to copy the combined files to the extension folder? (Y/N)\n {}'.format(extensionDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		files = [functionsFile]
		utils.copyFilesToDirectory(files, extensionDir)

	print('\nFUNCTIONS FILE COPIED\n')