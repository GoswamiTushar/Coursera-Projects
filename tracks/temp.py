import xml.etree.ElementTree as ET

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : 
	fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : 
        	return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


stuff = ET.parse(fname)

all = stuff.findall('dict/dict/dict')
# print(type(all), all, sep = '\n')
# print(all[1].items())
print('Dict count:', len(all))
print(lookup(all[0], 'Name'))
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : 
#     	continue

#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')

#     if name is None or artist is None or album is None : 
#         continue

#     print(name, artist, album, count, rating, length)