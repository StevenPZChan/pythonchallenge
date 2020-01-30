---
title: '#13'
layout: post
categories: python
tags:
  - python
  - challenge
last_modified_at: 2020-01-30T18:25:00+08:00
---

继续挑战

---
### 第13题地址[disproportional.html](http://www.pythonchallenge.com/pc/return/disproportional.html)
* <img src="http://huge:file@www.pythonchallenge.com/pc/return/disprop.jpg" alt="disprop.jpg" width="30%" height="30%">
* 网页标题是`call him`，题目内容是`phone that evil`，源码中没有隐藏信息，只有一个莫名的空标签`<remote />`

图片是一个电话机，其中**`5`**号键有个超链接[phonebook.php](http://www.pythonchallenge.com/pc/phonebook.php)<br>
显然解决问题要用到这个`php`了，我们直接打开看一看：


```python
import requests

response = requests.get('http://www.pythonchallenge.com/pc/phonebook.php').text
print(response)
```

    <?xml version="1.0"?>
    <methodResponse>
    <fault>
    <value>
    <struct><member><name>faultCode</name>
    <value><int>105</int></value>
    </member>
    <member>
    <name>faultString</name>
    <value><string>XML error: Invalid document end at line 1, column 1</string></value>
    </member>
    </struct>
    </value>
    </fault>
    </methodResponse>


嗯，返回结果是一个`xml`结构信息，并且报了很多的错误。

这个我一开始也是一头雾水，先去请教一下搜索引擎，`xml`里面用到了`<methodResponse>`这个的属于`RPC`的服务端回复：
> XML-RPC是一个远程过程调用（远程过程调用）（remote procedure call，RPC)的分布式计算协议，通过XML将调用函数封装，并使用HTTP协议作为发送机制。<br>
> XML-RPC透过向设备了这个协议的服务器发出HTTP请求。发出请求的客户端一般都是需要向远程系统要求调用的软件。
> ###### From [wikipedia.org](https://zh.wikipedia.org/wiki/XML-RPC)

实际上这个`XML-RPC`就是用指定的`xml`格式的数据用`http`的方式`post`到服务端，服务端解析数据后进行相应的操作，并按指定的`xml`格式的数据`response`到客户端。

幸运的我们发现`python`自带一个`xmlrpc`的模块，已经帮我们封装好了`xml`格式的编码和解析，并且也封装好了`post`请求的相关内容。<br>
我们来试一下：


```python
from xmlrpc.client import ServerProxy

server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(server.system.listMethods())
```

    ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']


服务端注册的方法除了`system`开头的那些就是那个显眼的`phone`了，结合题目我们基本确认就是要调用这个`phone`了。<br>
我们来看下用法：


```python
print(server.system.methodHelp('phone'))
print(server.system.methodSignature('phone'))
```

    Returns the phone of a person
    [['string', 'string']]


通过官方文档我们大致翻译一下这个用法的意思：
```python
def phone(person: str) -> str:
    """Returns the phone of a person"""
    return phone_of_person
```


```python
print(server.phone('evil'))
print(server.phone('that evil'))
```

    He is not the evil
    He is not the evil


那么问题来了，是要打电话给谁呢？<br>
别忘了，这个古老的挑战是需要前后联想的。<br>

---

我们翻回到前一题，还记得我们没有用到的那个信息么（`evil4.jpg`）：


```python
with requests.Session() as sess:
    sess.auth = ('huge', 'file')
    response = sess.get('http://www.pythonchallenge.com/pc/return/evil4.jpg').text
    print('evil4.jpg:')
    print(response)
```

    evil4.jpg:
    Bert is evil! go back!
    


那就试试这个**Bert**吧：


```python
print(server.phone('Bert'))
```

    555-ITALY


原来是打电话给**Bert**这个`evil`！<br>
这个回复怎么用呢？先试了[555-ITALY.html](http://www.pythonchallenge.com/pc/return/555-ITALY.html)是404错误，转而想到电话图片上链接就是在**`5`**上，所以把**`5`**去掉，修改地址为[ITALY.html](http://www.pythonchallenge.com/pc/return/ITALY.html)，打开后提示：
> SMALL letters.

最后结果是[italy.html](http://www.pythonchallenge.com/pc/return/italy.html)，来到了下一题。

### 总结：了解了一个传统应用`XML-RPC`，并开始了前后联想之旅。:)
###### 本题代码地址[13_disproportional.ipynb](https://github.com/StevenPZChan/pythonchallenge/blob/notebook/nbfiles/13_disproportional.ipynb)
