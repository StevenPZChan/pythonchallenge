---
title: '#4'
layout: post
categories: python
tags:
  - python
  - challenge
last_modified_at: 2018-08-22T10:40:00+08:00
---
继续挑战

---
### 第4题地址[linkedlist.php](http://www.pythonchallenge.com/pc/def/linkedlist.php)
* <img src="http://www.pythonchallenge.com/pc/def/chainsaw.jpg" alt="chainsaw.jpg" width="30%" height="30%">
* 网页标题是`follow the chain`
* 图片是小人锯东西❓❓❓

惯例打开网页源码[view-source](view-source:http://www.pythonchallenge.com/pc/def/linkedlist.php)，发现注释文字：
> urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

分析一下这段话的意思。首先提示`urllib`会对我们有帮助，还说400次足够了，还有`NOTHINGS`是个什么东西，为什么要试400次？<br>
在愁眉莫展的时候发现源码里面还有一个超链接，原来点击图片是会链接到一个页面[nothing=12345](http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345)的<br>
> and the next nothing is 44827

这样的话，`nothing`是个什么东西，还有为什么400次就很明了了。

> #### 这里简单说下网页中`?`的意思：<br>
> `?`表示`GET`方法，后面用`key1=value1&key2=value2[&...]`的方式传递参数<br>
> 然后后台使用php（本题）、asp、js得方式来进行处理并返回`GET`结果

就不废话了，我们先试个400次，不过我们用`requests`不用`urllib`，因为前者要好用一些：


```python
import re
import requests
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'
for i in range(400):
    response = requests.get(url + nothing).text
    result = re.findall(r'next nothing is (\d+)', response)
    if not result:
        print('nothing =', nothing)
        print(response)
        break
    nothing = result[0]
```

    nothing = 16044
    Yes. Divide by two and keep going.
    

有意思的是，在第二次的时候会提示`Your hands are getting tired`，正好说明了不建议手工操作:D<br>
在若干次之后停了下来，显示
> Divide by two and keep going.

也很好理解，我们继续。


```python
import re
import requests
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = str(16044 / 2)
for i in range(400):
    response = requests.get(url + nothing).text
    result = re.findall(r'next nothing is (\d+)', response)
    if not result:
        print('nothing =', nothing)
        print(response)
        break
    nothing = result[0]
```

    nothing = 66831
    peak.html
    

若干次之后也停了下来（中间出现了一次`There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579`，说明不能光区配数字来取结果，不然就是
[nothing=82683](http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82683)：
`You've been misleaded to here. Go to previous one and check.`）。<br>
看一下结果，是[`peak.html`](http://www.pythonchallenge.com/pc/def/peak.html)，打开之后到了下一题！

### 总结：这一题体会到了使用获取到的数据分析后继续获取数据的用法，用代码来实现也是十分爽快了。
###### 本题代码地址[4_linkedlist.ipynb](https://github.com/StevenPZChan/pythonchallenge/blob/notebook/nbfiles/4_linkedlist.ipynb)
