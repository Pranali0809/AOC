INPUT_FILE_PATH = './temp.txt'

dict={
      'r':[0,1],
      'd':[1,0],
      'l':[0,-1],
      'u':[-1,0]
    }

def change(dir):
    if dir=='r':
        return 'd'
    elif dir=='d':
        return 'l'
    elif dir=='l':
        return 'u'
    else:
        return 'r'


def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        matrix = f.read().split("\n")
    m=len(matrix)
    n=len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    obstacle = [[0 for _ in range(m)] for _ in range(n)]
    pos=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=='#':
                obstacle[i][j]=1
            if matrix[i][j]=='^':
                pos=[i,j]
                obstacle[i][j]=2
    for i in range(m):
        print(obstacle[i])
    dir='u'
    count=1
    i,j=pos
    dp[i][j]='*'
    
    while(0<=i+dict[dir][0]<m and 0<=j+dict[dir][1]<n ):
        while( 0<=i+dict[dir][0]<m and 0<=j+dict[dir][1]<n and matrix[i+dict[dir][0]][j+dict[dir][1]]!='#'):
            i+=dict[dir][0]
            j+=dict[dir][1]
            if dp[i][j]!='*':
                dp[i][j]='*'
                count=count+1
                
        if(0<=i+dict[dir][0]<m and 0<=j+dict[dir][1]<n):
            dir=change(dir)
    
    print(count)
        
        
if __name__ == "__main__":
    main()