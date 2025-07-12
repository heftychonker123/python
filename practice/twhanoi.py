def solve(start,des,aux,n):
    if n==1:
        print(start+des)
        return
    print(start+aux)
    print(start+des)
    print(aux+des)
    solve(aux,des,start,n-1)
solve("A","B","C",3)