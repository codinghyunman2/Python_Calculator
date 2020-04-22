#1번 
def isodd(num):
  if num % 2 == 0: 
    print("짝수")
  else: 
    print("홀수")

#2번
def gugudan_odd(): 
  for i in range(2, 10, 2):
    for j in range(1, 10):
      print(f'{i} * {j} =', i * j)

def gugudan_even(): 
  for i in range(1, 10, 2):
    for j in range(1, 10):
      print(f'{i} * {j} =', i * j)

#합치기 
def gugudan_odd_or_even(num):
  if num % 2 == 0: 
    gugudan_even()
  else: 
    gugudan_odd()

gugudan_odd_or_even(4)

#인자에 따라 출력
def gugudan(num):
  i = num
  while i < 10: 
    for j in range(1, 10):
      print(f'{i} * {j} =', i * j)
    i += 2 

#1이면 홀수단, 2이면 짝수단
def gugudan_odd_even(num):
  if num % 2 == 0: 
    gugudan(2)
  else: 
    gugudan(1)

def gugudan_input(num): 
  i = 1
  while i <= num: 
    for j in range(1, 10):
      print(f'{i} * {j} =', i * j)
    i += 1 





