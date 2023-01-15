from time import process_time
import hashlib


t1 = process_time()
cipher = input()
r=0
data = cipher + str(r)
x = hashlib.sha256(data.encode('utf-8')).hexdigest()
while r>=0 :
  data = cipher + str(r)
  x = hashlib.sha256(data.encode('utf-8')).hexdigest()
  r = r+1
  if x.startswith("00000"):
    break

print(x)
print(data)
t2 = process_time()
print(t2-t1)
