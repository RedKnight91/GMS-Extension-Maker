from gmlExtensionMaker import makeExtension

extPaths = {}

extPaths['projectDirName']			= 'GMS_utilities'
extPaths['extensionProjectDirName']	= extPaths['projectDirName'] + '_extension'
extPaths['extensionName']			= extPaths['projectDirName']

extPaths['projectsDir']				= r'C:\Users\mikec\Documents\GameMakerStudio2'
extPaths['extensionsSubDir']		= r'__MY ASSETS'

makeExtension(extPaths)