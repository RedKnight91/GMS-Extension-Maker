import utilities as utils
import os

def getFunctionNames(functionsFile):
	functionNames = []

	defineLines = utils.getLinesContainingString(functionsFile, '#define')
	for line in defineLines:
		name = line.split()[1]
		functionNames.append(name)

	return functionNames

def createFunctionJson(functionName):
	json = {
		'id'			: str(utils.makeUuidV4()),
		'modelName'		: 'GMExtensionFunction',
		'mvc'			: '1.0',
		'argCount'		: -1,
		'args'			: [],
		'externalName'	: functionName,
		'help'			: '',
		'hidden'		: 'false',
		'kind'			: 2,
		'name'			: functionName,
		'returnType'	: 1
	}

	return json

def createFunctionsJson(extensionDir, fileJson):
	fileName = fileJson['filename']
	functionsFile = os.path.join(extensionDir, fileName)
	functionNames = getFunctionNames(functionsFile)
	functionsJson = [createFunctionJson(functionName) for functionName in functionNames]

	fileJson['functions']	= functionsJson
	fileJson['order']		= [function['id'] for function in functionsJson]

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
	
	print('\nFUNCTION FILES INCLUDED \n')
	print('\nPOPULATING EXTENSION WITH FUNCTION JSON\n')

	print('[1/2] Making functions JSON')
	for functionFile in filesJson:
		createFunctionsJson(extensionDir, functionFile)
		
	print('[2/2] Writing JSON to extension')
	utils.writeFileJson(extensionFile, extensionJson)
	
	print('\nEXTENSION FILE POPULATED\n')