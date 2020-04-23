import os
import json
import utilityScripts as utils


def getExtensionFile(extensionDir):
	files = utils.getDirectoryFilesRecursive(extensionDir)
	extensionPath = utils.getMatchingFile(files, '.yy')

	return extensionPath 

def getFuncNameFromJsdoc(line):
	lineParts = line.split('(')
	funcName = lineParts[0]
	return funcName

def getJsdocs(jsdocFilePath):
	jsdocs = {}

	with (open(jsdocFilePath, 'r')) as jsdocFile:
		jsdocs = json.load(jsdocFile)

	return jsdocs

def formatArgsBlock(argumentJson):
	args = []
	stringType = 1
	# doubleType = 2

	for _ in argumentJson:
		args.append(stringType)

	return args

def getArgCount(argList, variableLengthArgs):
	argLen = len(argList)
	count = (argLen, -1)[variableLengthArgs]
	return count

def injectFunctionJsdoc(jsdoc, function):
	helpLine = jsdoc['helpLine']
	argsBlock = formatArgsBlock(jsdoc['arguments'])
	argCount = getArgCount(argsBlock, True)

	utils.setJsonChild(function, 'help', helpLine)
	utils.setJsonChild(function, 'args', argsBlock)
	utils.setJsonChild(function, 'argCount', argCount)

	return function

def injectFileJsdocs(fileJson, jsdocs):
	functionsJson = utils.getJsonChild(fileJson, 'functions')
	injectedFunctions = []

	for functionJson in functionsJson:
		name = utils.getJsonChild(functionJson, 'externalName')
		jsdoc = jsdocs[name]
		injectedFunction = injectFunctionJsdoc(jsdoc, functionJson)
		injectedFunctions.append(injectedFunction)

	return injectedFunctions

def injectJsdocs(extensionPath, jsdocFile):
	jsdocs = getJsdocs(jsdocFile)

	extensionJson = utils.readFileJson(extensionPath)
	includedFilesJson = utils.getJsonChild(extensionJson, 'files')
	injectedFilesJson = []

	for fileJson in includedFilesJson:
		injectedFile = injectFileJsdocs(fileJson, jsdocs)

		utils.setJsonChild(fileJson, 'functions', injectedFile)
		injectedFilesJson.append(fileJson)

	utils.setJsonChild(extensionJson, 'files', injectedFilesJson)

	return extensionJson


def injectExtensionJsdocs(extPaths):
	print('\nINJECT JSDOCS\n')

	extensionDir = extPaths['extensionDir']
	jsdocFile = extPaths['combinedJsdocFile']

	print('[1/3] Finding extension file')
	extensionPath = getExtensionFile(extensionDir)
	if (extensionPath == None):
		raise Exception('Extension file not found')

	print('[2/3] Making injected file JSON')
	extensionJson = injectJsdocs(extensionPath, jsdocFile)

	print('[3/3] Writing JSON to file')
	utils.writeFileJson(extensionPath, extensionJson)

	print('\nJSDOCS INJECTED\n')