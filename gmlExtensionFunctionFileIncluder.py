import utilityScripts as utils

def createFunctionFileJson(file):
	json = {}

	json['id'] = str(utils.makeUuidV4())
	json['modelName'] = 'GMExtensionFile'
	json['mvc'] = '1.0'
	json['ProxyFiles'] = []
	json['constants'] = []
	json['copyToTargets'] = -1
	json['filename'] = utils.getFileName(file)
	json['final'] = ''
	json['functions'] = []
	json['init'] = ''
	json['kind'] = 2
	json['order'] = []
	json['origname'] = ''
	json['uncompress'] = 'false'

	return json

def createFunctionFilesJson(extensionDir):
	files = utils.getDirectoryExtensionFiles(extensionDir, '.gml')

	filesJson = []
	
	for file in files:
		fileJson = createFunctionFileJson(file)
		filesJson.append(fileJson)

	return filesJson

def includeFunctionFilesToExtension(extPaths):
	print('\nINCLUDE FUNCTION FILES \n')

	extensionDir = extPaths['extensionDir']
	extensionFile = extPaths['extensionFile']

	print('[1/2] Creating files JSON')
	filesJson = createFunctionFilesJson(extensionDir)

	print('[2/2] Writing JSON to file')
	extensionJson = utils.readFileJson(extensionFile)
	extensionJson['files'] = filesJson
	
	utils.writeFileJson(extensionFile, extensionJson)

	print('\nFUNCTION FILES INCLUDED \n')
