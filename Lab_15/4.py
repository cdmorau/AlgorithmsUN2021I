import numpy

def LCS2(s1, s2, n1, n2):
    Matrix = numpy.zeros((n1+1 , n2+1))
    for i in range(1, n1+1):
        for j in range(1, n2+1):
          if s1[i-1] == s2[j-1]:
              Matrix[i][j] = Matrix[i-1][j-1] + 1
          else:
              Matrix[i][j] = max(Matrix[i][j-1], Matrix[i-1][j])
    
    return (int(Matrix[n1][n2]), Matrix)
if __name__ == '__main__':
    n1, s1, n2, s2 = int(input()), input(), int(input()), input() 
    s1, s2 = [int(i) for i in s1.split()], [int(i) for i in s2.split()]
    LCS_length, Matrix = LCS2(s1, s2, n1, n2)
    print(LCS_length)
