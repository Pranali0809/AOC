import re
INPUT_FILE_PATH = './input4.txt'

dict={'tl':[-1,-1],'t':[-1,0],'tr':[-1,1],'r':[0,1],'dr':[1,1],'d':[1,0],'dl':[1,-1],'l':[0,-1]}
def rec(lines,i,j,position,m,n,key):
    if i<0 or j<0 or i>=m or j>=n:
        return 0
    if position==4 and lines[i][j]=='S':
        return 1
    if position==3 and lines[i][j]=='A':
        return rec(lines,i+dict[key][0],j+dict[key][1],4,m,n,key)
    if position==2 and lines[i][j]=='M':
        return rec(lines,i+dict[key][0],j+dict[key][1],3,m,n,key)
    return 0

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    m=len(lines)
    n=len(lines[0])
    sum=0
    for i in range(m):
        for j in range(n):
            if lines[i][j] == 'X':
                for key in dict.keys():
                    sum+=rec(lines,i+dict[key][0],j+dict[key][1],2,m,n,key)
    print(sum)           
            
    
    
if __name__ == "__main__":
    main()