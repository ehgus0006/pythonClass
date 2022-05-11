import random
import sqlite3

count = 1
con = sqlite3.connect("pythonDB")
cur = con.cursor()
# cur.execute("create table lotto(count int, num1 int, num2 int, \
#             num3 int, num4 int, num5 int, num6 int)")

lucky_numbers = list()

while 0 <= len(lucky_numbers) < 6:
    b = random.randint(1, 45)
    if b not in lucky_numbers:
        lucky_numbers.append(b)
    else:
        continue

lucky_numbers.sort()
a = lucky_numbers

cur.execute("select max(count) from lotto")
row = cur.fetchone()
if row == None:
    count = 1
else:
    count = row[0] + 1


cur.execute("insert into lotto values(?, ?, ?, ?, ?, ?, ?)", \
            (count, a[0], a[1], a[2], a[3], a[4], a[5] ) )

con.commit()
print("회차 번호1 번호2 번호3 번호4 번호5 번호6")
print("----------------------------------")
cur.execute("select * from lotto")
while (True):
    row = cur.fetchone()
    if row == None:
        break
    d1 = row[0]
    d2 = row[1]
    d3 = row[2]
    d4 = row[3]
    d5 = row[4]
    d6 = row[5]
    d7 = row[6]
    print("%d %6d %6d %6d %6d %6d %6d" % \
          (d1, d2, d3, d4, d5, d6, d7))





