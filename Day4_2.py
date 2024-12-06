INPUT_FILE_PATH = './input4.txt'
def isValid(char):
    if char=='M' or char=='S':
        return True
    return False

def check(lines,i,j):
    if lines[i-1][j-1]!=lines[i+1][j+1]  and isValid(lines[i-1][j-1]) and isValid(lines[i+1][j+1]):
        if lines[i-1][j+1]!=lines[i+1][j-1]  and isValid(lines[i-1][j+1]) and isValid(lines[i+1][j-1]):
            return 1
    return 0
    
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    m=len(lines)
    n=len(lines[0])
    sum=0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if lines[i][j] == 'A':
               sum+=check(lines,i,j)
    print(sum)           
            
if __name__ == "__main__":
    main()