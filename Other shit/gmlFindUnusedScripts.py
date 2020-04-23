import os
import json

projectDir = r'C:\Users\mikec\Documents\Github\bitblock_blast'


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

def extractResourceName(path):
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
				path = value['resourcePath']
				name = extractResourceName(path)
				scripts.append(name)

	return scripts


def selfScriptFile(script, filePath):
	fileName = extractResourceName(filePath)
	isSelf = (fileName == script)
	return isSelf

def strInLine(string, line):
	line = line.replace(" ", "")
	return string in line

def getFileScriptCalls(script, file):
	calls = 0
	callsCommented = 0
	
	#TODO
	#inline comments
	#Match preceded by ///@
	#Match receded by //
	#Comment opened with /* and not yet closed by */
	commented = False
	
	for line in file:
		if strInLine(script, line):
			if (commented):
				callsCommented += 1
			else:
				calls += 1
				
	return [calls, callsCommented]

def getDirScriptCalls(script, dir):
	calls = [0, 0]

	files = getDirectoryFiles(dir)
	
	for filePath in files:
		valid = validFile(filePath, '.gml')
		_self = selfScriptFile(script, filePath)
		if (valid and not _self):
			with open(filePath, 'r') as file:
				fileCalls = getFileScriptCalls(script, file)
				calls[0] += fileCalls[0]
				calls[1] += fileCalls[1]
	
	return calls
				
def getScriptCalls(script):
	objCalls = getDirScriptCalls(script, projectDir + r'\objects')
	scrCalls = getDirScriptCalls(script, projectDir + r'\scripts')
	roomCalls = getDirScriptCalls(script, projectDir + r'\rooms')
	
	calls = [0, 0]
	calls[0] = objCalls[0] + scrCalls[0] + roomCalls[0]
	calls[1] = objCalls[1] + scrCalls[1] + roomCalls[1]
	
	return calls


def outputScriptUsage(script, scriptCalls):
	callNum = scriptCalls[0]
	callCommentedNum = scriptCalls[1]

	output = ''

	if (callNum == 0):
		if (callCommentedNum > 0):
			commentOutput = (script + ' has ' + callCommentedNum + ' commented calls.')
			output = commentOutput
		else:
			regularOutput = (script + ' is unused.')
			output = '\n'.join([output, regularOutput])

	return output
	
	

def findUnusedScripts():
	scriptList = sorted(getProjectScriptList())
	scriptN = len(scriptList)

	print('\n UNUSED SCRIPTS: \n')

	output = []

	for i, script in enumerate(scriptList):
		scriptCalls = getScriptCalls(script)
		
		print(str(i) + '/' + str(scriptN))

		output.append(outputScriptUsage(script, scriptCalls))

	#Clear empty strings from list
	emptyStrfilter = filter(lambda x: x != "", output)
	output = list(emptyStrfilter)

	for line in output:
		print(line)

	print('\n ALL SCRIPTS CHECKED \n')

	return





findUnusedScripts()