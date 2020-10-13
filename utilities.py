import os
import glob
import shutil
import json
import uuid
from jsoncomment import JsonComment

#Creates a file path
def makePath(dir, name, extension):
	path = os.path.join(dir, name) + '.' + extension
	return path

#Creates a list of file paths in the same dir
def makePathList(dir, names, extension):
	paths = [makePath(dir, name, extension) for name in names]
	return paths

#Gets file names from paths
def extractFileNames(paths, excludeExtension):
	names = []

	for path in paths:
		name = getFileName(path, excludeExtension)
		names.append(name)

	return names

def replaceExtension(path, extension):
	noExtPath = os.path.splitext(path)[0]
	newExtPath = noExtPath + '.' + extension
	return newExtPath

def removeExtension(name):
	name = os.path.splitext(name)[0]
	return name

def getDirFiles(path):
	fileList = []
	dirContent = next(os.walk(path))
	root = dirContent[0]
	files = dirContent[2]

	for file in files:
		fileList.append(os.path.join(root, file))

	return fileList

def getDirExtensionFiles(path, extension):
	fileList = []
	dirContent = next(os.walk(path))
	root = dirContent[0]
	files = dirContent[2]

	for file in files:
		if (fileMatchesExtension(file, extension)):
			fileList.append(os.path.join(root, file))

	return fileList


def getDirFilesRecursive(path):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			fileList.append(os.path.join(root, file))

	return fileList

def getDirExtensionFilesRecursive(path, extension):
	fileList = []
	for root, _, files in os.walk(path):
		for file in files:
			if (fileMatchesExtension(file, extension)):
				fileList.append(os.path.join(root, file))

	return fileList

#Gets all child directories which contain a file with a specific extension
def getSubDirectoriesContainingFileType(path, extension):
	os.chdir(path)
	fileFormat = '**/*.{}'.format(extension)
	files = glob.glob(fileFormat, recursive = True)

	matchingDirs = [os.path.dirname(os.path.abspath(file)) for file in files]
	
	return matchingDirs

#Gets all child directories which contain a file with a specific extension
#Doesn't look in a directories children if the file is found in the directory
def getDirectoriesContainingFileType(path, extension):
	subdirs = []
	contents = os.listdir(path)

	for item in contents:
		item = os.path.join(path, item)

		if os.path.isdir(item):
			subdirs.append(item)
		elif os.path.isfile(item) and item.endswith('.' + extension):
			return [path]

	matchingDirs = []
	for dir in subdirs:
		matchingDirs.extend(getDirectoriesContainingFileType(dir, extension))

	return matchingDirs

def getSubDirectories(path):
	if (not os.path.exists(path)):
		return []

	dirContent = next(os.walk(path))
	root = dirContent[0]
	directories = dirContent[1]

	dirList = [os.path.join(root, dir) for dir in directories]

	return dirList


def getSubDirectoriesRecursive(path):
	if (not os.path.exists(path)):
		return []
		
	for root, directories, _ in os.walk(path):
		dirList = [os.path.join(root, dir) for dir in directories]

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
	files = getDirFiles(dir)

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


def deleteDirFiles(dir):
	for child in os.listdir(dir):
		childPath = os.path.join(dir, child)
		os.remove(childPath)

def copyDirectoriesToDir(dirs, dest):
	for dir in dirs:
		if (not os.path.exists(dir)):
			dirName = os.path.basename(dir)
			fullDest = os.path.join(dest, dirName)
			shutil.copytree(dir, fullDest)

def copyFilesToDir(files, dir):
	for file in files:
		newPath = os.path.join(dir, os.path.basename(file))
		if (not os.path.exists(newPath)):
			shutil.copy(file, dir)

def replaceDirectoriesToDir(dirs, dest):
	for dir in dirs:
		dirName = os.path.basename(dir)
		fullDest = os.path.join(dest, dirName)

		if os.path.exists(fullDest):
			shutil.rmtree(fullDest)

		shutil.copytree(dir, fullDest)

