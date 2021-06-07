from zxepay.common_api.PostMethod import *
from zxepay.common_api.JiaMi import *


class OrderCheck:

    def __init__(self):
        self.send = UrlPost()

# 第一条用例检查结果

    def order_check(self, data):


        result_list = self.send.post_json(data["order_list"]["url"], jia_mi(data["order_list"]["para"]))



        print('下单返回结果：', result_list)


        if result_list["msg"] == "交易成功":
            return True
        else:
            return False



# 第二条用例的检查结果

    def order_query(self, data):

        result = self.send.post_json(data["order_query"]["url"], jia_mi(data["order_query"]["para"]))

        print('下单返回结果：', result)
        if result["msg"] == "交易成功":
            return True
        else:
            return False