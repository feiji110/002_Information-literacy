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
````
