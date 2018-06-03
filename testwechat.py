from autobysikulix.entity import checktaskjson
from autobysikulix.constant.errorcode import ERRORCODE_LIST

if __name__ == "__main__":
    nRet = checktaskjson.CheckJsonFile(r"F:\WeChatAutoBySikulix\task.json")
    if nRet:
        print (str(nRet) + ": " + str(ERRORCODE_LIST[nRet]))
    else:
        print("CheckJsonFile Sucess")
