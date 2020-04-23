import utilityScripts as utils

def getFunctionNames(extensionFunctionsPath):
	functionNames = []

	defineLines = utils.getLinesContainingString(extensionFunctionsPath, '#define')

	for line in defineLines:
		name = line.split()[1]
		functionNames.append(name)

	return functionNames

def makeFunctionJson(functionName):
	json = {}

	json['id'] = str(utils.makeUuidV4())
	json['modelName'] = 'GMExtensionFunction'
	json['mvc'] = '1.0'
	json['argCount'] = -1
	json['args'] = []
	json['externalName'] = functionName
	json['help'] = ''
	json['hidden'] = 'false'
	json['kind'] = 2
	json['name'] = functionName
	json['returnType'] = 1

	return json

def makeFunctionsJson(extensionFunctionsPath):
	functionNames = []
	functions = []

	functionNames = getFunctionNames(extensionFunctionsPath)

	for functionName in functionNames:
		functionJson = makeFunctionJson(functionName)
		functions.append(functionJson)

	return functions

def makeFunctionOrderList(functionsJson):
	orderedUuidList = []

	for function in functionsJson:
		uuid = function['id']
		orderedUuidList.append(uuid)

	return orderedUuidList

def populateFileFunctions(extensionDir, fileJson):
	functionsFilePath = r'{}\{}'.format(extensionDir, fileJson['filename'])
	functionsJson = makeFunctionsJson(functionsFilePath)
	functionOrderList = makeFunctionOrderList(functionsJson)
	
	utils.setJsonChild(fileJson, 'functions', functionsJson)
	utils.setJsonChild(fileJson, 'order', functionOrderList)

def populateExtensionFunctionJson(extPaths):
	print('\nPOPULATING EXTENSION WITH FUNCTION JSON\n')

	extensionDir = extPaths['extensionDir']
	extensionFile = extPaths['extensionFile']

	extensionJson = utils.readFileJson(extensionFile)
	filesJson = extensionJson['files']

	print('[1/2] Making functions JSON')
	for fileJson in filesJson:
		populateFileFunctions(extensionDir, fileJson)
		
	print('[2/2] Writing JSON to extension')
	utils.writeFileJson(extensionFile, extensionJson)
	
	print('\nEXTENSION FILE POPULATED\n')