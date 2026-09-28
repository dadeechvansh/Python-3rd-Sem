# x=int(input(""))
# l=[]
# for i in range(x):
#     c=int(input(""))
#     l.append(c)
# print("normal:",l)
# l.sort()
# o=[]
# for i in range(x-1,-1,-1):
#     o.append(l[i])
# print("sort():",l)
# print("rev desi",o)
# l.sort(reverse=True)
# print(l)

# attendance

# z=int(input(""))
# l=[]
# for i in range(z):
#     c=input("")
#     l.append(c)
# uni=[]
# for i in l:
#     if i not in uni:
#         uni.append(i)
# max=0
# for i in uni:
#     cnt=l.count(i)
#     print(i , "attended",cnt, "times")
#     if cnt>max:
#         max=cnt
# top=[]
# for i in uni:
#     if l.count(i)==max:
#         top.append(i)
# top.sort()
# print("Top attendee(s): ", end=" ")
# for name in top:
#     print(name, end=" ")

# armstrong

# n=input()
# digits=len(n)
# num=int(n)
# temp=num
# sum=0
# for i in range(digits):
#     n1=num%10
#     cal=n1**digits
#     sum+=cal
#     num//=10
# if sum== temp:
#     print("Armstrong")
# else:
#     print("Not")


# max in 3

# a=int(input())
# b=int(input())
# c=int(input())
# max=0
# if a>b and a>c:
#     max=a
# elif b>a and b>c:
#     max=b
# elif c>a and c>b:
#     max=c
# print(max)



# voweel /con

x=input().lower()
y=x.replace(" ","")
vowel="aeiou"
v=0
c=0
for i in y:
    if i in vowel:
        v+=1
    else:
        c+=1
print(f"vowels : {v} & Consonants : {c}")