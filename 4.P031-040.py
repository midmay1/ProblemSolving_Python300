##### Print Strings #####
print("#1")
print("="*30+"\n")
a = "3"
b = "4"
print(a + b)
## a + b command should be "3 4"
print("="*30+"\n")

print("#2")
print("="*30+"\n")
print("Hi" * 3)
## should be HiHiHi
print("="*30+"\n")

print("#3")
print("="*30+"\n")
print("-"*80)
## already I use this command
print("="*30+"\n")

print("#4")
print("="*30+"\n")
t1 = 'python'
t2 = 'java'
t0 = t1 + " " + t2 + " "
print(t0*3)
print("="*30+"\n")

print("#5")
print("="*30+"\n")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))
print("="*30+"\n")

print("#6")
print("="*30+"\n")
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

# I alread use the format method
print("="*30+"\n")

print("#7")
print("="*30+"\n")
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")
print("="*30+"\n")

print("#8")
print("="*30+"\n")
상장주식수 = "5,969,782,550"
num = int(상장주식수.replace(",",""))
print(num, type(num))
print("="*30+"\n")

print("#9")
print("="*30+"\n")
분기= "2020/03(E) (IFRS연결)"
str = 분기.split("(E)")[0]
print(str)
str = 분기[:7]
print(str)
print("="*30+"\n")

print("#10")
print("="*30+"\n")
data = "    삼성전자    "
data.strip() ; print(data)
data = data.strip() ; print(data)
print("="*30+"\n")
 
