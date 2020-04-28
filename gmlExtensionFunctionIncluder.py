import utilities as utils

def createFunctionFileJson(file):
	json = {
		'id'			: str(utils.makeUuidV4()),
		'modelName'		: 'GMExtensionFile',
		'mvc'			: '1.0',
		'ProxyFiles' 	: [],
		'constants'		: [],
		'copyToTargets'	: -1,
		'filename'		: utils.getFileName(file, False),
		'final'			: '',
		'functions'		: [],
		'init'			: '',
		'kind'			: 2,
		'order'			: [],
		'origname'		: '',
		'uncompress'	: 'false'
	}

	return json

def createFunctionFilesJson(extensionDir):
	files = utils.getDirectoryExtensionFiles(extensionDir, '.gml')

	filesJson = []
	
	for file in files:
		fileJson = createFunctionFileJson(file)
		filesJson.append(fileJson)

	return filesJson

def includeFunctionFilesToExtension(workPaths):
	print('\nINCLUDE FUNCTION FILES \n')

	extensionDir = workPaths.extension.dir
	extensionFile = workPaths.extension.file

	print('[1/2] Creating files JSON')
	filesJson = createFunctionFilesJson(extensionDir)

	print('[2/2] Writing JSON to file')
	extensionJson = utils.readFileJson(extensionFile)
	extensionJson['files'] = filesJson
	
	utils.writeFileJson(extensionFile, extensionJson)

	print('\nFUNCTION FILES INCLUDED \n')
