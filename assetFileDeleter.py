import utilities as utils
from workPaths import workPaths
from os.path import exists
from os import mkdir
import shutil

def deletableResource(res, assetPath):
	yyJson = utils.readJson(res.file)
	parentPath = yyJson['parent']['path']

	deletable = assetPath in parentPath
	return deletable

def deleteResourceTypeFromProject(type, resources):
	assetName = workPaths.assetProject.name
	assetPath = 'folders/{}/{}'.format(type, assetName)
	deletees = [res for res in resources if deletableResource(res, assetPath)]

	if not deletees:
		return

	utils.printList([res.name for res in deletees])
	confirm = utils.promptChoice('Delete {}? [y/n]'.format(type))
	if confirm:
		for res in deletees:
			shutil.rmtree(res.dir)

def deleteResourcesFromProject(project):
	deleteResourceTypeFromProject('Scripts', project.scripts)
	deleteResourceTypeFromProject('Objects', project.objects)
	deleteResourceTypeFromProject('Extensions', project.extensions)