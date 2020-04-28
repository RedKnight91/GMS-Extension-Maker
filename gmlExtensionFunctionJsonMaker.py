import utilities as utils
import os

def getFunctionNames(functionsFile):
	functionNames = []

	defineLines = utils.getLinesContainingString(functionsFile, '#define')
	for line in defineLines:
		name = line.split()[1]
		functionNames.append(name)

	return functionNames

def makeFunctionJson(functionName):
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

def makeFunctionsJson(extensionDir, fileJson):
	fileName = fileJson['filename']
	functionsFile = os.path.join(extensionDir, fileName)
	functionNames = getFunctionNames(functionsFile)
	functionsJson = [makeFunctionJson(functionName) for functionName in functionNames]

	fileJson['functions']	= functionsJson
	fileJson['order']		= [function['id'] for function in functionsJson]
	

def includeFunctionsToExtension(workPaths):
	print('\nPOPULATING EXTENSION WITH FUNCTION JSON\n')

	extensionDir = workPaths.extension.dir
	extensionFile = workPaths.extension.file

	extensionJson = utils.readFileJson(extensionFile)
	functionFilesJson = extensionJson['files']

	print('[1/2] Making functions JSON')
	for functionFile in functionFilesJson:
		makeFunctionsJson(extensionDir, functionFile)
		
	print('[2/2] Writing JSON to extension')
	utils.writeFileJson(extensionFile, extensionJson)
	
	print('\nEXTENSION FILE POPULATED\n')