import utilities as utils
from paths import workPaths
from os.path import exists
from os import mkdir
import shutil

def deleteResourceTypeFromProject(type, resources):
	for res in resources:
		yyJson = utils.readJson(res.file)
		parentPath = yyJson['parent']['path']
		assetPath = 'folders/' + type + '/' + workPaths.assetProject.name

		if assetPath in parentPath:
			shutil.rmtree(res.dir)

def deleteResourcesFromProject(project):
	deleteResourceTypeFromProject('Scripts', project.scripts)
	deleteResourceTypeFromProject('Objects', project.objects)
	deleteResourceTypeFromProject('Extensions', project.extensions)