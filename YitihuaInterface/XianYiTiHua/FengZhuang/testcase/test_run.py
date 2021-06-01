import sys

sys.path.append('F://python//YitihuaInterface')

from XianYiTiHua.FengZhuang.common_api import LoadData
from XianYiTiHua.FengZhuang.business.CheckResult import OrderCheck
from XianYiTiHua.FengZhuang.common_api.Start_Jvm import start_jvm


import pytest
import allure
import jpype

sys.dont_write_bytecode = True


class Test_Order:

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