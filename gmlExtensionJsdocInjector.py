import os
import json
import utilities as utils


def getFuncNameFromJsdoc(line):
	lineParts = line.split('(')
	funcName = lineParts[0]
	return funcName

def formatArgsBlock(argumentJson):
	stringType = 1
	# doubleType = 2

	args = [stringType] * len(argumentJson)
	return args

def countArgs(argList, variableLengthArgs):
	if variableLengthArgs:
		return -1
	else:
		return len(argList)


def includeFunctionJsdocsToExtension(workPaths):
	print('\nINJECT JSDOCS\n')

	extensionFile = workPaths.extension.file
	extensionJson = utils.readJson(extensionFile)
	jsdocsFile = workPaths.combinedJsdocs.file
	jsdocsJson = utils.readJson(jsdocsFile)

	def injectFunctionJsdoc(function):		
		name = function['externalName']
		jsdoc = jsdocsJson[name]
		args = formatArgsBlock(jsdoc['arguments'])

		function.update({
			'help'		: jsdoc['helpLine'],
			'args'		: args,
			'argCount'	: countArgs(args, True)
		})

		return function

	def injectFileJsdocs(fileJson):
		fileJson['functions'] = [injectFunctionJsdoc(function) for function in fileJson['functions']]
		return fileJson


	print('[1/2] Making injected file JSON')
	extensionJson['files'] = [injectFileJsdocs(file) for file in extensionJson['files']]

	print('[2/2] Writing JSON to file')
	utils.writeJson(extensionFile, extensionJson)

	print('\nJSDOCS INJECTED\n')