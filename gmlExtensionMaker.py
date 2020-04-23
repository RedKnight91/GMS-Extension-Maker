from gmlExtensionPathMaker import concatenateExtensionPaths
from gmlExtensionScriptCombiner import combineGmlScripts
from gmlExtensionFileCopier import copyCombinedFilesToExtensionDir
from gmlExtensionFunctionFileIncluder import includeFunctionFilesToExtension
from gmlExtensionFunctionJsonMaker import populateExtensionFunctionJson
from gmlExtensionJsdocInjector import injectExtensionJsdocs
from gmlExtensionUpdater import pushExtension
import utilityScripts as utils

def printHeader(extPaths):
	extensionName = extPaths['extensionName']
	extensionProjectDirName = extPaths['extensionProjectDirName']
	projectDirName = extPaths['projectDirName']
	print('Making extension "{}" in project {}, combining project {}'.format(extensionName, extensionProjectDirName, projectDirName))


def makeExtension(extPaths):
	printHeader(extPaths)

	concatenateExtensionPaths(extPaths)
	combineGmlScripts(extPaths)
	copyCombinedFilesToExtensionDir(extPaths)
	includeFunctionFilesToExtension(extPaths)
	populateExtensionFunctionJson(extPaths)
	injectExtensionJsdocs(extPaths)
	pushExtension(extPaths)