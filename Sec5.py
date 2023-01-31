'''
Timer OverFlow
'''
res = int(input("Please enter the timer resolution: "))
freq = int(input("Please enter the System frequancy in MHZ: "))
pre = int(input("Please enter the Prescaller Value: "))
freq=freq*(10**6)/pre
ans = 1/freq * (2**res)
print (f"the timer would overflow after : {ans*1000} mili seconds")