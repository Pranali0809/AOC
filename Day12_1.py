INPUT_FILE_PATH = './temp.txt'
import string

def rec(i,j,lines,m,n,parent,area):
    if i<0 or j<0 or i>=m or j>=n:
        return 1
    if lines[i][j]==parent:
        lines[i][j]=lines[i][j].lower()
        return rec(i+1,j,lines,m,n,lines[i][j],area+1)+rec(i-1,j,lines,m,n,lines[i][j],area+1)+rec(i,j+1,lines,m,n,lines[i][j],area+1)+rec(i,j-1,lines,m,n,lines[i][j],area+1)
    else:
        return 0
    

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
        
    lines = [list(c) for c in lines]
    
    m=len(lines)
    n=len(lines[0])
    sum1=0
    print(lines)
    for i in range(m):
        for j in range(n):
            if lines[i][j]!=lines[i][j].lower():
                area=0
                peri=rec(i,j,lines,m,n,lines[i][j],area)
                sum1+=area*peri
    print(sum1)
if __name__ == "__main__":
    main()