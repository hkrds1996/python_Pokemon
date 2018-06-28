# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:23:55 2018

@author: kangrong
"""
import urllib2,cookielib
import os
import re
from bs4 import BeautifulSoup as bf
import codecs
import csv
import get_attri
import time
import random
import math
from pokemon_class import Pokemon,Chara
user_agent_list = [  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",  
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0 Zune 3.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 4.0.20402; MS-RTC LM 8)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.2)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; FDM; Tablet PC 2.0; .NET CLR 4.0.20506; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 3.0.04506; Media Center PC 5.0; SLCC1; Tablet PC 2.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET CLR 1.1.4322; InfoPath.2)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.3029; Media Center PC 6.0; Tablet PC 2.0)',  
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322)',  
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.0.3705; Media Center PC 3.1; Alexa Toolbar; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',  
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',  
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)',  
        'Mozilla/5.0 (MSIE 7.0; Macintosh; U; SunOS; X11; gu; SV1; InfoPath.2; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',  
        'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)',  
        'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)',  
        'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; fr-FR)',  
        'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)',  
        'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)',  
        'Mozilla/4.79 [en] (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',  
        'Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',  
        'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)',  
        'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)',  
        'Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0;)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; YPC 3.2.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727)',  
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 3.0.04506)',  
       ];
def pokemondata():
    cj=cookielib.CookieJar();
    #seesion=requests.Session();
    #headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537/36 (KHTML, like Gecko) Chrome",
              #         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);      
    #创建Pokemon对象                
    pokemon=[];
    pokemon_r=[];
    if(os.path.exists('pokemon.csv')):
        csv_file=codecs.open('pokemon.csv','r',"utf-8-sig");
        for stu in csv_file:
            tm=stu.split(',');
            poke=Pokemon(int(tm[0]),str(tm[1].encode('utf-8')),str(tm[2].encode('utf-8')));
            attri_t=re.split('[/]',tm[12][1:])
            texing_t=re.split('[/]',tm[13][1:]);
            poke.ADD(str(tm[3].encode('utf-8')),int(tm[4]),int(tm[5]),int(tm[6]),int(tm[7]),int(tm[8]),int(tm[9]),int(tm[10]),float(tm[11]),attri_t,texing_t,str(tm[14].encode('utf-8')));
            pokemon.append(poke);  
        pokemon_r=pokemon;
    else:
        url="http://www.pokemon.name/wiki/%E4%B8%BB%E9%A2%98:%E5%AE%9D%E5%8F%AF%E6%A2%A6";
        #创建Request对象
        #q=session.get(url,headers=headers);
        request=urllib2.Request(url);
        
        request.add_header("User-Agent","Mozilla/5.0");
        response=urllib2.urlopen(request);
        soup=bf(response.read(),'html.parser',from_encoding='utf-8');
        #	soup=bf(req.text);
        ccs=soup.find_all('td'); 
        for cc in ccs:
            links=cc.find_all('li');
            for link in links:        
                if(len(link.get_text().split('. '))==2):
                    H=link.find('a');
                    Root="http://www.pokemon.name";
                    poke=Pokemon(int(link.get_text().split('. ')[0].split()[0].encode('utf-8')),link.get_text().split('. ')[1].encode('utf-8') ,(Root.decode('utf-8')+H['href']).encode('utf-8') );                
                    m=get_attri.get_attri(poke.href,user_agent_list[int(math.floor(len(user_agent_list)*random.random()))]);
                    print poke.name,poke.array,time.localtime(time.time());
                    time.sleep(0.5*random.random());
                    poke.ADD(m[-1],m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10]);
                    pokemon.append(poke);
        csvFile = open("pokemon.csv", 'w+')
        try:
            csvFile.write(codecs.BOM_UTF8);
            writer = csv.writer(csvFile);
            for i in pokemon:
                for j in range(len(i.leixing)):
                    attri_t=""
                    for temp in i.attri[j]:
                        attri_t=attri_t+"/"+str(temp);
                    texing_t=""
                    for temp in i.texing[j]:
                        texing_t=texing_t+"/"+str(temp);
                    writer.writerow((i.array,i.name,i.href,i.leixing[j],int(i.HP[j]),int(i.Attack[j]),int(i.SPA[j]),int(i.Defense[j]),int(i.SPD[j]),int(i.Speed[j]),int(i.TTL[j]),float(i.Weight[j]),attri_t,texing_t,i.hide[j]));
                    pokemon_=Pokemon(i.array,i.name,i.href);
                    pokemon_.ADD(i.leixing[j],int(i.HP[j]),int(i.Attack[j]),int(i.SPA[j]),int(i.Defense[j]),int(i.SPD[j]),int(i.Speed[j]),int(i.TTL[j]),float(i.Weight[j]),i.attri[j],i.texing[j],i.hide[j])
                    pokemon_r.append(pokemon_)
                
        finally:
            csvFile.close();
    return pokemon_r;
###Pokemon属性
def charadata():
    cj=cookielib.CookieJar();
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);  
    chara=[];
    if(os.path.exists('character.csv')):
        csv_file=codecs.open('pokemon.csv','r',"utf-8-sig");
        for stu in csv_file:
            tm=stu.split(',');
            char=Chara(str(tm[0]),str(tm[1]));
            char.ADD(str(tm[2]),str(tm[3]));
            chara.append(char);
    else:
        url="www.baidu.com";
    
    
    
