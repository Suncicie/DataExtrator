# encoding=utf-8
import re

import split_sentence
import select_keywords_sentence
import LCS
# get the answer from splited data by mode



def get_mode(FileName):
    file=open(FileName,mode="r+")
    lines=file.readlines()
    mode=[]
    i=0
    for line in lines:
        i+=1
        if i%2==0 :
            mode.append(line.decode("utf-8"))
    return mode

# constractor a re
def get_answer(ModeFile,SplitedData,ExtracData):
    mode_list=get_mode(ModeFile)
    pattern_list=[]
    for mode in mode_list:
        pattern_list.append(re.compile(mode))
    print "mode_list"
    print mode_list
    match_result=[]
# read the file and extract by re
    split_data=open(SplitedData,mode="r+")
    split_sentence=split_data.readlines()
    for line in split_sentence:
        line=line.decode("utf-8")
        for pattern in pattern_list:
            match=pattern.search(line)
            if match!=None:
                match_result.append(line)
            print "*"*30
            print line.encode("utf-8")
            print match


    extraData=open(ExtracData,mode="a+")
    for item in match_result:
        extraData.write(item.encode("utf-8"))
    extraData.close()
    return match_result