import os

def concatenateExtensionPaths(extPaths):
	extensionName = extPaths['extensionName']
	extensionProjectDirName = extPaths['extensionProjectDirName']
	projectDirName = extPaths['projectDirName']
	extensionsSubDir = extPaths['extensionsSubDir']
	projectsDir = extPaths['projectsDir']

	projectDir = r'{}\{}\{}\{}'.format(projectsDir, extensionsSubDir, projectDirName, projectDirName)
	scriptsDir = r'{}\scripts'.format(projectDir)
	extensionProjectDir = r'{}\{}\{}\{}'.format(projectsDir, extensionsSubDir, projectDirName, extensionProjectDirName)
	extensionDir = r'{}\extensions\{}'.format(extensionProjectDir, extensionName)
	combinedFilesDir = r'C:\Users\mikec\Desktop\GMLCombinerResults\{}'.format(projectDirName)

	functionsFileName = '{}_functions.gml'.format(projectDirName)
	jsdocFileName = 'jsdocs_combined.gml'

	functionsFile = extensionDir + '\\' + functionsFileName
	extensionFile = extensionDir + '\\' + extensionName + '.yy'
	combinedFunctionsFile = combinedFilesDir + '\\' + functionsFileName
	combinedJsdocFile = combinedFilesDir + '\\' + jsdocFileName

	if (not os.path.exists(projectDir)):
		raise Exception('Project not found:\n {}'.format(projectDir))

	if (not os.path.exists(extensionProjectDir)):
		raise Exception('Extension project not found:\n {}'.format(extensionProjectDir))
		
	if (not os.path.exists(extensionDir)):
		raise Exception('Extension folder not found:\n {}'.format(extensionDir))

	extPaths['projectDir'] = projectDir
	extPaths['scriptsDir'] = scriptsDir
	extPaths['extensionProjectDir'] = extensionProjectDir
	extPaths['extensionDir'] = extensionDir
	extPaths['combinedFilesDir'] = combinedFilesDir
	extPaths['functionsFileName'] = functionsFileName
	extPaths['jsdocFileName'] = jsdocFileName
	extPaths['functionsFile'] = functionsFile
	extPaths['extensionFile'] = extensionFile
	extPaths['combinedFunctionsFile'] = combinedFunctionsFile
	extPaths['combinedJsdocFile'] = combinedJsdocFile
