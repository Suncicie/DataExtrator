# encoding=utf8
import LCS_add
import re

def calc_cache_pos(strings, indexes):
    """
    :param strings: list of sentence
    :param indexes: list of sentence's length
    :return:
    """
    factor = 1
    pos = 0
    for s, i in zip(strings, indexes): # 对于每一个句子 pos为 累加 指针index与factor乘积的  factor是
        pos += i * factor       # indexes 不一定是sentence长度了，相当于指针在从后往前移动， i指着的指针 乘 factor
        factor *= len(s)       #  factor 更新为句子长度 index1 * 1 + index2 * len(s1) + index3 * len(s2)
                               # 将三维映射进一维，可看成此时的 sentence 的 index1i 的字符的位置
    return pos

def lcs_back(strings, indexes, cache):
    """
    :param strings:
    :param indexes:
    :param cache:
    :return:
    """
    if -1 in indexes:
        return ""

    match = all(strings[0][indexes[0]] == s[i]        # strings is a list s[i][j]表示第i个词的第j个字
                for s, i in zip(strings, indexes))            # 如果都匹配的话 如果所有字符穿的最后一个字都与第一个字符串的的最后一个字匹配
    if match:
        new_indexes = [i - 1 for i in indexes]
        result = lcs_back(strings, new_indexes, cache) + strings[0][indexes[0]]       # 则递归调用
        # print "222222222222222222222222222222222"
        # print strings[0][indexes[0]]
    else:

        substrings = [""] * len(strings)               #否则  substring 存三个字符串
        for n in range(len(strings)):                                                     #对于每一个字符串
            if indexes[n] > 0:                                                        # 如果字符串长度大于0
                new_indexes = indexes[:]
                new_indexes[n] -= 1                                                             #将该字符串的长度值-1
                cache_pos = calc_cache_pos(strings, new_indexes) # 计算出该字符在cache中的位置
                if cache[cache_pos] is None:
                    substrings[n] = lcs_back(strings, new_indexes, cache) # 如果这个位置为空，则进行递归计算下一层
                else:
                    substrings[n] = cache[cache_pos]  # 如果不为空，这把这个字符放进substrings 中的第n个句子
                    # print "----------------"
                    # print cache[cache_pos]
                    # substrings[n]=substrings[n]+"_"
                    # print substrings[n]
        # print substrings

        result = max(substrings, key=len)     # 上面一块计算完毕后， 将最大子串给result
        # print "------------------"
        # for item in substrings:
        #     print item
        #     print "max"
        #     print max(substrings, key=len)
    cache[calc_cache_pos(strings, indexes)] = result # 将算得的最大子串，放进cache中此时的词的最后的位置
    # print result
    return result

def genaralization(result,KeyWordLists):
    result=result.replace("_",".*")
    # result=result.decode()
    print result
    print KeyWordLists
    for word in KeyWordLists:
        print word
        print result
        word=word.decode("utf8")
        pattern=re.compile(word)
        temp=pattern.search(result)
        pos=temp.start()
        if result[pos-1]=="*":
            result=result.replace(word,"")
        else:result=result.replace(word,".*")
    return result




def lcs(FileName,OutputFileName,KeyWordLists):
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
    newf = open(OutputFileName, mode="a+")
    # print strings
    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        newf.write(strings[0].encode("utf-8"))
        newf.close()
        return strings[0]
    else:
        cache_size = 1
        for s in strings:
            cache_size *= len(s)#  cache 是所以句子的长度的乘积
        cache = [None] * (cache_size+1) # each word length
        indexes = [len(s) - 1 for s in strings] # 每个句子 的长度 作为index 的值

        # print "result"
        # print lcs_back(strings, indexes, cache)

        # return lcs_back(strings, indexes, cache)
        commen_sen=lcs_back(strings, indexes, cache)
        # print commen_sen.decode("utf-8")
        # return commen_sen
        print "commen_sen："
        print commen_sen
        result=LCS_add.add_(commen_sen, strings)
        rule_result=genaralization(result,KeyWordLists)
        # newf.writelines(question)
        # newf.writelines("\n".encode("utf8"))

        newf.write(result.encode("utf-8"))
        newf.write(rule_result.encode("utf-8"))
        newf.close()
        return LCS_add.add_(commen_sen,strings)