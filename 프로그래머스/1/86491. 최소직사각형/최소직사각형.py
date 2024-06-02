def solution(sizes):
    left=0
    right=0
    for size in sizes:
        if size[0]<size[1]:
            size[0],size[1]=size[1],size[0]
        if size[0]>left:
            left=size[0]
        if size[1]>right:
            right=size[1]
    
    return right*left