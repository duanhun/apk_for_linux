# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import re
import time
import traceback
import requests
from bs4 import BeautifulSoup

class DuZheBaoJokeSpider(object):
    _host = "http://www.duzhebao.com/xiaohua/"
    _type = ""
    _compile = "/xiaohua/"
    _joke_type_dict = {}

    def __init__(self, jokeType):
        self.get_types()
        self._type = jokeType

    @classmethod
    def get_types(cls):
        """
        获取笑话类型
        :return:
        """
        url = cls._host + cls._type
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        for liTag in soup.find_all("a", href=re.compile(cls._compile + "[^\d.+]")):
            key = liTag.attrs.get("href").replace(cls._compile,"").replace("/", "")
            value = liTag.string.replace(u"\u7b11\u8bdd","") # u"\u7b11\u8bdd" = u"笑话"
            if key is not None and value is not None:
                cls._joke_type_dict[key] = value
        return cls._joke_type_dict

    @classmethod
    def pull_jokes_by_type(cls, jokeType):
        """
        根据类型拉取笑话
        :param jokeType: 
        :return:
        """
        url = originUrl = cls._host + "/" + jokeType + "/"
        isStop = True
        pageIndex = 1
        sql_text_list = []
        print "jokeType", jokeType
        while(isStop):
            try:
                print pageIndex
                response = requests.get(url)
                soup = BeautifulSoup(response.text)
                for preTag in soup.find_all("pre"):
                    text = (preTag.string if preTag.string else "").replace("\r","").replace("\n","")
                    sql = """INSERT INTO joke(joke_type, joke_type_text, joke_text, joke_origin) values("%s", "%s",  "%s", "%s");""" \
                          % (jokeType.encode("utf8"), cls._joke_type_dict[jokeType].encode("utf8"), text.encode("utf8"), "duzhebao")
                    sql_text_list.append(str(sql))
                    sql_text_list.append("\n")
                with open("joke.sql", "a") as f:
                    f.writelines(sql_text_list)
                if not sql_text_list:
                    isStop = False
                sql_text_list = []
                pageIndex += 1
                url = originUrl + str(pageIndex) + ".htm"

            except Exception as e:
                isStop = False
                raise

    @classmethod
    def create_sql(cls):
        jokeTypes = cls.get_types().keys()
        print "jokeTypes", jokeTypes
        for jokeType in jokeTypes:
            cls.pull_jokes_by_type(jokeType)



class XiaoHuaJiSpider(object):
    _host = "http://www.jokeji.cn"
    _encoding = "gbk"
    _joke_type_dict = {}

    def __init__(self):
        self.get_types()

    def get_types(self):
        """

        :return: dict
        """
        _typeUrl = self._host + "/Keyword.htm"
        response = requests.get(_typeUrl)
        response.encoding = self._encoding # 设置requests的编码

        soup = BeautifulSoup(response.text)
        tdListTag = soup.find_all("table", id="classlist")
        aSoup = tdListTag[0]
        aList = aSoup.find_all("a")
        for aTag in aList:
            key = aTag['href'].replace("\r\n", "")
            value = re.sub(r"\(.+", "", aTag.string).replace("\r\n", "")
            self._joke_type_dict[key] = value
        return self._joke_type_dict

    def pull_jokes_by_type(self, _type):
        for i in range(1, 1000):
            try:
                _type = re.sub(r"_\d+.", "_"+ str(i)+".", _type)
                listUrl = self._host + _type
                print "listUrl:", listUrl
                response = requests.get(listUrl)
                response.encoding = self._encoding
                soup = BeautifulSoup(response.text)
                divTag = soup.find_all("div", class_="list_title")
                ulTag = divTag[0]
                # index = 0
                for aTag in ulTag.find_all("a"):
                    sqlText = self._get_jokes_in_one_page(_type,aTag["href"])
                    with open("xiaohuaji.sql", "a") as f:
                        f.write(sqlText)
                    # index += 1
            except Exception as e:
                print "error:",e, traceback.format_exc()
                break

    def _get_jokes_in_one_page(self, jokeType, path):
        sqlList = []
        pageUrl = self._host + path
        response = requests.get(pageUrl)
        response.encoding = self._encoding
        soup = BeautifulSoup(response.text)
        pTags = soup.find_all("p")
        for pTag in pTags:
            if pTag.find("a") is not None:
                continue
            text = re.sub(r"(\d+\u3001|\d+.)*(@.+)*", "", pTag.text)
            # text = pTag.text
            sql = """INSERT INTO joke(joke_type, joke_type_text, joke_text, joke_origin) values("%s", "%s",  "%s", "%s");"""\
                  % (jokeType.encode("utf8"), self._joke_type_dict[re.sub(r"_\d+.", "_1.", jokeType.encode("utf8"))].encode("utf8"), text.encode("utf8"), "xiaohuaji")
            print sql
            sqlList.append(sql)
        return "\n".join(sqlList)


    def create_sql(self):
        jokeTypes = self.get_types().keys()
        print "jokeTypes", jokeTypes
        # self.pull_jokes_by_type("/list29_1.htm")
        escapeType = ["/list41_1.htm", "/list19_1.htm", "/list31_1.htm", "/list28_1.htm", "/list32_1.htm",
                      "/list14_1.htm", ]
        for jokeType in jokeTypes:
            if jokeType in escapeType:
                print "escape"
                continue
            self.pull_jokes_by_type(jokeType)


