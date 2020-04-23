import os
import json

projectDir = r'C:\Users\mikec\Documents\GameMakerStudio2\TweenGMS Pro'


def getMatchingFile(files, extension):
	match = None

	for filePath in files:
		if (validFile(filePath, extension)):
			match = filePath
			break

	return match

def getDirectoryFiles(path):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			fileList.append(os.path.join(root, file))

	return fileList

def validFile(filePath, extension):
	valid = filePath.endswith(extension)
	return valid

def extractPathName(path):
	#Extract filename, split in [name, extension]
	name = os.path.basename(path)
	name = os.path.splitext(name)
	return name[0]

def getProjectScriptList():
	scripts = []
	files = getDirectoryFiles(projectDir)
	yypPath = getMatchingFile(files, '.yyp')

	with open(yypPath, 'r') as yypFile:
		yypJson = json.load(yypFile)
		resources = yypJson['resources']
		
		for resource in resources:
			value = resource['Value']
			type = value['resourceType']
			if (type == 'GMScript'):
				scripts.append(resource)

	return scripts

def getScriptName(scriptResource):
	value = scriptResource['Value']
	path = value['resourcePath']
	name = extractPathName(path)

	return name

def listScriptNamesAndKeys(scriptList):
	nameKeylist = []

	for script in scriptList:
		scriptObj = {}
		scriptObj['name'] = getScriptName(script)
		scriptObj['key'] = script['Key']
		nameKeylist.append(scriptObj)

	return nameKeylist
	

def makeSortedKeyList(scriptList):
	#Order scripts by name
	scriptList = sorted(scriptList, key = lambda script: script['name'].lower())

	keyList = []

	for script in scriptList:
		keyList.append(script['key'])

	return keyList

def makeSortedNameList(scriptList):
	#Order scripts by name
	scriptList = sorted(scriptList, key = lambda script: script['name'].lower())

	nameList = []

	for script in scriptList:
		nameList.append(script['name'])

	return nameList

def writeOrderedScriptsToFile(keyList):
	files = getDirectoryFiles(projectDir)
	yypPath = getMatchingFile(files, '.yyp')

	with open(yypPath, 'r') as yypFile:
		yypJson = json.load(yypFile)

	yypJson['script_order'] = keyList

	with open(yypPath, 'w') as yypFile:
		json.dump(yypJson, yypFile)

def printList(l):
	print('[')

	for item in l:
		print(r'"' + item + r'",')

	print(']')


def gmlScriptsOrderByName():
	scriptList = getProjectScriptList()
	scriptList = listScriptNamesAndKeys(scriptList)

	#nameList = makeSortedNameList(scriptList)
	#printList(nameList)

	keyList = makeSortedKeyList(scriptList)

	#NOTE: I thought it would be enough to update the .yyp 'script_order' node, NOPE!
	#You also have to find the View (in the Views folder) for scripts, and edit that as well.

	#Use this if you want to manually copy the ordered list to the view file.
	printList(keyList)

	#writeOrderedScriptsToFile(keyList)

	return





gmlScriptsOrderByName()