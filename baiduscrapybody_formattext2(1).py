#encoding:utf-8
import  urllib
import  urllib2
from lxml import  etree
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import chardet
import  gzip
import  re

#http://finance.ifeng.com/news/2010/lizehou/
#http://www.sbkk88.com/mingzhu/zhongguoxiandaiwenxuemingzhu/tanmei/
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
urlbiglist = []  # 将所有的url放进

#重新构建url,加入参数（页数）  要循环的（退出的条件是找不到下一页）
#h获得的url添加到list中，且顺序保持不变
def geturl(keyword,number):

    for i in range(number/10):
        url = "http://www.baidu.com/s?wd=%s&pn=%d0"%(urllib.quote(keyword),i)
        request = urllib2.Request(url = url,headers=headers)
        print request
        response = urllib2.urlopen(request)
        html = response.read()
        content = etree.HTML(html,parser=etree.HTMLParser(encoding='utf-8'))

        nextpage = content.xpath('//div[@id="page"]/a[last()][@class="n"]')
        if(not len(nextpage)):
        #     #若没有下一页(不满足条件) 跳出循环  不然就继续爬取
            break
        urllist = content.xpath('//h3[@class="t"]/a/@href')  #获得所有的url 每一页抽取url,组成一个list
        urlbiglist.append(urllist)
        print  urlbiglist
        print  len(urlbiglist)
    print "循环结束"
     #获得url成功

#用已得到的url 去爬取界面  然后解析界面，获得文本数据
def parsehtml(file,urlbiglist):
    #开始处理url
    for i in range(len(urlbiglist)):
        for j in range(len(urlbiglist[i])):
            # print urlbiglist[i][j]
            for k in range(3):
                try:
                   request = urllib2.Request(url = urlbiglist[i][j],headers=headers)
                   html = urllib2.urlopen(request).read()
                   print "连接成功，跳出循环"
                   break

                except urllib2.HTTPError,e:
                    print "有问题，再连一遍"
                    continue
            #编码问题解决
            char_type = chardet.detect(html)
            print (char_type)
            #再对编码进行一次判断  只要中文字符的网页 若超出范围直接跳出
            language = ['Chinese','']
            print char_type['language']
            print char_type['language'] in language

            if not ( char_type['language'] in language):
                print char_type['language']
                print char_type['language'] in language
                continue
            if(char_type["encoding"]=='GB2312'):
                try:
                     html = html.decode('gbk').encode('utf-8')
                except UnicodeDecodeError,e:
                    print "编码有些问题，已跳过"
                    continue
            else:
                html = unicode(html, char_type["encoding"]).encode("utf-8")
            pagecontent = etree.HTML(html,parser=etree.HTMLParser(encoding='utf-8'))

            #因为每个界面的网页结构不同  所以要查找多种形式

            # 第一种找法  搞一个大的字符串（其中包括空格和空行）
            filecontent = ''
            p1 = pagecontent.xpath('//div[@class="main-content"]')
            print  type(p1)
            print p1
            print ("第一次找")
            for i in range(len(p1)):
                filecontent = filecontent + p1[i].xpath('string()')
            # 去空格  去空行
            filestringcontent = ''
            file.write('\n这是一篇:\n')
            for line in filecontent.splitlines():
                if not line.split():
                    continue
                line = line.strip()#去空格    也是去掉了换行符
                filestringcontent += line
            file.write(filestringcontent)

            # 每一个网页抓完后的标志

            if(len(p1)):
                continue
            print "第二次找"
            p2 = pagecontent.xpath('//body//div//p//text()')

            print p2
            for l in range(len(p2)):
                print '打印每一页的内容====='
                print p2[l]
                print type(p2[l])
                file.write(p2[l])

                #对每一个p标签下的文本  做处理   也让其成为一个大的一行字符串
    file.close()
    print '解析结束'

def demo1():
    request = urllib2.Request("http://finance.ifeng.com/news/2010/lizehou/")
    html = urllib2.urlopen(request).read()

    # 编码问题解决
    char_type = chardet.detect(html)
    print (char_type)
    # 再对编码进行一次判断  只要中文字符的网页 若超出范围直接跳出
    language = ['Chinese', '']
    print char_type['language']
    print char_type['language'] in language

    if not (char_type['language'] in language):
        print char_type['language']
        print char_type['language'] in language

    if (char_type["encoding"] == 'GB2312'):
        try:
            html = html.decode('gbk').encode('utf-8')
        except UnicodeDecodeError, e:
            print "编码有些问题，已跳过"

    else:
        html = unicode(html, char_type["encoding"]).encode("utf-8")

    pagecontent = etree.HTML(html,parser=etree.HTMLParser(encoding='utf-8'))
    #对页面进行解析
    p = pagecontent.xpath('//body//div//p//text()')
    print type(p)
    print p
    # filecontent = ''
    for i in range(len(p)):
        print  p[i]
        print type(p[i])
        file.write(p[i])
        # filecontent = filecontent+p[i].xpath('string()')
    #去空格
    # filestringcontent = ''
    # for line in filecontent.splitlines():
    #     if not line.split():
    #         continue
    #     line = line.rstrip()+"\n"
    #     filestringcontent+=line
    # #写入文件
    #     file.write(filestringcontent)
        # file.writelines(p[i])

def textformat(filepath1):
    content = ''
    file = open(filepath1,'r')
    for line in file.readlines():
        content+=line
    bigString = ''
    for line in content.splitlines():
        if(not len(line)):
            continue
        line = line.strip()+'\n'
        bigString+=line
    file.close()

    print type(bigString)
    print  bigString

    file2 = open(filepath1,'w')
    file2.writelines(bigString)
    file2.close()



if __name__=="__main__":
    print "开始"
    #输入关键词
    keyword = '网易 成立时间'
    file = open("%s.txt" % (keyword), 'w')
    #输入要抓取的篇章数
    geturl(keyword,50)
    parsehtml(file,urlbiglist)
    # demo1()
    #/ Users / lx / PycharmProjects / ltp / 朱光潜.txt
    filepath1 = '/Users/Suncicie/Project/DataExtracor/%s.txt'%(keyword)
    # filepath2 = '/Users/lx/PycharmProjects/ltp/%s2.txt'%(keyword)
    textformat(filepath1)

