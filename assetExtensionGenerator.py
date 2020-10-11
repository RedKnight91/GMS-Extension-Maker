from assetProjectFinder import projectUsesAsset
from models import extensionYYJSON
import utilities as utils
import os
from gmUtilities import includeResourceTypeToProject
from paths import workPaths
from classes import File

def generateAssetExtension():
	project = workPaths.assetProject
	name = workPaths.assetProject.name

	extensionExists = projectUsesAsset(project.dir, name)

	if extensionExists:
		return

	dir = os.path.join(project.extensionsDir, name)
	extension = File(name, dir, '.yy')

	os.makedirs(dir, exist_ok=True)
	extJson = extensionYYJSON(name)
	utils.writeJson(extension.file, extJson)
	
	includeResourceTypeToProject('extensions', [extension], project.file)