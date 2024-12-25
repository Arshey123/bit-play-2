# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# def check(a,b):
#     if ((a^b)!=0):
#         print("They are not equal")
#     else:
#         print("They are equal")
# print(check(a,b))
# Activity 2
def odd(arr):
    res=0
    for element in arr:
        res=res^element
    return res
arr= []
n=int(input("Enter an array:"))
while (n):
    num=int(input("Enter a number:"))
    arr.append(num)
    n-=1
print(odd(arr))