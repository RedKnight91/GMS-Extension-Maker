import utilities as utils

def promptPushToAll():
	prompt = 'Push to all projects at once? (y/n)'
	updateAll = utils.promptChoice(prompt)
	return updateAll

def promptPushToProject(dir):
	prompt = 'Push to {} project? (y/n)'.format(dir)
	return utils.promptChoice(prompt)