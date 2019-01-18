import random

def random_walk(n):
    x,y = 0,0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(-1,0),(1,0)])
        x += dx
        y += dy
    return (x,y)

# Monte Carlo method
# simulate random walk with length 1-30
# find the longest walk with average distance < 5
number_of_walks = 10000
longest_walk = 0

for walk_len in range(1,31):
    hammin = 0
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_len)
        hammin += abs(x)+abs(y)
    hammin = hammin / number_of_walks
    if hammin < 5:
        longest_walk = walk_len
        print(hammin)

print("Walk size = ", longest_walk, " can be the longest walk")