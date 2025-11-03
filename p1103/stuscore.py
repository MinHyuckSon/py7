#로또 만들기
import random

iLotto = random.sample(range(1,46),6)

print(iLotto)
iCount = 0

my_Lotto = []
for i in range(5):
    my_Lotto.append(random.sample(range(1,46),6))

print(my_Lotto)