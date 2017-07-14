#encoding=utf-8
import re




def cut_sentence(words):
    words = (words).decode('utf8') #如果是从编码为 utf8 的 txt 文本中直接输入的话，需要先把文本解码成 unicode 来处理
    start = 0
    i = 0  #记录每个字符的位置
    sents = []
    punt_list = ',，!?;~。！？；～=='.decode('utf8')  #string 必须要解码为 unicode 才能进行匹配
    for word in words:
        if word in punt_list:
            sents.append(words[start:i+1])
            start = i + 1  #start标记到下一句的开头
            i += 1
        elif word!='\n'.decode("utf8"):
                i += 1  #若不是标点符号，则字符位置继续前移
    if start < len(words):
        sents.append(words[start:])  #这是为了处理文本末尾没有标点符号的情况
    return sents
# def remove_changLine(text):


def _split_sentence(FileName ,OutputFileName):
    print "********************* start split sentence *********************"
    f=open(FileName, mode="r+")


    text = f.read()
    text= text.replace("\n","")
    # print text
    pattern = re.compile(r"\d{10,}")
    text=pattern.sub("。",text)
    newf = open(OutputFileName, mode="w+")

    # text=remove_changeLine(text_origin)
    line=cut_sentence(text)

    # print line
    for i in line:
        # i=i.encode("gb2312")
        # print i
        newf.write(i.encode("utf-8"))
        newf.write("\n")
    newf.close()
    f.close()

