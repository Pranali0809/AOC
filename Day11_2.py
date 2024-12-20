INPUT_FILE_PATH = './temp.txt'

def rec(line,ct):
    if ct==75:
        return len(line)
    j=0
    while j<len(line):
        word=line[j]
        if word=='0':
            line[j]='1'
            j=j+1
        elif len(word)%2==0:
            first, second = word[:len(word)//2], word[len(word)//2:] 
            line[j]=str(int(first))
            line.insert(j+1,str(int(second)))
            j=j+2
        else:
            line[j]=str(int(word)*2024)
            j=j+1
    
    return rec(line,ct+1)


def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split(" ")
    

    
    ans=0
    for i in range(len(lines)):
        ans+=rec([lines[i]],0)

    print(ans)

        
        


if __name__ == "__main__":
    main()