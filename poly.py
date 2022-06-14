class Polynomials():

  def __init__(self, base=[]):
    self.base = base
    self.degree = self.degree()

  def get(self):
    exp = 0
    while input(f"Now at x to {exp}, add value? y/n: ") == 'y':
      self.base.append(int(input(f"Value for x to the {exp}: ")))
      exp += 1
    self.base.reverse()

  def sum(self, target):
    if len(self.base) >= len(target.base):
      big = self.base
      small = target.base
    else:
      big = target.base
      small = self.base
    big = big[:]
    for i in range(len(big)):
      if i in range(len(small)):
        big[i] += small[i]
    big = Polynomials(big)
    return big

  def subtract(self, target):
    if len(self.base) >= len(target.base):
      big = self.base
      small = target.base
    else:
      big = target.base
      small = self.base
    big = big[:]
    for i in range(len(big)):
      if i in range(len(small)):
        big[i] -= small[i]
    big = Polynomials(big)
    return big
    
  def mult(self, target):
    n = len(self.base)
    m = len(target.base)
    prod = [0] * (n + m -1)
    for i in range(n):
      for j in range(m):
        prod[i + j] += self.base[i] * target.base[j]
    prod = Polynomials(prod)
    self.restrict(prod)
    return prod

  def restrict(self, poly):
    while poly.base[-1] == 0 and len(poly.base) > 1:
      poly.base.pop()

  def degree(self):
    self.restrict(self)
    return len(self.base) - 1

  def div(self, target):
    remainder = self
    result = {'q':[], 'r':remainder.base}
    while remainder.degree >= target.degree and remainder.base != [0.0]:
      factor = remainder.base[-1]/target.base[-1]
      degree = remainder.degree - target.degree
      if result['q'] == []:
        result['q'] = [0] * (degree + 1)
      mult = [0] * (degree + 1)
      result['q'][degree] = factor
      mult[degree] = factor
      mult = Polynomials(mult)
      sub = target.mult(mult)
      remainder = remainder.subtract(sub)
      self.restrict(remainder)
      result['r'] = remainder
      self.restrict(remainder)
    result['q'] = Polynomials(result['q'])
    return result

  def remain(self, target):
    remainder = self
    while remainder.degree >= target.degree and remainder.base != [0.0]:
      factor = remainder.base[-1]/target.base[-1]
      degree = remainder.degree - target.degree
      mult = [0] * (degree + 1)
      mult[degree] = factor
      mult = Polynomials(mult)
      sub = target.mult(mult)
      remainder = remainder.subtract(sub)
      self.restrict(remainder)
    return remainder

  def gcd(self, target):
    zero = [0.0]
    A = self
    B = target
    if A.remain(B).base == zero:
      return B
    if B.remain(A).base == zero:
      return A
    TB = B
    R = A.remain(TB)
    while A.remain(R).base != zero or B.remain(R).base != zero:
      T = R
      R = TB.remain(R)
      TB = T
    return R

