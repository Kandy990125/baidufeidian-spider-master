# -*-coding:utf-8-*-
import time
import operator
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def fun(list):
    csv_file = open('data.csv', 'a')
    out = csv.writer(csv_file)
    for item in list:
        list = []
        list.append(item["time"] )
        list.append(item["name"])
        print item["name"]
        list.append(item["community_id"])
        list.append(item["vote"])
        list.append(item["thirdId"])
        out.writerow(list)
    csv_file.close()
def main():
    import requests
    url = "https://mbd.baidu.com/webpage?type=starhit&action=home&format=json&uk=ADW-FJtof7ZdvEgtPJ7e8A"
    html = requests.get(url).text
    import json
    dic = json.loads(html)
    timeStamp = float(dic["timestamp"])
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    time_s = otherStyleTime
    print time_s
    dic_main = dic["data"]["maleStar"]
    list = []
    for item in dic_main:
        new_item = {}
        new_item["time"] = time_s
        new_item["name"] = item["name"]
        # print new_item["name"]
        new_item["community_id"] = item["community_id"]
        # print int(new_item["community_id"])-(1000000000)
        new_item["vote"] = item["vote"]
        new_item["thirdId"] = item["thirdId"]
        list.append(new_item)
    list = sorted(list, key=operator.itemgetter('community_id'))
    # print list
    fun(list)

if __name__ == "__main__":
    while True:
        try:
            main()
            time.sleep(60)
        except:
            time.sleep(10)