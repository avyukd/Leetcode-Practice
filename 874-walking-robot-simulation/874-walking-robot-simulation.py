class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        maxdist = 0
        
        obset = set()
        for ob in obstacles:
            obset.add((ob[0], ob[1]))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        currPos = [0, 0]
        currDir = 0
        
        for command in commands:
            print(command)
            print(currDir)
            if command == -1:
                currDir += 1
                currDir %= 4
            elif command == -2:
                currDir += 3
                currDir %= 4
            else:
                k = command
                while k != 0:
                    currPos[0] += directions[currDir][0]
                    currPos[1] += directions[currDir][1]
                    if (currPos[0], currPos[1]) in obset:
                        currPos[0] -= directions[currDir][0]
                        currPos[1] -= directions[currDir][1]
                        break
                    k-=1
                maxdist = max(maxdist, currPos[0]**2 + currPos[1]**2)
        
        return maxdist