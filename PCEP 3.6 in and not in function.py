a0 = 2
r = 2
n = 50

geometric_series = [a0 * r**(i - 1) for i in range(1, n+1)]

b0=3
r2=2
n=25

geometric_series2=[b0*r2**(j-1) for j in range(1, n+1)]

print(geometric_series)
print(geometric_series2)
print("About geometric_series", "\nIs 3 in the sequence?: ", 3 in geometric_series)

