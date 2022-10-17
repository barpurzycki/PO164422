from typing import List

def fun1(a:List[List[int]], b:List[List[int]]) -> List[List[int]]:
    temp:List[List[int]]
    temp=[]
    for row in range(len(a)):
        temp2 = []
        for column in range(len(b[row])):
            temp2.append(a[row][column]+b[row][column])
        temp.append(temp2)
    return temp

macierz:List[List[int]]=[[1, 2, 3, 4],[5, 6, 7, 8]]
macierz2:List[List[int]]=[[1, 2, 3, 4],[5, 6, 7, 8]]
print(fun1(macierz, macierz2))
