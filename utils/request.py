from datetime import datetime
import requests
from utils.global_constant import GlobalConstant
class Request:
    base_url=GlobalConstant.BASE_URL_DEV
    # base_url=GlobalConstant.BASE_URL_PROD
    def __init__(self,authorization='') -> None:
        self.authorization=authorization
        pass
    
    def set_authorization(self,authorization) -> None:
        self.authorization = authorization

    def get(self,url='',headers={},params={}) -> requests.Response:
        headers["Authorization"] = self.authorization
        url = '{}{}'.format(Request.base_url,url)
        return requests.get(url=url,headers=headers,params=params,timeout=60)
    
    def post_with_formdata(self,url='',headers={},data={},files=None) -> requests.Response:
        headers["Authorization"] = self.authorization
        url = '{}{}'.format(Request.base_url,url)
        if files is None:
            return requests.post(url=url,headers=headers,data=data,timeout=60)
        else:
            return requests.post(url=url,headers=headers,files=files,data=data,timeout=60)
    
    def post_with_json(self,url='',headers={},json={}) -> requests.Response:
        headers["Authorization"] = self.authorization
        url = '{}{}'.format(Request.base_url,url)
        return requests.post(url=url,headers=headers,json=json,timeout=60)

    @staticmethod
    def check_response(response:requests.Response) -> None:
        result = response.json()
        if not result:
            raise Exception("返回数据为空")
        elif 'code' not in result:
            raise Exception("返回数据格式不包含code,response.json()为:{}".format(str(response.json())))
        elif result["code"] != 200:
            raise Exception("请求失败,code:{},message:{}".format(result['code'],result['message'])) 

    @staticmethod
    def with_prod(is_prod:bool):
        if is_prod:
            if Request.base_url == GlobalConstant.BASE_URL_PROD:
                return
            authenority_code = input("please input the authority code:")
            if authenority_code == datetime.now().strftime("%x"): # dd/MM/yy
                Request.base_url = GlobalConstant.BASE_URL_PROD
            else:
                print("anthority failure!")
        else:
            Request.base_url = GlobalConstant.BASE_URL_DEV
