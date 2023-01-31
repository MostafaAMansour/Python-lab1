'''
Print Pyramid
'''
i = 0
num = int(input("Please enter the maximum number of '*': "))
while i<num:
    print("*"*(i+1))
    i+=1
while i>1:
    print("*"*(i-1))
    i-=1
