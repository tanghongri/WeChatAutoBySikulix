import json
import os
from autobysikulix.constant import errorcode


def CheckJsonFile(filepah):
    if not os.path.exists(filepah):
        return 1
    taskjson = None
    with open(filepah, 'r') as fjson:
        try:
            taskjson = json.load(fjson)
        except:
            return 2
    if not taskjson:
        return 3
    return 0
