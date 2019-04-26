import re

class REoperation:
    '''
    查找匹配值isMatch
    获取全部匹配的结果getAllMatch
    获取第一个结果getOneResult
    '''
    def __init__(self,expr,string):
        self.expr=expr
        self.string=string
        re.compile(expr)

    def isMatch(self):
        try:
            result=re.search(self.expr, self.string)
            print(result)
            if result.group(0):
                return True
            return False
        except AttributeError:
            pass

    def getAllResult(self):
        return re.findall(self.expr,self.string)

    def getOneResult(self,index):
        ret=""
        try:
            result=re.search(self.expr,self.string)
            ret=result.group(index)
        except IndexError:
            pass
        finally:
            return ret

if __name__=='__main__':

    pa='([0-9]+).*([0-9]+)'
    s='asd34345bd4534kisjdi'
    # r=REoperation(pa,s)
    # print(r.getAllResult())
    # print(r.getOneMatch(2))

    print(re.findall(pa,s))
    print(re.split(pa,s))

    #
    # def match()
    # result=re.search(pa,s)
    # try:
    #     i=0
    #     while result.group(i):
    #         print(result.group(i))
    #         i=i+1
    # except IndexError:
    #     pass





