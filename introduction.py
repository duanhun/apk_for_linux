#!/bash/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'Jeffrey'

import random
import time

def doing(activity, use_time):
    print activity , int(use_time) * 5 + 1, "minutes"

class PythonProgrammer(object):
    real_English_name = "Jeffrey Chu"
    nick_name = "魔术师Jeffrey Chu"
    occupation = "Server development engineer"
    hobbies = ["魔术", "美食", "编程", "诗词", "音乐", "摄影", "游戏"]
    blog_url = "http://zhujinhui.net/"
    _relaxing = ("relax","1")


    def working(self):
        activities = ["writing implements", "writing blog", "studying", "fixing bug", "writing SQL", "talking with PM"]
        index = 0
        while index<10:
            use_time = random.randint(0,10) # seconds
            activity_type = random.randint(0, len(activities)-1)
            activity = activities[activity_type]
            doing(activity, use_time)
            time.sleep(use_time)
            doing(*self._relaxing)
            index += 1

    def listening(self):
        pass



if __name__ == "__main__":
    pp = PythonProgrammer()
    pp.working()