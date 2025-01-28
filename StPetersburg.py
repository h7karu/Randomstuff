'''The St Petersburg Paradox is a game with theoretically infinite expectation. I wrote out the following 
monte carlo simulation to find out the realistic amount of money we can expect to win from this game. 
(Its not very high, about 20-30)
'''

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
