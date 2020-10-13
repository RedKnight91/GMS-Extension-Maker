from classes import WorkPaths

workPaths = ''

def initWorkPaths(paths):
	global workPaths #This lets the function know we're referencing the module-level variable workPaths
	workPaths = WorkPaths(
		paths['projectsDir'],
		paths['assetProjectDir']
	)