class PengFuSpider(object):
    _host = "http://www.pengfu.com/"
    _type = ""
    _compile = "/xiaohua/"
    _joke_type_dict = {}


    @classmethod
    def get_types(cls):
        """
        获取笑话类型
        :return:
        """
        url = cls._host + cls._type
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        for liTag in soup.find_all("a", href=re.compile(cls._compile + "[^\d.+]")):
            key = liTag.attrs.get("href").replace(cls._compile,"").replace("/", "")
            value = liTag.string.replace(u"\u7b11\u8bdd","") # u"\u7b11\u8bdd" = u"笑话"
            if key is not None and value is not None:
                cls._joke_type_dict[key] = value
        return cls._joke_type_dict

    @classmethod
    def pull_jokes_by_type(cls, jokeType):
        """
        根据类型拉取笑话
        :param jokeType:
        :return:
        """
        url = originUrl = cls._host + "/" + jokeType + "/"
        isStop = True
        pageIndex = 1
        sql_text_list = []
        print "jokeType", jokeType
        while(isStop):
            try:
                print pageIndex
                response = requests.get(url)
                soup = BeautifulSoup(response.text)
                for preTag in soup.find_all("pre"):
                    text = (preTag.string if preTag.string else "").replace("\r","").replace("\n","")
                    sql = """INSERT INTO joke(joke_type, joke_type_text, joke_text, joke_origin) values("%s", "%s",  "%s", "%s");""" \
                          % (jokeType.encode("utf8"), cls._joke_type_dict[jokeType].encode("utf8"), text.encode("utf8"), "duzhebao")
                    sql_text_list.append(str(sql))
                    sql_text_list.append("\n")
                with open("joke.sql", "a") as f:
                    f.writelines(sql_text_list)
                if not sql_text_list:
                    isStop = False
                sql_text_list = []
                pageIndex += 1
                url = originUrl + str(pageIndex) + ".htm"

            except Exception as e:
                isStop = False
                raise

    @classmethod
    def create_sql(cls):
        jokeTypes = cls.get_types().keys()
        print "jokeTypes", jokeTypes
        for jokeType in jokeTypes:
            cls.pull_jokes_by_type(jokeType)

if __name__ == "__main__":
    # jSpider = DuZheBaoJokeSpider("")
    # jSpider.create_sql()
    # jSpider.pull_jokes_by_type("lengxiaohua")
    x=XiaoHuaJiSpider()
    x.create_sql()
    pass
