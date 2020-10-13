from assetPathValidator import validateWorkPaths
from assetExtensionGenerator import generateAssetExtension
from assetProjectFinder import listProjectsUsingAsset
from assetPromptPush import promptPushToAll, promptPushToProject
from assetFileDeleter import deleteResourcesFromProject
from assetFileCopier import copyResourcesToProject
from assetResourceIncluder import includeAssetResourcesToProject
from assetResourceExcluder import excludeAssetResourcesFromProject

import utilities as utils
import os

def makeExtension():
	validateWorkPaths()
	
	generateAssetExtension()

	userProjects = listProjectsUsingAsset()

	updateAll = promptPushToAll()
	for project in userProjects:
		if (updateAll or promptPushToProject(project)):
			deleteResourcesFromProject(project)
			excludeAssetResourcesFromProject(project)
			copyResourcesToProject(project)
			includeAssetResourcesToProject(project)