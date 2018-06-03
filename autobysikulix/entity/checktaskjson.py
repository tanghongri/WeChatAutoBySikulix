import json
from constant.errorcode import ERRORCODE_LIST

def CheckJsonFile(filepah):
    return 0


if __name__ == "__main__":
    nRet = CheckJsonFile(r"F:\WeChatAutoBySikulix\task.json")
    if not nRet:
        print (str(nRet))
