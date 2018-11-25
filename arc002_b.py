
from datetime import datetime
from datetime import timedelta


raw = input()
ds = datetime.strptime(raw, '%Y/%m/%d')
done = timedelta(days=1)
for i in range(1000*365):
  strs = ds.strftime('%Y/%m/%d')
  y, m, d = [int(s) for s in strs.split('/')]
  if y/m/d == y//m//d:
    print(strs)
    break
  ds += done
  
