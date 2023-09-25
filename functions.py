#create function

def sayHello(name='sam'):
    print(f'Hello {name}')
    
#return values
def getsum(num1, num2):
    total = num1 + num2
    return total

#a lambda function is a small anonymous function.
#a lambda function can take any nuymber of arguments, but can only have one expression.
getsum = lambda num1, num2 : num1 + num2


print(getsum(10,3))