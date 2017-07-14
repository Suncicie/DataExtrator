# encoding=utf-8
def add_(lcs,sentenceLists):
    # print sentenceLists
    sentenceInfo=[]

    for i in range(len(sentenceLists)):
        leng=len(sentenceLists[i])
        pos=0
        sen=sentenceLists[i]
        sentenceInfo.append({"len":leng ,"pos":pos ,"sen":sen})
        # print sentenceInfo


    def NoMatch(sentenceInfo,word):
        # print sentenceInfo

        pos_begin=[]
        pos_after=[]
        for sen in sentenceInfo:
            # print "item "
            # print sen
            pos_begin.append(sen["pos"]) # 放入pos指针指向的字符
            # print "sen "+sen["sen"]
            # print "pos "+ str(sen["pos"])
            # print "len"+str(len(sen["sen"]))
            # print sen["sen"][sen["pos"]]

            while(word!=sen["sen"][sen["pos"]]): # pos变为指向sen中与Word相同的字符
                # print "word "+word
                # print "pos "+ str(sen["pos"])
                # print  "word in sen "+sen["sen"][sen["pos"]]
                # if sen["pos"]<sen["len"]-1:
                sen["pos"]+=1
                # else:
                #     sen["pos"]+=1
                #     break
            # if sen["pos"]<sen["len"]-1:
            #     sen["pos"]+=1
            pos_after.append(sen["pos"])
        # print "word:"
        # print word
        # print "pos_begin:"
        # print pos_begin
        # print "pos_after:"
        # print pos_after
        # print "*"*30
        v = max(list(map(lambda x: x[0] - x[1], zip(pos_after, pos_begin))))
        if v>2:
            return 1
        else:return 0

    result=[]
    for i in lcs:
        # print i
        if(NoMatch(sentenceInfo,i)): # 判断这个字符在 这几个句子中 和下一个字符在这几句子中的 位置 是否连续
            # print "matcn result:"
           # print NoMatch(sentenceInfo,i)
            result.append("_".decode("utf-8"))
        result.append(i)
    result=("").join(result)
    return result



# senlist1=["深圳市腾讯计算机系统有限公司成立于1998年11月  ，","腾讯计算机系统有限公司成立于1998年11月。","腾讯公司于1998年11月在深圳成立，","市腾讯公司成立于1998年11月。","深圳市腾讯计算机系统有限公司成立于1998年11月，"]
# senlist=[]
# for i in senlist1:
#     senlist.append(i.decode("utf-8"))
# print senlist
#
# print add_("腾讯公司于1998年11月".decode("utf8"),senlist)