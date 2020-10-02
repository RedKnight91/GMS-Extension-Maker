from gmlExtensionUpdater import projectUsesExtension
from jsonModels import extensionYYJSON
import utilities as utils
import os

def generateAssetExtension(workPaths):
	project = workPaths.sourceProject
	extName = workPaths.sourceProject.name

	extensionExists = projectUsesExtension(project, extName)

	if extensionExists:
		exit

	extDir = os.path.join(project.extensionsDir, extName)
	extFile = extName + '.yy'
	extPath = os.path.join(extDir, extFile)

	os.mkdir(extDir)
	extJson = extensionYYJSON(extName)
	utils.writeJson(extPath, extJson)