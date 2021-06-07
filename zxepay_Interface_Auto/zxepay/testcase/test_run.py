import os
import sys


# 指定目录：F://python//zxepay_Interface_Auto ,意思是把当前目录的上级目录加进去
sys.path.append(os.path.join(os.getcwd(), ".."))

from zxepay.common_api import LoadData
from zxepay.business.CheckResult import OrderCheck
from zxepay.common_api.Start_Jvm import start_jvm


import pytest
import allure
import jpype

sys.dont_write_bytecode = True


class Test_Order:

    print('当前地址：', os.getcwd())

    @allure.title("下单接口")
    @pytest.mark.parametrize('data', LoadData.load_data("order_data"))
    def test_order(self, data):
        start_jvm()
        print('data:', data)

        # assert OrderCheck.order_check(data)，不能这样写，因为OrderCheck 使用了初始化方法，所以必须初始化类

        assert OrderCheck().order_check(data)


    @allure.title("下单查询接口")
    @pytest.mark.parametrize('data1', LoadData.load_data("order_data"))
    def test_query(self, data1):
        print('data:', data1)

        assert OrderCheck().order_query(data1)
        jpype.shutdownJVM()