import cmath, math, numpy
def add_complex( z1, z2):
    return z1 + z2
def sub_complex(z1, z2):
  return z1-z2
z1 = complex(2, 3)
z2 = complex(1, 2)
print( "Addition is : ", addComplex(z1, z2))
z1= complex(2,3)
z2= complex(1,2)
print("substraction is: ", subComplex(z1,z2))
z = complex(2,5)
print(" conjugate is: ", z.conjugate())
c = 4+ 4j
# phase
phase = cmath.phase(c)
print('4+ 4j Phase =', phase)
print('Phase in Degrees =', numpy.degrees(phase))
print('-4-4j Phase =', cmath.phase(-4-4j), 'radians. Degrees =', numpy.degrees(cmath.phase(-4-4j)))
# we can get phase using math.atan2() function too
print('Complex number phase using math.atan2() =', math.atan2(2, 1))
