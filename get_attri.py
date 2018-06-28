# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:03:01 2018

@author: kangrong
"""
import urllib2,cookielib
from bs4 import BeautifulSoup as bf
import re
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
    wei=[];
    HP=[];
    Attack=[];
    SPA=[];
    SPD=[];
    Defense=[];
    Speed=[];
    TTL=[];
    atrr=[];
    texing=[];
    hide=[];
    zhuangtai=[];
    m=0;
    for tbody in soup.find_all('table'):
     m=m+1;
     if(m==6):
         tm=tbody;
         break;
    for td in tm.find_all("div"):        
        if(len(td.get_text().split())==0):continue;
        if((td.get_text().encode('utf-8') not in zhuangtai)&(td.get_text()!="")):
            zhuangtai.append(td.get_text().encode('utf-8'));
    for tr in soup.find_all("tr"):
        if(tr.get_text().split()==[]): continue;
        sp="属性".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            atrr_T=[];
            arr=tr.get_text().split()[1];
            for td in tr.find_all("td"):
                if(td.get_text()==arr):
                    for lens in range(len(td.find_all('span'))):
                        atrr_T.append(td.find_all('span')[lens].get_text().encode('utf-8'));
            atrr.append(atrr_T);
        sp="特性".decode('utf-8'); 
        if(tr.get_text().split()[0]==sp):
            texing_T=[]
            arr=re.split('[\n/]',tr.get_text());
            for iv in arr[1:]:
                texing_T.append(iv.split()[0].encode('utf-8'));
            texing.append(texing_T);        
        sp="隐藏特性".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            hide.append(arr.encode('utf-8')); 
        sp="HP".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            HP.append(arr.encode('utf-8'));
        sp="攻击".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Attack.append(arr.encode('utf-8')); 
        sp="防御".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            SPA.append(arr.encode('utf-8')); 
        sp="特攻".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Defense.append(arr.encode('utf-8'));    
        sp="特防".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            SPD.append(arr.encode('utf-8'));                
        sp="速度".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            Speed.append(arr.encode('utf-8')); 
        sp="总和".decode('utf-8');
        if(tr.get_text().split()[0]==sp):
            arr=tr.get_text().split()[1];
            TTL.append(arr.encode('utf-8')); 
        sp="体重".decode('utf-8');
        if(tr.get_text().split()[0].startswith(sp)):
            for td in tr.find_all('td'):
                arr=td.get_text().split()[0];
                arr=arr.split('kg')[0];
            wei.append(arr.encode('utf-8')); 
#        sp="生蛋蛋组".decode('utf-8');
#        if(tr.get_text().split()[0]==sp):
#            for i in range(1,len(tr.get_text().split())):
#                group[i-1]=tr.get_text().split()[i];
    return HP,Attack,SPA,Defense,SPD,Speed,TTL,wei,atrr,texing,hide,zhuangtai;
