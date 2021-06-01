import json
import requests


class UrlPost:

    def __init__(self):
        """
        :return:
        """
        self.session = requests.session()
        # 依赖于api请求的Content-Type 方式  此时
        self.session.headers = {"Content-Type": "application/x-www-form-urlencoded", "appguid": "fiscal",
                                "user-agent": "okhttp/3.11.0",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
        # https 忽略校验
        self.session.verify = False

    def post_json(self, url, para):
        self.session.headers["Content-Type"] = "application/json"
        res = self.session.post(url, data=para)
        res_json = ''
        try:
            res_json = res.json()
        except:
            print("接口返回错误%s", res_json)

        return res_json
