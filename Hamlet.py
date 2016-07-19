import urllib
webUrl = "http://www.cs.iusb.edu/~yul/C151/hamlet.txt"
doc = urllib.urlopen(webUrl).read()
str_dst = doc.split()
str_dst = [x.lower() for x in str_dst]
print str_dst
from collections import Counter
word_counts = Counter(str_dst)
top_ten = word_counts.most_common(10)
print top_ten