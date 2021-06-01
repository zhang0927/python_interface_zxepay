import json
import os
import yaml


def load_data(file_name):
    print(os.getcwd())
    file_path = "F://python//YitihuaInterface//XianYiTiHua//FengZhuang" + os.sep + "configure" + os.sep + file_name + ".yml"
    file = open(file_path, 'r', encoding='utf-8')
    data = yaml.load(file)
    return data


if __name__ == '__main__':
    da = load_data("order_data")