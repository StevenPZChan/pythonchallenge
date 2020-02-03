---
title: '#30'
layout: post
categories: python
tags:
  - python
  - challenge
last_modified_at: 2020-02-03T17:20:00+08:00
---

继续挑战，越来越有趣了

---
### 第30题地址[yankeedoodle.html](http://www.pythonchallenge.com/pc/ring/yankeedoodle.html)
* <img src="http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.jpg" alt="yankeedoodle.jpg" width="30%" height="30%">
* 网页标题是`relax you are on 30`，题目内容为`The picture is only meant to help you relax`，[源码](view-source:http://www.pythonchallenge.com/pc/ring/yankeedoodle.html)里面有一行隐藏内容：
> <!-- while you look at the csv file --\>

很明显了，标题没有什么用，说这题是休息的，题目内容也说图片是帮助休息的，就只有提示里面那句话有用了，也就是下载[yankeedoodle.csv](http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv)了：


```python
import requests

with requests.Session() as sess:
    sess.auth = ('repeat', 'switch')
    response = sess.get('http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv').text
print(response[:200])
```

    0.82207, 0.91181, 0.88563, 0.78018, 0.64716, 0.34371, 0.28306, 0.21141,
    0.12154, 0.29302, 0.22339, 0.22462, 0.27513, 0.34526, 0.67971, 0.78513,
    0.96414, 0.72911, 0.99316, 0.72118, 0.90557, 0.98607, 0.


这个`csv`里面就是一些逗号分隔的数，看上去没什么规律，但都是**0-1**之间的数。应该就是一张图片了，只不过像素值归一化了。


```python
yankeedoodle = [f.strip() for f in response.split(',')]
print('count:', len(yankeedoodle))
```

    count: 7367


接下来就是找出图像的大小（质因数分解）：


```python
def prime_factor(n: int) -> tuple:
    factors = []
    while n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
                break
        else:
            factors.append(n)
            break
    return tuple(factors)

print(prime_factor(len(yankeedoodle)))
```

    (53, 139)


只有一种分解方式：$$7367=53\times139$$。所以图像大小为`(53, 139)`：


```python
from PIL import Image

img = Image.new('L', prime_factor(len(yankeedoodle)))
img.putdata([float(p) for p in yankeedoodle], 256)
img
```




![png]({{site.baseurl}}/images/30_yankeedoodle_files/30_yankeedoodle_8_0.png)



需要翻转一下：


```python
img = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
img
```




![png]({{site.baseurl}}/images/30_yankeedoodle_files/30_yankeedoodle_10_0.png)



写的是$$n=str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]$$，所以是三个数值一组，连成一个字符串：


```python
x = yankeedoodle
encoded_str = [str(x[i])[5] + str(x[i + 1])[5] + str(x[i + 2])[6] for i in range(0, len(x) // 3 * 3, 3)]
print(encoded_str[:20])
```

    ['083', '111', '044', '032', '121', '111', '117', '032', '102', '111', '117', '110', '100', '032', '116', '104', '101', '032', '104', '105']


这个也像是字节码，翻译一下：


```python
decoded_str = bytes(int(s) for s in encoded_str)
print(decoded_str.decode()[:200])
```

    So, you found the hidden message.
    There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage. 
    VTZ.l'tf*Om@I"p]#R`cWEBZ40o


所以，我们切换地址到[grandpa.html](http://www.pythonchallenge.com/pc/ring/grandpa.html)，来到了下一题。

### 总结：这一题仍然需要一些观察力足矣。
###### 本题代码地址[30_yankeedoodle.ipynb](https://github.com/StevenPZChan/pythonchallenge/blob/notebook/nbfiles/30_yankeedoodle.ipynb)
