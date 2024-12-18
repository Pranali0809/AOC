INPUT_FILE_PATH = './input9.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read()
    sum=0
    i=0
    lines = [c for c in lines]
    numbers=[]

    index=0
    for i in range(len(lines)):
        if i%2==0:
            temp=""
            for j in range(int(lines[i])):
                temp=temp+str(index)
            numbers.append(temp)
            index=index+1
        else:
            temp=""
            for j in range(int(lines[i])):
                temp=temp+'.'
            numbers.append(temp)
    
    i=len(lines)-1
    j=len(lines)-1
    if(len(lines)%2==0):
        j=j-1

    start=1
    while i>0:
        start=1
        while(start<i):
            if numbers[start]!='' and numbers[start][0]=='.' and numbers[i] and numbers[i][0]!='.' and len(numbers[i])<=len(numbers[start]):
                numbers.insert(start,numbers[i])
                start=start+1
                numbers[start]='.'*(len(numbers[start])-len(numbers[i+1]))
                i=i+1
                numbers[i]='.'*len(numbers[i])
                break
            else:
                start=start+1
        i=i-1
    index=0
    for string in numbers:
        if string:
            if string[0]!='.':
                for char in string:
                    
                    sum+=int(char)*index
                    
                    index=index+1
            else:
                index=index+len(string)
            

    print(sum)
                        
if __name__ == "__main__":
    main()