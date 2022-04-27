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
z=3+2j
z.real
z=3+2j
z.imag
z1 = 2 + 3j
z2 = 4 + 5j
z1 * z2
z1 = 2 + 3j
z2 = 4 + 5j
z1 / z2
algebraic = 3 + 2j
geometric = complex(3, 2)
radius, angle = cmath.polar(algebraic)
trigonometric = radius * (cmath.cos(angle) + 1j*cmath.sin(angle))
exponential = radius * cmath.exp(1j*angle)

for number in algebraic, geometric, trigonometric, exponential:
  print(format(number, "g"))
