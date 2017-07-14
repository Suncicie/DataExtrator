# encoding="utf8"
import extrator_re
import split_sentence
import select_keywords_sentence

dataroot="dataset/test"

# set the theme
seacher_word="tencentMa1998"
theme="built"

OriginData="%s/%s_origin.txt"%(dataroot,seacher_word)
SplitedData="%s/%s_split.txt"%(dataroot,seacher_word)
ModeFile="%s/%s_mode.txt"%(dataroot,theme)
ExtracData="%s/%s_extra_result.txt"%(dataroot,seacher_word)

split_sentence._split_sentence(OriginData,SplitedData)

print extrator_re.get_answer(ModeFile,SplitedData,ExtracData)