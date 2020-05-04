import os
import json
import utilities as utils

validParamTags = ['@param', '@arg', '@argument']

def makeScriptFilePath(scriptDir):
	dirName = os.path.basename(scriptDir)
	script = os.path.join(scriptDir, dirName) + '.gml'
	return script

def parseScriptName(filePath):
	scriptName = os.path.basename(filePath)
	scriptName = scriptName.replace('.gml', '')
	return scriptName

def getParamTag(string):
	for tag in validParamTags:
		if (tag in string):
			return tag

	return ''

def extractArgumentName(string, paramTag):
	words = string.split()

	if (paramTag in words):
		paramTagIndex = words.index(paramTag)
	else:
		paramTagIndex = words.index('///' + paramTag)
		
	argIndex = paramTagIndex + 1
	argName = words[argIndex]

	return argName

def getArgumentNames(fileContent):
	args = []
	for line in iter(fileContent.splitlines()):
		paramTag = getParamTag(line)
		
		if (paramTag in validParamTags):
			argName = extractArgumentName(line, paramTag)
			args.append(argName)

	return args

def buildArgumentListLine(arguments):
	argumentListLine = ''
	for arg in arguments:
		argumentListLine += arg + ', '

	argumentListLine = argumentListLine[:-2]

	return argumentListLine

def buildDefineLine(filePath):
	scriptName = parseScriptName(filePath)
	define = '#define ' + scriptName + '\n'
	return define

def buildJsdocFuncLine(filePath, argListLine):
	scriptName = parseScriptName(filePath)
	define = scriptName + '(' + argListLine + ')'
	return define

def generateFunctionData(filePath, file):
	fileContent = file.read()
	arguments = getArgumentNames(fileContent)
	argListLine = buildArgumentListLine(arguments)

	defineLine = buildDefineLine(filePath)
	jsdocFuncLine = buildJsdocFuncLine(filePath, argListLine)

	function = defineLine + '///@func ' + jsdocFuncLine + '\n' + fileContent + '\n\n\n'
	return [function, jsdocFuncLine, arguments]

def generateFunctionBody(filePath, file, jsdoc):
	fileContent = file.read()
	defineLine = buildDefineLine(filePath)
	jsdocFuncLine = jsdoc['helpLine']

	functionBody = defineLine + '///@func ' + jsdocFuncLine + '\n' + fileContent + '\n\n\n'
	return functionBody


def generateFunctionArgList(file):
	fileContent = file.read()
	arguments = getArgumentNames(fileContent)

	return arguments


def generateFunctionJsdoc(filePath, arguments):
	argListLine = buildArgumentListLine(arguments)
	jsdocFuncLine = buildJsdocFuncLine(filePath, argListLine)

	return jsdocFuncLine


def combineFunctions(scripts, jsdocs):
	combinedFunctions = ''

	for scriptPath in scripts:
		with open(scriptPath, 'r') as script:
			scriptName = parseScriptName(scriptPath)
			jsdoc = jsdocs[scriptName]
			combinedFunctions += generateFunctionBody(scriptPath, script, jsdoc)

	return combinedFunctions


def combineJsdocs(scripts):
	combinedJsdocs = {}

	for scriptPath in scripts:
		with open(scriptPath, 'r') as script:
			arguments = generateFunctionArgList(script)
			functionJsdoc = {
				'arguments' : arguments,
				'helpLine' : generateFunctionJsdoc(scriptPath, arguments)
			}

		scriptName = parseScriptName(scriptPath)
		combinedJsdocs[scriptName] = functionJsdoc

	return combinedJsdocs


def writeCombinedFiles(jsdocs, functions, combinedFilesDir, functionsFilePath, jsdocFilePath):
	if (not os.path.exists(combinedFilesDir)):
		os.mkdir(combinedFilesDir)

	print('Writing {}'.format(functionsFilePath))
	utils.writeFile(functionsFilePath, functions)

	print('Writing {}'.format(jsdocFilePath))
	utils.writeJson(jsdocFilePath, jsdocs)


def combineScripts(workPaths, scriptDirs):
	print('\nCOMBINE SCRIPTS\n')

	combinedDir	= workPaths.combinedFunctions.dir
	functionsFile = workPaths.combinedFunctions.file
	jsdocFile = workPaths.combinedJsdocs.file

	scripts = [makeScriptFilePath(scriptDir) for scriptDir in scriptDirs]

	print('[1/2] Combining scripts, combining jsdocs')
	combinedJsdocs		= combineJsdocs(scripts)
	combinedFunctions	= combineFunctions(scripts, combinedJsdocs)

	print('[2/2] Writing files')
	writeCombinedFiles(combinedJsdocs, combinedFunctions, combinedDir, functionsFile, jsdocFile)

	

	print('\nSCRIPTS COMBINED\n')