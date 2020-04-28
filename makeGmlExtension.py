from gmlExtensionMaker import makeExtension

class Paths:
	pass

inputPaths = Paths()

inputPaths.sourceProjectName	= 'Tool'
inputPaths.extensionProjectName	= inputPaths.sourceProjectName + '_extension'
inputPaths.extensionName		= inputPaths.sourceProjectName

inputPaths.projectsDir			= r'C:\Users\mikec\Desktop\Fake Projects'
inputPaths.extensionsSubDir		= ''

inputPaths.externalResourcesGroup = 'External'
inputPaths.internalResourcesGroup = 'Internal'

# inputPaths.sourceProjectName	= 'GMS_utilities'
# inputPaths.extensionProjectName	= inputPaths.sourceProjectName + '_extension'
# inputPaths.extensionName		= inputPaths.sourceProjectName

# inputPaths.projectsDir			= 'C:/Users/mikec/Documents/GameMakerStudio2'
# inputPaths.extensionsSubDir		= '__MY ASSETS'

# inputPaths.externalResourcesGroup = 'External'
# inputPaths.internalResourcesGroup = 'Internal'

makeExtension(inputPaths)