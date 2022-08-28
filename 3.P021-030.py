##### String indexing  #####
print("#1")
print("="*30+"\n")
letters = 'python'
print(letters[0],letters[2])
print("="*30+"\n")

print("#2")
print("="*30+"\n")
license_plate = "24가 2210"
print(license_plate[-4:])
print("="*30+"\n")

print("#3")
print("="*30+"\n")
string="홀짝홀짝홀짝홀짝"
print(string[::2])
print("="*30+"\n")

print("#4")
print("="*30+"\n")
string="python"
print('origin string is "{}"'.format(string))
print("".join(reversed(string)))
reversed_string = ''
for item in string:
	reversed_string = item + reversed_string
print(reversed_string)
print(string[::-1])

print('For me the best is : print(string[::-1])')
print(string[::-1])
print("="*30+"\n")

print("#5")
print("="*30+"\n")
str="011-1111-2222"
phone_number = str.replace('-',' ')
print(phone_number)

import re
phone_number = re.sub("-"," ",str)
print(phone_number)

phone_number = str
for char in str:
	if char in "-":
		phone_number = phone_number.replace(char, " ")
print(phone_number)
print("="*30+"\n")

print("#6")
print("="*30+"\n")
str="011-1111-2222"
phone_number = str.replace('-','')
print(phone_number)

import re
phone_number = re.sub("-","",str)
print(phone_number)

phone_number = str
for char in str:
   if char in "-":
      phone_number = phone_number.replace(char, "")
print(phone_number)
print("="*30+"\n")

print("#7")
print("="*30+"\n")
url = "http://sharebook.kr"
url_print = url.split('.')[-1]
print(url_print)
print("="*30+"\n")

print("#8")
print("="*30+"\n")
lang='python'
##lang[0]='P'
#then lang should be "Python" , capital P
#### print(lang) ;;;;; 'str' object does not support item assignment ... Fail to guess.
print("="*30+"\n")

print("#9")
print("="*30+"\n")
str = 'abcdef2a364a32a'
str = str.replace('a','A')
print(str)
### It is why replace method is meaningful. str object does not support item assignment !!
print("="*30+"\n")

print("#10")
print("="*30+"\n")
str = 'abcd'
str.replace('b', 'B')
#then str should be "aBcd" in stead of 'abcd'
print(str)

#### I fail to guess again. replace method returns new object in stead of saving my command to original variables. So, if I just do str.replace A to B and not save to another (or the same) variables, my command can not be saved....
print("="*30+"\n")
 
