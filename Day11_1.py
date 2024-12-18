INPUT_FILE_PATH = './input11.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        line = f.read().split(" ")
        
    for i in range(25):
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

    print(len(line))        
        


if __name__ == "__main__":
    main()