#BFS O(NlogN)
class Solution:
    def racecar(self, target: int) -> int:
        tmp=[(0,1)]
        cnt=0
        used={(0,1)}
        while tmp:
            new=[]
            for pos,speed in tmp:
                if pos==target:
                    return cnt
                elif pos >= 10000 or -1>= pos:
                    continue
                if (pos+speed,speed*2) not in used:
                    new.append((pos+speed,speed*2))
                    used.add((pos+speed,speed*2))
                if speed>0 and (pos,-1) not in used:
                    new.append((pos,-1))
                    used.add((pos,-1))
                elif speed<0 and (pos,1) not in used:
                    new.append((pos,1))
                    used.add((pos,1))
            tmp=new
            cnt+=1

#DP  O(NlogN)
#
class Solution(object):
    def __init__(self):self.dp={0:0}
    def racecar(self, t):
        if t in self.dp: return self.dp[t]
        n=t.bit_length()
        if 2**n-1 == t: self.dp[t]=n
        else:
            self.dp[t]=self.racecar(2**n-1-t)+n+1 ##pass by the target then go back 2**n-1-t
            for add in range(n-1):
                self.dp[t]=min(self.dp[t],self.racecar(t-2**(n-1)+2**add)+n+add+1) ##straight to the closest place to the target then stop and move carefully
        return self.dp[t]