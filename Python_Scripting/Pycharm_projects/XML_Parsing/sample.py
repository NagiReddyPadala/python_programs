import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")
root = tree.getroot()
#root = ET.fromstring("data")
print(root)
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, "  ", child.attrib)

print(root[0][1].text)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    print(country.get('name'), "  ", country.find('rank').text)
    ET.SubElement(country, "currency")

for currency in root.iter('currency'):
    currency.text = "INR"
tree.write('out2.xml')
# for rank in root.iter('rank'):
#     newRank = int(rank.text) + 1
#     rank.text = str(newRank)
#     rank.set('updated', 'yes')
# tree.write("out.xml")

# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write("out1.xml")




