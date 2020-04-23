import os
import json

projectDir = r'C:\Users\mikec\Documents\Github\bitblock_blast'


def getDirFiles(path):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			fileList.append(os.path.join(root, file))

	return fileList

def validFile(filePath, extension):
	valid = filePath.endswith(extension)
	return valid

def getDirScripts(dir):
	files = getDirFiles(dir)
	validFiles = []

	for filePath in files:
		valid = validFile(filePath, '.gml')
		if (valid):
			validFiles.append(filePath)
	
	return validFiles

def countLineSemicolons(line):
	count = line.count(';')
	return count

def removeLineSemicolons(line):
	line = line.replace(';', '')
	return line

def isCharAtEOL(char, line):
	line = ''.join(line.split())
	pos = line.find(char)

	EOL = len(line) - 1
	isEOL = (pos == EOL)

	return isEOL

def validSemicolonLine(line):
	semicolonCount = countLineSemicolons(line)
	singleSemicolon = (semicolonCount == 1)
	semicolonAtEnd = isCharAtEOL(';', line)
	valid = (singleSemicolon and semicolonAtEnd)

	return valid

def removeFileSemicolons(file):
	cleanedFile = []

	for line in file:
		if (validSemicolonLine(line)):
			line = removeLineSemicolons(line)
		
		cleanedFile.append(line)

	return cleanedFile

def removeDirSemicolons(dir):
	scripts = getDirScripts(dir)

	for scriptPath in scripts:
		with open(scriptPath, 'r') as script:
		   scriptCleaned = removeFileSemicolons(script)

		with open(scriptPath, 'w+') as script:
			for line in scriptCleaned:
				script.write(line)

def removeSemicolons():
	removeDirSemicolons(projectDir + r'\objects')
	removeDirSemicolons(projectDir + r'\scripts')
	removeDirSemicolons(projectDir + r'\rooms')

	return





removeSemicolons()