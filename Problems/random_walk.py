import random

class SimpleRandomWalk:
    @staticmethod
    def random_walk(n):
        """Return coordinate after 'n' block random walk """
        x, y = 0, 0
        for i in range(n):
            step = random.choice(['N', 'S', 'E', 'W'])
            if step == 'N':
                y += 1
            elif step == 'S':
                y -= 1
            elif step == 'E':
                x += 1
            else:
                x -= 1
        return x, y


class RandomWalk:
    @staticmethod
    def random_walk(n):
        x, y = 0, 0
        for i in range(n):
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            x += dx
            y += dy
        return x, y




for i in range(25):
    walk = SimpleRandomWalk.random_walk(10)
    print(walk, "Distance from home =", abs(walk[0]+abs(walk[1])))
    print("+=+"*20)
    walk = RandomWalk.random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]+abs(walk[1])))
