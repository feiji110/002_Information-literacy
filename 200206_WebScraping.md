````py
    # -*- coding: utf-8 -*-
    """
    Created on Wed Feb  5 14:18:47 2020

    @author: angus
    """

    import requests
    url = 'http://www.webscrapingfordatascience.com/basichttp/'
    r = requests.get(url)
    print(r.text)
    # =============================================================================
    # 导入request模块，接着检索url内容，使用requests.get方法
    # 对URL执行HTTP GET请求，该方法会返回一个requests.Response的
    # python对象，其中包含许多http相应的信息。同样requests负责解析
    # HTTP响应。而r.text以文本形式包含HTTP响应的内容主体
    # =============================================================================

    import requests
    url = 'http://www.webscrapingfordatascience.com/basichttp/'
    r = requests.get(url)
    # Which HTTP status code did we get back from the server?
    print(r.status_code)
    # What is the textuaL status code?
    print(r.reason)
    # What were the HTTP reponse headers?
    print(r.headers)
    # The request information is saved as a Python object in r.request: 
    print(r.request)
    #What were the HTTP request headers?
    print(r.request.headers)
    # the HTTP response content:
    print(r.text)

````
