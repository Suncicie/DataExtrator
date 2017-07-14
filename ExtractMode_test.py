# encoding=utf-8
import split_sentence
import select_keywords_sentence
import LCS
# import lcs_2

dataroot="dataset/test"
seacher_word="tencentMa1998"
question="built"

OriginData="%s/%s_origin.txt"%(dataroot,seacher_word)
SplitedData="%s/%s_split.txt"%(dataroot,seacher_word)
FliteredData="%s/%s_fliter.txt"%(dataroot,seacher_word)
ModeData="%s/%s_mode.txt"%(dataroot,question)

#句子中要过滤的词
KeyWords=["腾讯","马化腾","1998"]
# 要泛化的词
genKeyWords=["腾讯","马化腾","1998"]
# genKeyWord 要包含于 KeyWords

# question="公司，组织成立时间"


split_sentence._split_sentence(OriginData,SplitedData)

# test select keywords in sentence
select_keywords_sentence._find_keywords_sentence(SplitedData,FliteredData,KeyWords)
print LCS.lcs(FliteredData,ModeData,genKeyWords)