import os
from workPaths import workPaths

def validateFile(file):
	assert os.path.exists(file.dir), '{} dir not found:\n {}'.format(file.name, file.dir)

def validateWorkPaths():
	validateFile(workPaths.assetProject)