import os
import json
import utilities as utils

validParamTags = ['@param', '@arg', '@argument']

def makeScriptFilePath(scriptDir):
	dirName = utils.getFileName(scriptDir, True)
	script = os.path.join(scriptDir, dirName) + '.gml'
	return script

def makeScriptHead(scriptPath):
	name = utils.getFileName(scriptPath, True)
	head = '//{}\n'.format(name)
	return head

def makeScriptChunk(scriptPath):
	head = makeScriptHead(scriptPath)

	with open(scriptPath, 'r') as script:
		body = script.read()

	foot = '\n//SCRIPT END\n\n\n'

	return head + body + foot


def appendScripts(scripts):
	combinedScripts = ''

	for scriptPath in scripts:
		combinedScripts += makeScriptChunk(scriptPath)
		
	return combinedScripts

def writeCombinedScriptFile(scripts, combinedFilesDir, functionsFilePath):
	if (not os.path.exists(combinedFilesDir)):
		os.mkdir(combinedFilesDir)

	print('Writing {}'.format(functionsFilePath))
	utils.writeFile(functionsFilePath, scripts)


def combineScripts(workPaths, scriptDirs):
	print('\nCOMBINE SCRIPTS\n')

	combinedDir	= workPaths.combinedScripts.dir
	combinedScriptsFile = workPaths.combinedScripts.file

	scripts = [makeScriptFilePath(scriptDir) for scriptDir in scriptDirs]

	print('[1/2] Combining scripts')
	combinedScripts	= appendScripts(scripts)

	print('[2/2] Writing combined file')
	writeCombinedScriptFile(combinedScripts, combinedDir, combinedScriptsFile)

	print('\nSCRIPTS COMBINED\n')