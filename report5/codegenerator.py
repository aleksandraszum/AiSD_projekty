c = {'e': '0000', 's': '0001', 'a': '001', 'k': '010000', 'T': '0100010', 'B': '0100011', 'g': '01001', 'i': '0101',
     't': '0110', 'c': '0111', ' ': '100', 'f': '1010000', 'M': '1010001', 'W': '1010010', 'S': '1010011',
     'P': '1010100', 'E': '1010101', 'I': '1010110', 'R': '1010111', 'm': '101100', '\n': '101101', 'A': '101110',
     'b': '101111', 'd': '11000', 'r': '11001', 'u': '11010', 'l': '11011', 'n': '1110', 'o': '1111'}

text = "A Web Simulation of Medical Image Reconstruction and Processing as an Educational Tool\nAbstract\nBackground"

for i in range(0, len(text) - 1):
    d = text[i]
    # print(c[d])

e = 0
s = 0
a = 0
k = 0
T = 0
B = 0
g = 0
ii = 0
t = 0
c = 0
f = 0
M = 0
W = 0
S = 0
P = 0
E = 0
I = 0
R = 0
m = 0
A = 0
b = 0
d = 0
r = 0
u = 0
l = 0
n = 0
o = 0
for i in range(0, len(text) - 1):
    if (text[i] == 'e'):
        e += 1
    if (text[i] == 's'):
        s += 1
    if (text[i] == 'a'):
        a += 1
    if (text[i] == 'k'):
        k += 1
    if (text[i] == 'T'):
        T += 1
    if (text[i] == 'B'):
        B += 1
    if (text[i] == 'g'):
        g += 1
    if (text[i] == 'i'):
        ii += 1
    if (text[i] == 't'):
        t += 1
    if (text[i] == 'c'):
        c += 1
    if (text[i] == 'f'):
        f += 1
    if (text[i] == 'M'):
        M += 1
    if (text[i] == 'W'):
        W += 1
    if (text[i] == 'S'):
        S += 1
    if (text[i] == 'P'):
        P += 1
    if (text[i] == 'E'):
        E += 1
    if (text[i] == 'I'):
        I += 1
    if (text[i] == 'R'):
        R += 1
    if (text[i] == 'm'):
        m += 1
    if (text[i] == 'A'):
        A += 1
    if (text[i] == 'b'):
        b += 1
    if (text[i] == 'd'):
        d += 1
    if (text[i] == 'r'):
        r += 1
    if (text[i] == 'u'):
        u += 1
    if (text[i] == 'l'):
        l += 1
    if (text[i] == 'n'):
        n += 1
    if (text[i] == 'o'):
        o += 1

#print('e: ', e)
#print('s: ', s)
print('a: ', a)
#print('k: ', k)
#print('t: ', T)
#print('B: ', B)
#print('g: ', g)
print('i: ', ii)
print('t: ', t)
print('c: ', c)
#print('f: ', f)
#print('M: ', M)
#print('W: ', W)
#print('S: ', S)
#print('P: ', P)
#print('I: ', I)
#print('R: ', R)
#print('m: ', m)
#print('A: ', A)
#print('b: ', b)
#print('d: ', d)
#print('r: ', r)
#print('u: ', u)
#print('l: ', l)
print('n: ', n)
print('o: ', o)
