class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque([])
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                if asteroids[i] > 0:
                    stack.append(asteroids[i])
                else:
                    addAsteroid = True
                    while stack and stack[-1] > 0:
                        if stack[-1] > -asteroids[i]:
                            addAsteroid = False
                            break
                        elif stack[-1] < -asteroids[i]:
                            stack.pop()
                        else:
                            stack.pop()
                            addAsteroid = False
                            break
                    if addAsteroid:
                        stack.append(asteroids[i])
        return list(stack)