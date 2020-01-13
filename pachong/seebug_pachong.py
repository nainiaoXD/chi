#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import re
import os
lianjie_list=[] #链接
biaoti_list=[]  #标题
url=r'https://paper.seebug.org'
headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'}
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title
def shouye():           #获取链接,标题名
    res=requests.get(url=url,headers=headers)
    zhenze_list=re.findall('''<a href="(.+)"><i
      class="fa fa-angle-right"></i>(.+)</a>''',res.text)
    for i in range(0,len(zhenze_list)) :                
        lianjie_list.append(zhenze_list[i][0])
        biaoti_list.append(zhenze_list[i][1]) 
        #wjm='d://seebug//{}'.format(biaoti_list[i])
        #os.mkdir(wjm)
def wenzhang():
    for i in range(0,len(lianjie_list)):
        url1=r'https://paper.seebug.org'+lianjie_list[i]
        res=requests.get(url=url1,headers=headers)
        zhenze_list=re.findall( '<span class="page-number">Page 1 of (.+)</span>',res.text) #匹配文章页数
        for j in range(0,int(zhenze_list[0])):  
            url2=url1+'?page='+str(j+1)
            res1=requests.get(url=url2,headers=headers)
            zhenze_list1=re.findall('<h5 class="post-title"><a href="(.+)">(.+)</a></h5>',res1.text) #p匹配文章链接
            for z in range(0,len(zhenze_list1)):
                url3=url+str(zhenze_list1[z][0])
                print(zhenze_list1[z][1])
                res=requests.get(url=url3,headers=headers) 
                with open('d://seebug//{}//{}.txt'.format(biaoti_list[i],validateTitle(zhenze_list1[z][1])),'w',encoding='utf-8') as f :
                    f.write(res.text)
                

#os.mkdir('d://seebug')
shouye()
wenzhang()
