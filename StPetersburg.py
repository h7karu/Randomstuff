import random 

sum = 0
for i in range(10000000):
    payout = 2
    flip = random.getrandbits(1)
    while flip != 1:
        payout *= 2
        flip = random.getrandbits(1)
    sum += payout
print(sum / 10000000.0)