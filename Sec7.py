'''
Mirroring String
'''
string = input("Please enter a sentence: ")
ans=""
for i in string:
    ans = i + ans 
print(f"the sentence after mirroring is {ans}")
print(f"the sentence after mirroring is {string[::-1]}")