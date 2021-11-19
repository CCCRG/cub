from django.http import Http404, HttpResponse
import datetime
import pymysql
import pymysql.cursors
from django.template.loader import get_template
from django.template import Context
import json
import time
import random
import math

def eyes_s(x,y,r):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_cub')
    cur = conn.cursor()
    cur.execute("select x1, y1, x2, y2 from stena")
    stxy = cur.fetchall()
    script1 = 'insert into eyes('
    script2 = 'value('
    n = 59
    s3 = 100
    r_l = 60
    s1 = 20
    ggg = 0
    s2 = s3 + s1
    ds1 = []
    ds2 = []
    sss = []
    for i in range(0, n+1):
        ds1.append(rotors(x + 10, y + 15, x + 25, y + 5 + s1 * i / n, r))
        ds2.append(rotors(x + 10, y + 15, x + 25 + s3, y + 5 - s3 / 2 + s2 * i / n, r))
    print ds1
    print ds2
    for i in range(0, n+1):
        print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        rrr = []
        for j in range(0,len(stxy)):
            print ('-------------------------------------------------------------------------------------------------')
            xy = distance_e(ds1[i][0],ds1[i][1],ds2[i][0],ds2[i][1],stxy[j][0],stxy[j][1],stxy[j][2],stxy[j][3])
            #if xy[0] - ds1[i][0] > 0 and ds2[i][0] - ds1[i][0] > 0 or xy[0] - ds1[i][0] < 0 and ds2[i][0] - ds1[i][0] < 0 or xy[1] - ds1[i][1] > 0 and ds2[i][1] - ds1[i][1] > 0 or xy[1] - ds1[i][1] < 0 and ds2[i][1] - ds1[i][1] < 0:
            rrr.append(math.sqrt((xy[0] - ds1[i][0]) * (xy[0] - ds1[i][0]) + (xy[1] - ds1[i][1]) * (xy[1] - ds1[i][1])))
            print xy, ds1[i], ds2[i]
        sss.append(min(rrr))
        script1 = script1 + 's' + str(i+1) + ',' + 'c' + str(i+1) + ','
        script2 = script2 + str(sss[i]) + ','
        script2 = script2 + str(0) + ','
    script1 = script1[0:len(script1) - 1] + ') '
    script2 = script2[0:len(script2) - 1] + ')'
    script = script1 + script2 + ';'
    cur.execute(script)
    conn.commit()
    print sss
    return script

def rotors(x0, y0, x, y, r):
    dx = x - x0
    dy = y - y0
    xy = [dx * math.cos(math.radians(r)) - dy * math.sin(math.radians(r)) + x0,
          dx * math.sin(math.radians(r)) + dy * math.cos(math.radians(r)) + y0]
    return xy

def distance_e(x1, y1, x2, y2, x3, y3, x4, y4):
    x1 = float(x1) + 0.00000000000000001
    y1 = float(y1) + 0.00000000000000001
    x2 = float(x2) + 0.00000000000000002
    y2 = float(y2) + 0.00000000000000002
    x3 = float(x3) + 0.00000000000000001
    y3 = float(y3) + 0.00000000000000001
    x4 = float(x4) + 0.00000000000000002
    y4 = float(y4) + 0.00000000000000002
    k1 = (y2 - y1) / (x2 - x1 + 0.00000000000000001)
    k2 = (y4 - y3) / (x4 - x3 + 0.00000000000000001)
    y01 = y1 - k1 * x1
    y02 = y3 - k2 * x3
    x = (y01 - y02) / (k2 -k1 + 0.00000000000000001)
    y = k1 * x + y01
    xy = [round(x),round(y)]
    return xy


print eyes_s(400, 3, -45)
