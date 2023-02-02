class Solution:
    def originalDigits(self, s: str) -> str:
        lst = []
        h = ''
        n = {'e':0, 'g':0, 'f':0, 'i':0, 'h':0, 'o':0, 'n':0,'s':0, 'r':0, 'u':0, 't':0, 'w':0, 'v':0, 'x':0, 'z':0}
        for x in s:
            if x in n:
                n[x]+= 1
        q = []
        for z in s:
            q.append(z)
        print(n)
        # Remove all zeroes, twos, fours, six, eight if they are in the string.
        if n['z'] != 0:
            while n['z'] > 0:
                lst.append('0')
                n['e'] -= 1
                n['r'] -= 1
                n['o'] -= 1
                n['z'] -= 1
        if n['w'] != 0:
            while n['w'] > 0:
                lst.append('2')
                n['t'] -= 1
                n['o'] -= 1
                n['w'] -= 1
        if n['u'] != 0:
            while n['u'] > 0:
                lst.append('4')
                n['f'] -= 1
                n['u'] -= 1
                n['o'] -= 1
                n['r'] -= 1
        if n['x'] != 0:
            while n['x'] > 0:
                lst.append('6')
                n['s'] -= 1
                n['i'] -= 1
                n['x'] -= 1
        if n['g'] != 0:
            while n['g'] > 0:
                lst.append('8')
                n['e'] -= 1
                n['i'] -= 1
                n['h'] -= 1
                n['t'] -= 1
                n['g'] -= 1

        # AFTER REMOVAL FIND ALL ODD NUMBERS!!! ALMOST THERE!!!
        # One, Three, Five, Seven, Nine
        
       
        if n['o'] != 0 and n['z'] <= 0 and n['w'] <= 0 and n['u'] <= 0:
            while n['o'] > 0:
                lst.append('1')
                n['e'] -= 1
                n['n'] -= 1
                n['o'] -= 1
        if n['h'] != 0 and n['g'] <= 0:
            while n['h'] > 0:
                lst.append('3')
                n['t'] -= 1
                n['r'] -= 1
                n['e'] -= 1
                n['e'] -= 1
                n['h'] -= 1
        if n['f'] != 0:
            while n['f'] > 0:
                lst.append('5')
                n['i'] -= 1
                n['v'] -= 1
                n['e'] -= 1
                n['f'] -= 1
        if n['i'] != 0 and n['f'] <= 0:
            while n['i'] > 0:
                lst.append('9')
                n['n'] -= 1
                n['n'] -= 1
                n['e'] -= 1
                n['i'] -= 1
        if n['n'] != 0 and n['f'] <= 0 and n['i'] <= 0:
            while n['n'] > 0:
                lst.append('7')
                n['s'] -= 1
                n['e'] -= 1
                n['v'] -= 1
                n['e'] -= 1
                n['n'] -= 1
        
        lst.sort()
        print(n)
        h = ''.join(lst)
        return h
