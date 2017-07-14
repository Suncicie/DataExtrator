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
from bs4 import  BeautifulSoup as bs

from pyquery import  PyQuery as pq

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
        urllist = content.xpath('//h3[@class="t"]/a/@href')
        urlbiglist.append(urllist)
        print  urlbiglist
        print  len(urlbiglist)
    print "循环结束"
     #获得url成功

#用已得到的url 去爬取界面  然后解析界面，获得文本数据
def parsehtml(file,urlbiglist):
    #开始处理url
    #准备好正则表达式

    rules = ur"([\u0030-\u0039\u4e00-\u9fff\u3002\uFF1F\uFF01\uFF0C\u3001\uFF1B\uFF1A\u300A\u300B\u3008\u3009\u2018\u2019\u201C\u201C\uFF08\uFF08\u3010\u3011]+)"
    pattern = re.compile(rules)

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
            # language = ['Chinese','']
            # print char_type['language']
            # print char_type['language'] in language
            #
            # if not ( char_type['language'] in language):
            #     print char_type['language']
            #     print char_type['language'] in language
            #     continue
            if(char_type["encoding"]=='GB2312'):
                try:
                     html = html.decode('gbk').encode('utf-8')
                except UnicodeDecodeError,e:
                    print "编码有些问题，已跳过"
                    continue
            else:
                html = unicode(html, char_type["encoding"]).encode("utf-8")
            # pagecontent = etree.HTML(html,parser=etree.HTMLParser(encoding='utf-8'))
            file.write('\n这是一篇:\n')
            #全部的中文信息，没有空格和空行  （也没有标点符号）
            source= html.decode('utf-8')
            results = pattern.findall(source)   #只是一个个列表
            for result in results:
               file.write(result)




    file.close()
    print '解析结束'

if __name__=="__main__":
    print "开始"
    #输入关键词
    keyword = '腾讯 马化腾 1998'
    file = open("%s.txt" % (keyword), 'w')
    #输入要抓取的篇章数
    geturl(keyword,10)
    parsehtml(file,urlbiglist)

