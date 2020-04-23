import os
import shutil
import json
import uuid

def getDirectoryFiles(path):
	fileList = []
	dirContent = next(os.walk(path))
	root = dirContent[0]
	files = dirContent[2]

	for file in files:
		fileList.append(os.path.join(root, file))

	return fileList

def getDirectoryExtensionFiles(path, extension):
	fileList = []
	dirContent = next(os.walk(path))
	root = dirContent[0]
	files = dirContent[2]

	for file in files:
		if (fileMatchesExtension(file, extension)):
			fileList.append(os.path.join(root, file))

	return fileList


def getDirectoryFilesRecursive(path):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			fileList.append(os.path.join(root, file))

	return fileList

def getDirectoryExtensionFilesRecursive(path, extension):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			if (fileMatchesExtension(file, extension)):
				fileList.append(os.path.join(root, file))

	return fileList


def getSubDirectories(path):
	dirList = []
	dirContent = next(os.walk(path))
	root = dirContent[0]
	directories = dirContent[1]

	for dir in directories:
		dirList.append(os.path.join(root, dir))

	return dirList


def getSubDirectoriesRecursive(path):
	dirList = []

	for root, directories, _ in os.walk(path):
		for dir in directories:
			dirList.append(os.path.join(root, dir))

	return dirList

def fileMatchesExtension(filePath, extension):
	match = filePath.endswith(extension)
	return match


def getMatchingFile(files, extension):
	match = None

	for filePath in files:
		if (fileMatchesExtension(filePath, extension)):
			match = filePath
			break

	return match


def dirContainsFileType(dir, extension):
	files = getDirectoryFiles(dir)

	for file in files:
		if (fileMatchesExtension(file, extension)):
			return True

	return False

def dirContainsFileTypeRecursive(dir, extension):
	for _, _, files in os.walk(dir):
		for file in files:
			if (fileMatchesExtension(file, extension)):
				return True

	return False


def deleteDirectoryFiles(dir):
	for child in os.listdir(dir):
		childPath = os.path.join(dir, child)
		os.remove(childPath)


def copyFilesToDirectory(files, dir):
	for file in files:
		shutil.copy(file, dir)


def replaceDirFiles(dir, files):
	deleteDirectoryFiles(dir)
	copyFilesToDirectory(files, dir)

def getFileName(path):
	return os.path.basename(path)

def getDirName(path):
	return os.path.basename(path)

def getLinesContainingString(filePath, string):
	matches = []

	with open(filePath, 'r') as file:
		for line in file:
			if (string in line):
				matches.append(line)

	return matches

def readFileJson(filePath):
	with open(filePath, 'r') as file:
		content = json.load(file)

	return content

def writeFileJson(filePath, content):
	with open(filePath, 'w') as file:
		json.dump(content, file, indent = 4)

def getJsonChild(object, key):
	child = object[key]
	return child


def setJsonChild(object, key, value):
	object[key] = value


def promptChoice(prompt):
	print(prompt)
	choice = input()

	return (choice.upper() == 'Y')

def makeUuidV4():
	return uuid.uuid4()