def replaceFilesToDir(files, dir):
	for file in files:
		shutil.copy(file, dir)

def replaceDirFiles(dir, files):
	deleteDirFiles(dir)
	copyFilesToDir(files, dir)

def getFileName(path, _removeExtension):
	name = os.path.basename(path)
	if (_removeExtension):
		name = removeExtension(name)

	return name

def getDirName(path):
	name = os.path.basename(path)
	return name

def getParentDir(path):
	path = os.path.dirname(path) #remove file name
	parentDir = os.path.split(path)[0] #remove last dir
	return parentDir

def getDir(path):
	path = os.path.dirname(path)
	return dir

def getLinesContainingString(filePath, string):
	matches = []

	with open(filePath, 'r') as file:
		for line in file:
			if (string in line):
				matches.append(line)

	return matches

def writeFile(filePath, content):
	with open(filePath, 'w') as file:
		file.write(content)

def readJson(filePath):
	with open(filePath, 'r') as file:
		content = JsonComment().load(file)

	return content

def writeJson(filePath, content):
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

def printList(list):
	print('[')
	for item in list:
		print('    {},'.format(item))
	print(']')

def makeUuidV4():
	return uuid.uuid4()

def getMatchingJsonObject(jsonObjects, key, value):
	for object in jsonObjects:
		if (object[key] == value):
			return object

	return None

#Splits a path into a list of its dirs (and file)
def splitPath(path):
    path = os.path.normpath(path)
    parts = []

    while True:
        head, tail = os.path.split(path)
        if head == path:  # sentinel for absolute paths
            parts.insert(0, head)
            break
        elif tail == path: # sentinel for relative paths
            parts.insert(0, tail)
            break
        else:
            path = head
            parts.insert(0, tail)

    return parts

#Splits a path into a list of its dirs, excluding the file at the end
def splitPathDirs(path):
    path = os.path.normpath(path)
    dirs = []
    
    while True:
        head, tail = os.path.split(path)
        ext = os.path.splitext(tail)[1]

		#Exclude file tail
        if (ext != ''):
          path = head
          continue

        if head == path:  # sentinel for absolute paths
            dirs.insert(0, head)
            break
        elif tail == path: # sentinel for relative paths, end of split
            dirs.insert(0, tail)
            break
        else:
            path = head
            dirs.insert(0, tail)

    return dirs


def valueInDicts(dictList, value):
	#Returns True if any key's value in any dict matches searchedValue
	isMatch = any((_dict[key] == value for key in _dict) for _dict in dictList)
	return isMatch

def valueInDictsKey(dictList, key, value):
	#Returns True if a specific key's value in any dict matches searchedValue
	isMatch = any(_dict[key] == value for _dict in dictList)
	return isMatch

def dictInDicts(dictList, searchDict):
	#Returns True if all keys in any dict match all keys in searchedDict
	isMatch = any(all(_dict[key] == searchDict[key] for key in searchDict) for _dict in dictList)
	return isMatch


def findDictsMatchingValue(dictList, value):
	#Returns dicts with ANY key's value matching searchedValue
	matchingDicts = [_dict for _dict in dictList if any(_dict[key] == value for key in _dict)]
	return matchingDicts

def findDictsMatchingKeyValue(dictList, key, value):
	#Returns dicts with A key's value matching searchedValue
	matchingDicts = [_dict for _dict in dictList if _dict[key] == value]
	return matchingDicts

def findDictsWithKeyValueInList(dictList, key, list):
	#Returns dicts with A key's value matching searchedValue
	matchingDicts = [_dict for _dict in dictList if _dict[key] in list]
	return matchingDicts

def findDictsMatchingDict(dictList, searchDict):
	#Returns dicts with all keys matching searchedDict keys
	matchingDicts = [_dict for _dict in dictList if all(_dict[key] == searchDict[key] for key in searchDict)]
	return matchingDicts