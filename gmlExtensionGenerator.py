from gmlExtensionUpdater import projectUsesExtension
from models import extensionYYJSON
import utilities as utils
import os
from gmsUtilities import includeResourcesToYyp

def generateAssetExtension(workPaths):
	project = workPaths.assetProject
	extName = workPaths.assetProject.name

	extensionExists = projectUsesExtension(project.dir, extName)

	if extensionExists:
		return

	extDir = os.path.join(project.extensionsDir, extName)
	extFile = extName + '.yy'
	extPath = os.path.join(extDir, extFile)

	os.makedirs(extDir, exist_ok=True)
	extJson = extensionYYJSON(extName)
	utils.writeJson(extPath, extJson)

	includeResourcesToYyp('extensions', [extName], project.file)