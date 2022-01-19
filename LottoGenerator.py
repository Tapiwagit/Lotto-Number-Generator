#random 6 number generator

import random

lotto_nums = []

for i in range(0, 6):
  num = random.randint(1, 52)
  while num in lotto_nums:
    num = random.randint(1, 52)
  lotto_nums.append(num)
  lotto_nums.sort()

print(f'Todays random lotto numbers picks are{lotto_nums}')