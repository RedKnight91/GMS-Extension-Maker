import os
import json

projectDir = r'C:\Users\mikec\Documents\Github\bitblock_blast'


def validFile(filePath, extension):
	valid = filePath.endswith(extension)
	return valid

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

def getProjectResourceList():
	resources = []
	files = getDirectoryFiles(projectDir)
	yypPath = getMatchingFile(files, '.yyp')

	print (yypPath)

	with open(yypPath, 'r') as yypFile:
		yypJson = json.load(yypFile)
		resources = yypJson['resources']

	return resources

def validateResource(resource):
	output = ''
	
	if ('Key' not in resource):
		return 'Resource missing key'

	key = resource['Key']

	if ('Value' not in resource):
		return 'Resource ' + key + 'missing "Value" key'
	
	value = resource['Value']

	if ('id' not in value):
		missingID = ('Resource ' + key + 'missing "id" key')
		output = '\n'.join([output, missingID])


	if ('resourcePath' not in value):
		missingPath = ('Resource ' + key + 'missing "resourcePath" key')
		output = '\n'.join([output, missingPath])

	if ('resourceType' not in value):
		missingType = ('Resource ' + key + 'missing "resourceType" key')
		output = '\n'.join([output, missingType])

	return output
	
	

def validateYyp():
	resList = getProjectResourceList()
	resN = len(resList)

	print('\n CHECKING RESOURCES: \n')

	for i, res in enumerate(resList):
		print(str(i) + '/' + str(resN))
		print(validateResource(res))

	print('\n ALL RESOURCES CHECKED \n')

	return





validateYyp()