# -*- coding: utf-8 -*-
import datetime, os, json

# 디렉토리 내 하나의 json 파일 탐색 후 list(dict) 형태로 반환
def get_data_from_json() :
    target, ret = "", []

    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".json"):
            target = filename
            break
        
    f = open(target, "r", encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        ret.append(json.loads(line))
    f.close()

    return ret

# log만 파일로 출력
def formatting(input) :
    export_name = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:-7]
    f = open(export_name + ".txt", 'w', encoding='UTF-8')

    for data in input :
        f.write(data["log"] + '\n')

    f.close()

formatting(get_data_from_json())