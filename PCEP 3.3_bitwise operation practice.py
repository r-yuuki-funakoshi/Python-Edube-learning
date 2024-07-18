x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(bin(x)[2:])
print(bin(y)[2:])
print(a, b, c, d, e, f)
print(bin(a)[2:])
print(bin(b)[2:])
print(bin(c)[2:])
print(bin(d)[2:])
print(bin(e)[2:])
print(bin(f)[2:])

x=-1
y=6

a=x&y
b=x|y
c=~x
d=~y
e=x^y
f=x>>2
g=x<<2

print(a,b,c,d,f,g)
