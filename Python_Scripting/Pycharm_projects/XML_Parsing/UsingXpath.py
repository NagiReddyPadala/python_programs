import xml.etree.ElementTree as ET

root = ET.parse('sample.xml')

# Top-level elements
print(root.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
print(root.findall("./country/neighbor"))

# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))

# 'year' nodes that are children of nodes with name='Singapore'
print(root.findall(".//*[@name='Singapore']/year"))

# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))