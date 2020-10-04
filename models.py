from os.path import basename
from utilities import getFileName

def folderJson(path, name):
	json = {
		"folderPath": path, #NOTE e.g. "folders/Scripts/Math.yy"
		"order": 0,
		"resourceVersion": "1.0",
		"name": name,
		"tags": [],
		"resourceType": "GMFolder"
	}
	return json

def resourceParentJson():
	json = {
		'name': 'Scripts',
		'path': 'folders/Scripts.yy',
	}
	return json

def resourceRelativePath(resourcesName, resourceName):
	path = resourcesName + '/' + resourceName + '/' + resourceName + '.yy'
	return path

def resourceJson(path):
	#NOTE Path should be resources/resName/resName.yy
	#e.g. extensions/Asset/Asset.yy

	json = {
		'id': {
			'name': getFileName(path, True),
			'path': path
		},
		'order': 0
	}

	return json

def extensionYYJSON(extensionName):
	extensionYY = {
		'optionsFile': 'options.json',
		'options': [],
		'exportToGame': True,
		'supportedTargets': -1,
		'extensionVersion': '0.0.1',
		'packageId': '',
		'productId': '',
		'author': '',
		'date': '2020-10-02T11:34:28.7561714+02:00',
		'license': '',
		'description': '',
		'helpfile': '',
		'iosProps': False,
		'tvosProps': False,
		'androidProps': False,
		'installdir': '',
		'files': [],
		'classname': '',
		'tvosclassname': None,
		'tvosdelegatename': None,
		'iosdelegatename': '',
		'androidclassname': '',
		'sourcedir': '',
		'androidsourcedir': '',
		'macsourcedir': '',
		'maccompilerflags': '',
		'tvosmaccompilerflags': '',
		'maclinkerflags': '',
		'tvosmaclinkerflags': '',
		'iosplistinject': None,
		'tvosplistinject': None,
		'androidinject': None,
		'androidmanifestinject': None,
		'androidactivityinject': None,
		'gradleinject': None,
		'iosSystemFrameworkEntries': [],
		'tvosSystemFrameworkEntries': [],
		'iosThirdPartyFrameworkEntries': [],
		'tvosThirdPartyFrameworkEntries': [],
		'IncludedResources': [],
		'androidPermissions': [],
		'copyToTargets': -1,
		'parent': {
			'name': 'Extensions',
			'path': 'folders/Extensions.yy',
		},
		'resourceVersion': '1.0',
		'name': extensionName,
		'tags': [],
		'resourceType': 'GMExtension',
	}

	return extensionYY