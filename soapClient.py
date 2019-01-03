from zeep import Client
from lxml import etree 
import xmlschema
import xml.dom.minidom

# client = Client('http://127.0.0.1:8000/soapAPI1/?wsdl')
soap = "https://selecttopic.herokuapp.com/soapAPI1/?wsdl"
client = Client(soap)


def showInfor(resultXMLtest):
    print("------------------------- Information ------------------------------")
    utf8_parser = etree.XMLParser(encoding='utf-8')
    root = etree.fromstring(resultXMLtest)
    for std in root.findall('student'):
        print("id :",std.find('id').text)
        print("name :",std.find('name').text)
        print("hobby :",std.find('hobby').text)
        print()

def showStock(resultXMLtest):
    print("------------------------------ Stock ------------------------------")
    utf8_parser = etree.XMLParser(encoding='utf-8')
    root = etree.fromstring(resultXMLtest.encode('utf-8'), parser=utf8_parser)

    for data in root.findall('item'):
        print("id :",data.find('id').text)
        print("sender :",data.find('sender').text)
        print("reciever :",data.find('reciever').text)
        print("weight :",data.find('weight').text)
        print("status :",data.find('status').text)
        print()

#################  ข้อ 1
# result = client.service.sendProfile()
# showInfor(result)

#################  ข้อ 2
# result = client.service.inserItem(20001,"Mark","331/587",2.35)
# print(result)

# result = client.service.updateItem(10003,1)
# print(result)

result = client.service.showStockAll()
print(result)
showStock(result)


