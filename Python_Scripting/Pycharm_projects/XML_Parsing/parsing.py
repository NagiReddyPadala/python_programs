import xml.etree.ElementTree as ET
import time

myTree = ET.parse("resources.xml")
time.sleep(2)
myRoot = myTree.getroot()
print(myRoot)
print(myRoot.tag)
print(myRoot[0].tag)
print(myRoot[0].attrib)

for x in myRoot[0]:
    print(x.tag, x.attrib)
print("***************************************")
#print(myRoot.tag.findall('WIDGET_REFERENCE'))
# for widget_ref in myRoot.iter('WIDGET_REFERENCE'):
#     for widget in widget_ref.iter('WIDGET'):
#         fontName = x.find('name').text
#         fontSize = x.find('palette').text
#         print(fontName, "   ", fontSize)

# for x in myRoot:
#     print(len(x))
#
#     for ele in x:
#         print(ele.tag, ele.attrib)

# for data in myRoot.findall('./WIDGET_REFERENCE/WIDGET'):
#     print(data.text)

for data in myRoot.iter('WIDGET'):
    print(data.get('name'))


