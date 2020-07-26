'''
# exercie 3

str_numb=[1,5,4,7,100,200]
count=0
for numb in str_numb:
    count=count+1
    print(f'{numb}')
    if int(len(str_numb)/2)==count:
        break

# exercie 4

str= ['coding of world','pen','python','hello']
print(f'{str}')
count=0
for x in str:

   x = str[count].upper()
   print(f'{x}')
   count=count+1



# exercie 5

str= ['coding of world','pen','python','hello']
print(f'{str}')
count=0
for x in str:
   if int(len(str[count]))<4 :
      print(f'{x}')
      break
   count=count+1


# exercie 6


str='jeremy fulop'
x=str[-5:]
print(f'{x}')
x=str[:3]
print(f'{x}')
char='a'
count=0
resu=0
for x in str:
  if x==char:
     resu=resu+1

print(f'{resu}')
if resu>0:
    print('true')
else:
    print('false')

x = str.split()
print(x)
print(x[::-1])
y=x[1].upper()
print(y)

z=int(len(x[0])/2)
y=x[0][z-1]
print(x[0].replace(y, ''),x[1])


# exercie 7

str='hello world'
resu=0
for x in str:
  if x=='o':
     resu=resu+1
print(f'{resu}')

y=''
for x in str:
   y=y+x
   if x=='o':
      break
print(f'{y}')

count=0
for x in str:
   if x=='o':
      break
   count=count+1
print(f'{str[count:]}')

print(str.replace('o',''))

# exercie 8

# exercie 10

str_numb=[1,5,200,7,100,8]
res=str_numb[0]
for x in str_numb:
    if x>res:
        res=x
print(f'max = {res}')
'''
# exercie 11

str_numb=[4,8,200],[4,3000,-1],[9,87,12]
res=0
countx=0
county=0
print(f'{str_numb[0]}')
x=0

for y in str_numb:
    for x in str_numb[county]:
#        print(f'{str_numb[county][countx]}')

        if str_numb[county][countx]>res:
            res=str_numb[county][countx]
        countx=countx+1
    print(f'{res}')
    res=0
    countx=0
    county=county+1
#print(f'{res}')



