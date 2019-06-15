a = 23
b = 33
c = a + b
d = a - b
e = a / b
f = a * b
print(c)
print("Sum is",c)
print("Sum of",a,"and",b,"is",c)
print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))
print("Sum of {} and {} is {}".format(a,b,c))
print(f"Sum of {a} and {b} is {c}")

print("""
Sum is {}
Diff is {}
Div is {}
Mul is {}
""".format(c,d,e,f))

#print("1.Add\t2.Sub")
#print("3.Div\t4.Mul")

print("""
1. Add       2. Sub
3. Div       4. Mul
""")
