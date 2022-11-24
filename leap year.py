import datetime

def leapyear(year):

  if (year % 400 == 0) and (year % 100 == 0):
    leap.append(year)

  elif (year % 4 ==0) and (year % 100 != 0):
    leap.append(year)

  else:
    nonleap.append(year)

leap=[]
nonleap=[]
a=input("Enter 1st Date:")
c=input("Enter 2nd Date:")
b=datetime.datetime.strptime(a,'%d/%m/%Y')
d=datetime.datetime.strptime(c,'%d/%m/%Y')
for i in range(b.year, d.year+1):
  leapyear(i)

print("Leap Years:",leap)
print("Non-Leap Years:",nonleap)
