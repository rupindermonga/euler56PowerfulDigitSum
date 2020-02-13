'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

def getSum(n): 
    sum = 0
    while (n != 0):
        sum += n % 10
        n = n//10 
    return sum

def PowerfulDigitalSum(a,b):
    #a^b, max number of a and b
    max_sum = 0
    for eachNumber in range(a):
        for eachPower in range(b):
            new_sum = getSum(eachNumber**eachPower)
            max_sum = max(new_sum, max_sum)
    return max_sum

final = PowerfulDigitalSum(100,100)
print(final)