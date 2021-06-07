import json
import os
import yaml


def load_data(file_name):

    #获取上一级目录

    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    file_path = os.getcwd() + os.sep + "configure" + os.sep + file_name + ".yml"
    file = open(file_path, 'r', encoding='utf-8')
    data = yaml.load(file)
    return data


if __name__ == '__main__':
    da = load_data("order_data")