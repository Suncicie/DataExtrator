# encoding=utf8

#  give up

import LCS_add
import string


def LCS_Match(sentenceInfo):
    # print sentenceInfo
    commen_lcs=[]
    for word in sentenceInfo[0]["sen"]:
        pos_begin = []
        pos_after = []
        match = []
        print "word in sentence1 (%s) is %s  "%(sentenceInfo[0]["sen"],word)
        print "*"*40
        for sen in sentenceInfo[1:]:
            print "the compare sen is %s, and start word is %s"%(sen["sen"],sen["sen"][sen["pos"]])
            pos_begin.append(sen["pos"])  # 放入pos指针指向的字符
            temp=sen["pos"]
            while (word != sen["sen"][temp]):  # pos变为指向sen中与Word相同的字符
                if temp<sen["len"]-1: # len 为17 temp 最大只能是16
                    temp=temp+1#  最后不匹配时，指向的是最后匹配的后一个了
                elif temp==sen["len"]-1: # temp 为16时候,最后一个值，如果没匹配Word ，temp+1 匹配temp不变
                    if word != sen["sen"][temp]:
                        temp=temp+1
                        match.append(0)
                    break
            if temp!=sen["len"]: # 可以找到匹配 temp 是匹配了的词的位置
                 # 找到了匹配的时候 ，后面的查找全部从这个pos开始，如果没有找到匹配，pos还在原位置
                 if 0 not in match:
                     sen["pos"] = temp
                 match.append(1)
            # if sen["pos"]<sen["len"]-1: # sen["pos"]是要写入 sentenceInfo的，如果到了一个len 就结束了 ,没匹配的话应该就停在原处
                # sen["pos"]+=1           # 若len 17 pos最大为16 此处最大15
            elif sen["pos"]==sen["len"]-1: #若为最后一个,结束整个过程，返回结果
                return commen_lcs
            pos_after.append(sen["pos"])
        print pos_begin
        print pos_after
        print match

        if (0 in match):
            v=0
        else:
            v=1
        print "v is %s "%v
        if (v):
            print "append the word %s"%word
            commen_lcs.append(word)
        # lent = max(list(map(lambda x: x[0] - x[1], zip(pos_after, pos_begin))))
        # if lent >1:
        #     commen_lcs.append("_".decode("utf8"))
    print commen_lcs
    return commen_lcs




def lcs(FileName,OutputFileName):
    """
    >>> lcs(['666222054263314443712', '5432127413542377777', '6664664565464057425'])
    '54442'
    >>> lcs(['abacbdab', 'bdcaba', 'cbacaa'])
    'baa'
    """
    print "********************* start find substring *********************"

    f = open(FileName, mode="r+")
    lines = f.readlines()
    strings=[]
    for item in lines:
        # print item.decode("utf-8")
        strings.append(item.decode("utf-8"))

    # print strings
    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        return strings[0]
    else:
        sentenceInfo = []

        for i in range(len(strings)):
            leng = len(strings[i])
            pos = 0
            sen = strings[i]
            sentenceInfo.append({"len": leng, "pos": pos, "sen": sen})
        commen_sen=LCS_Match(sentenceInfo)
        print "commen_sen "+ "".join(commen_sen)
        result=LCS_add.add_(commen_sen, strings)
        newf = open(OutputFileName, mode="a+")
        newf.write(result.encode("utf-8"))
        newf.close()
        return LCS_add.add_(commen_sen,strings)

# lcs("dataset/splited_birthday.txt","dataset/flited_birthday.txt")