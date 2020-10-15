import initPaths
paths = initPaths.initGMS_utilities()

import workPaths
workPaths.initWorkPaths(paths)

from assetMaker import makeExtension
makeExtension()