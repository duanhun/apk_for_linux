# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

from bs4 import BeautifulSoup
import urllib2
import re
import httplib
jokeID=1
def buildsql(content):
    global jokeID
    id=jokeID
    jokeID=jokeID+1
    return "insert IGNORE into joke_list(jokeID,jokecontent) values('%s','%s');"%(id,content)
def main(url):
#print str(soup).decode("UTF-8").encode("GBK")
    page = urllib2.urlopen(url)
    html= page.read()
    soup=BeautifulSoup(html.decode("GBK"))
    p=soup.findAll(['p'])
    file_object = open('pagecontent_1.txt','a')
    sqls=''
#print str(p).decode("UTF-8").encode("GBK")
    for i in range(len(p)):
        p1=p[i]
        jokecontent=''
        if (len(p1.contents)>1)==True:
            """
            for j in range(len(p1.contents)):
                jokecontenttemp=""
                s1=p1.contents[j]
                jokecontenttemp=jokecontenttemp+str(s1)
                jokecontent=jokecontenttemp.decode("UTF-8")
                jokecontent=re.sub(u'[0-9]\u3001','',jokecontent)
                jokecontent=re.sub(u'<br />','',jokecontent)
            """
            jokecontent=re.sub(u'[0-9]\u3001','',str(p1).decode("UTF-8"))
            jokecontent=re.sub(u'<p>','',jokecontent)
            jokecontent=re.sub(u'</p>','',jokecontent)
            jokecontent=re.sub(u'<br[ /]*>','',jokecontent)
            #print jokecontent.encode("GBK")

        else:
            jokecontent=str(p1.contents[0]).decode("UTF-8")
            jokecontent=re.sub(u'[0-9]\u3001','',jokecontent)
            #print jokecontent.encode("GBK")
        #findall 返回列表
        if (re.findall(u'href',jokecontent)!=[]):
            continue
        jokecontent=buildsql(jokecontent)
        sqls=sqls+jokecontent
        print sqls
    try:
        file_object.writelines(sqls.encode("utf-8"))#多行输入
    finally:
        file_object.close()
        #p3=str(p2.contents[0]).decode("UTF-8")
        #print re.sub(u'[0-9]\u3001','',p3).encode("GBK")
def getsql(soup):
    p=soup.findAll(href=re.compile("/jokehtml/xy/[0-9]+.htm"))


    for i in range(len(p)):
        r=re.findall(r"/jokehtml/xy/[0-9]+.htm",str(p[i]))
        #print r[0]
        main("http://www.jokeji.cn"+r[0])

        #print str(p[0]).decode("utf-8").encode("GBK")
        """"


        """


def getcontent(index):

    while(index<=5):
        url="http://www.jokeji.cn/list5_"+str(index)+".htm"
        index=index+1

#url="http://www.jokeji.cn/jokehtml/xy/2015020318560570.htm"
#url="http://www.jokeji.cn/jokehtml/xy/2015010608341573.htm"

        page = urllib2.urlopen(url)
        html= page.read()
        soup=BeautifulSoup(html.decode("GBK"))

        getsql(soup)


index=1
getcontent(index)
print "END"