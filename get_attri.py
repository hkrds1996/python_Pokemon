# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:03:01 2018

@author: kangrong
"""
import urllib2,cookielib
from bs4 import BeautifulSoup as bf
#import requests
def get_attri(href,user_agent):
#    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537/36 (KHTML, like Gecko) Chrome",
#         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
#	req=session.get(url,headers=headers);
#	soup=bf(req.text);
    cj=cookielib.CookieJar();
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);  
    request=urllib2.Request(href);
    request.add_header("User-Agent",user_agent);
    print(user_agent);
    response=urllib2.urlopen(request);
    soup=bf(response.read(),'html.parser');
    wei=[""];
    HP=[""];
    Attack=[""];
    SPA=[""];
    SPD=[""];
    Defense=[""];
    Speed=[""];
    TTL=[""];
    for tr in soup.find_all("tr"):
        if(tr.get_text().split()==[]): continue;
#        sp="属性".decode('utf-8');
#        if(tr.get_text().split()[0]==sp):
#            arr=tr.get_text().split()[1];
#            for td in tr.find_all("td"):
#                if(td.get_text()==arr):
#                    for lens in len(td.find_all('span')):
#                        atrr[lens]=td.find_all('span').get_text().encode('utf-8');
        sp="HP".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            HP[0]=arr.encode('utf-8');
        sp="攻击".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Attack[0]=arr.encode('utf-8'); 
        sp="防御".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            SPA[0]=arr.encode('utf-8');
        sp="特攻".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Defense[0]=arr.encode('utf-8');   
        sp="特防".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            SPD[0]=arr.encode('utf-8');                 
        sp="速度".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Speed[0]=arr.encode('utf-8');
        sp="总和".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            TTL[0]=arr.encode('utf-8');
        sp="体重".decode('utf-8');
        if(tr.get_text().split()[0].startswith(sp)):
            for td in tr.find_all('td'):
                arr=td.get_text().split()[0];
            wei=arr.encode('utf-8');
#        sp="生蛋蛋组".decode('utf-8');
#        if(tr.get_text().split()[0]==sp):
#            for i in range(1,len(tr.get_text().split())):
#                group[i-1]=tr.get_text().split()[i];
    return HP,Attack,SPA,Defense,SPD,Speed,TTL,wei;
