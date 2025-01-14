INPUT_FILE_PATH = './temp.txt'
dict={
      'r':[0,1],
      'd':[1,0],
      'l':[0,-1],
      'u':[-1,0]
}

def rec(i,j,m,n,matrix,parent):
    if i<0 or j<0 or i>=m or j>=n:
        return [1,0]
    
    
    if parent.lower()== matrix[i][j]:
        return [0,0]
    
    if parent !=matrix[i][j]:
        return [1,0]
    
    
    if parent==matrix[i][j]:
        a=1
        p=0
        matrix[i][j]=matrix[i][j].lower()
        for k in dict.keys():
           temp=rec(i+dict[k][0],j+dict[k][1],m,n,matrix,parent)
           p+=temp[0]
           a+=temp[1]
        return [p,a]
    

def main():
    array_2d = []
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
        array_2d = [list(line) for line in lines if line.strip()]  # Convert each line into a list of characters
    
    m=len(array_2d)
    n=len(array_2d[0])
    sum=0
    for i in range(m):
        for j in range(n):
            if(array_2d[i][j]!=array_2d[i][j].lower()):
                ans=rec(i,j,m,n,array_2d,array_2d[i][j])
                sum+= (ans[0]*ans[1])
    print(sum)

if __name__ == "__main__":
    main()
        