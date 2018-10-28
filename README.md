# 简书爬虫

## selenium 通用爬虫 mysql保存 

### 问题：
Traceback (most recent call last):
  File "C:\python3.7\lib\site-packages\twisted\internet\defer.py", line 1418, in _inlineCallbacks
    result = g.send(result)
  File "C:\python3.7\lib\site-packages\scrapy\core\downloader\middleware.py", line 37, in process_request
    response = yield method(request=request, spider=spider)
  File "D:\a_code\chuanzhi\jianshu_spider\jianshu_spider\middlewares.py", line 19, in process_request
    self.driver.get(request.url)
TypeError: get() missing 1 required positional argument: 'url'