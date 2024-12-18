INPUT_FILE_PATH = './input10.txt'

def rec(lines,i,j,m,n,curr):
    if i<0 or i>=m or j<0 or j>=n or int(curr)+1 != int(lines[i][j]):
        return 0
    
    if (lines[i][j]=='9' ):
        return 1
    
    return rec(lines,i+1,j,m,n,lines[i][j])+rec(lines,i-1,j,m,n,lines[i][j])+rec(lines,i,j+1,m,n,lines[i][j])+rec(lines,i,j-1,m,n,lines[i][j])


def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")    

    lines = [c for c in lines]
    sum=0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=='0':
                sum+=rec(lines,i,j, len(lines),len(lines[0]),-1)

    print(sum)
if  __name__ == "__main__":
    main()