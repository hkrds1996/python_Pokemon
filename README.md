# python_Pokemon
using python to capture the data of Pokemon in Chinese Pokemon wiki
## using module: urllib2,cookielib,BeautifulSoup,codecs,csv,time
### codecs
For capturing the information in Chinese Website, the decoding different between python and web information is a big deal. You need to familiar with how to decode and encode character.
Codecs is a model to help you to fix the problem.
### csv
While there exist 5 different ways to hold data [blog](https://blog.csdn.net/weixin_39198406/article/details/78231430), I perfer to use csv to save data temporary.
### time,urllib2
Setting "user-agent" may help you get ride of web bloking, but normally it's not good enough. In this time, without enough money, setting big step(sleeping your function) may make sense.
