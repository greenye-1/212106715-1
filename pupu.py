import requests


def get_message():
    # 访问地址
    url = "https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/d8a2b28f-487a-44af-a1a9-4bfd4aea471b"
    # 头部信息
    headers={
        "Accept": "*/*",
        "pp-placeid": "43effc43-4fb2-4473-92e6-8ebecc67bb7a",
        "pp-version": "2021063201",
        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
        "Accept-Language": "zh-Hans-CN;q=1.0",
        "pp_storeid": "7c1208da-907a-4391-9901-35a60096a3f9",
        "User-Agent": "Pupumall/2.9.0;iOS 14.4;D7CC2F22-7AA0-47B9-991E-44B33EA43CE6",
        "Host": "j1.pupuapi.com",
        "Connection": "keep-alive",
    }
    # 爬取到的数据存到response里
    response = requests.get(url=url,headers=headers)
    # 将数据解析为json
    jsonData = response.json()
    # 根据json格式从json中提取取需要的信息
    name = jsonData['data']['name']
    float =  jsonData['data']['price']/100
    share_content = jsonData['data']['share_content']
    spec = jsonData['data']['spec']
    # 返回商品名称,价格,详情，规格
    print("获取到的数据为："+jsonData)


if __name__ == '__main__':
    get_message()