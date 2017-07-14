# encoding= utf-8
import SuffixTree
from SuffixTree import SubstringDict

sd=SubstringDict()
sd.__setitem__("我是python程序员",1)
sd.__setitem__("我是ruby程序员",2)
sd.__setitem__("我是javascript程序员",3)
sd.__setitem__("我是android程序员",4)
sd.__setitem__("我还是DBA",4)
# sd._addToTree("我还是算法工程师")

SuffixTree._testWithDictWords()


print sd["我是"]
print sd["我还是"]