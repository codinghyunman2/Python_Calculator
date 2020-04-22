class FourCal: 
  def __init__(self, name, age, univ):
    self.name = name
    self.age = age
    self.univ = univ
    self.add_num = 0 
    self.sub_num = 0 
    self.mul_num = 0 
    self.div_num = 0 

  def add(self, n1, n2):
    self.add_num += 1
    return n1 + n2
  
  def sub(self, n1, n2):
    self.sub_num += 1
    return n1 - n2

  def mul(self, n1, n2):
    self.mul_num += 1
    return n1 * n2  

  def div(self, n1, n2):
    self.div_num += 1 
    if n2 == 0: 
      print("0으로 나눌 수 없습니다.")
      return None
    return n1 / n2
  
  def ShowCount(self):
    print("덧셈 :", self.add_num)
    print("뺄셈 :", self.sub_num)
    print("곱셈 :", self.mul_num)
    print("나눗셈 :", self.div_num)
  
 

calculator1 = FourCal("김현민", 25, "korea.univ")
print(calculator1.name, calculator1.age, calculator1.univ)
print(calculator1.add(3, 4))
print(calculator1.sub(5, 7))
print(calculator1.mul(3, 4))
print(calculator1.div(8, 4))
calculator1.ShowCount()
