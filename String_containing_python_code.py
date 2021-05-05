mycode='print("hello world")'
code="""
def multiply(x,y):
    return x*y
print("the multiply of 6 and 4 is:",multiply(6,4))
"""
exec(mycode)
exec(code)