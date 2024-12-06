import re
INPUT_FILE_PATH = './input2.txt'

def asc(vec):
    flag=True
    for i in range(len(vec)-1):
        diff=int(vec[i+1])-int(vec[i])
        if diff>3 or diff<1:
            if not flag:
                return 0
            flag=False
            
    return 1   
        
    
def desc(vec):
    flag=True
    for i in range(len(vec)-1):
        diff=int(vec[i])-int(vec[i+1])
        if diff>3 or diff<1:
            if not flag:
                return 0
            flag=False
    return 1 
    
def main():
    sum=0
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")

    for line in lines:
        word=line.split(" ")
        if int(word[0])>int(word[1]):
            sum+=desc(word)
        else:
            sum+=asc(word)
    
    print(sum)
        
if __name__ == "__main__":
    main()