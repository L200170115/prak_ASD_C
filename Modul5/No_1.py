class MhsTIF(object):
    def __init__(self,nim):
        self.nim = nim
    def __str__(self):
        s = str(self.nim)
        return s

c0 = MhsTIF(21)
c1 = MhsTIF(87)
c2 = MhsTIF(54)
c3 = MhsTIF(39)
c4 = MhsTIF(44)
c5 = MhsTIF(20)
c6 = MhsTIF(14)
c7 = MhsTIF(16)
c8 = MhsTIF(90)
c9 = MhsTIF(114)
c10 = MhsTIF(105)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos-1].nim:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
def CetakDaftar(d):
    for i in d :
        print (i)

insertionSort(Daftar)
CetakDaftar(Daftar)




