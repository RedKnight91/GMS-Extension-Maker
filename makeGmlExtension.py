import initPaths
paths = initPaths.initTest()

import workPaths
workPaths.initWorkPaths(paths)

from assetMaker import makeExtension
makeExtension()