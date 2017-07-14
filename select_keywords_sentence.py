# encoding=utf8
# find the sentence include the key words

import re



def _judge_include_keywords(line,patternList):
    """
    :param line: the line from sentence
    :param patternList: keywords create it
    :return: wheather the line include the keywords in keywordlist
    """
    # print line
    line = (line).decode('utf8')

    result=1
    for pattern in patternList:
        # result=1
        match=pattern.search(line)
        # print "match"
        # print match
        if match==None:match=0
        else:match=1
        # print match
        result=result*match
    # print result
    # print result
    return result

def _find_keywords_sentence(FileName, OutputFileName,keywordlists):
    """
    :param FileName: the source of sentence
    :param OutputFileName: the file which consist of sentence including keyword in keywordlists
    :param keywordlists:
    :return:
    """
    print "********************* start fliter sentence *********************"

    f = open(FileName, mode="r+")
    lines = f.readlines()
    newf = open(OutputFileName, mode="w+")

    patternList=[]
    for keyword in keywordlists:
        # print "keyword %s"%keyword
        keyword = (keyword).decode('utf8')
        patternList.append(re.compile(keyword))
    lines=list(set(lines))
    for item in lines:
        if _judge_include_keywords(item,patternList):
            newf.writelines(item)
    newf.close()
    f.close()