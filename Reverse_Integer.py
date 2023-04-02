class Solution:
    def check(self, res):
        if res < -2**31 or res > 2**31 -1:
            return 0
        else:
            return res
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x > 0:
            if str(x)[-1] != 0 :
                tmp = list(str(x))[::-1]
                res = int("".join(tmp))
            else:
                tmp = list(str(x))[::-1]
                tmp.pop(0)
                res = int("".join(tmp))                
        elif x < 0:
            s = abs(x)
            if str(s)[-1] != 0 :
                tmp = list(str(s))[::-1]
                res = int("".join(tmp))*-1
            else:
                tmp = list(str(s))[::-1]
                tmp.pop(0)
                res = int("".join(tmp))*-1
        return self.check(res)