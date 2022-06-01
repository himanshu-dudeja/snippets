from collections import defaultdict
st = "test string"
count = defaultdict(int)
for i in range(len(st)):
  count[st[i]] += 1
  
print(count)
