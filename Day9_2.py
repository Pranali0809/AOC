INPUT_FILE_PATH = './input9.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read()
        sum=0
    i=0
    lines = [c for c in lines]
    index=0
    counterstart=0
    counterend=int(len(lines)/2)
    if len(lines)%2!=0:
        j=len(lines)-1
    else:
        j=len(lines)-2
   
    while i<=j:
        if i%2==0:
            for s in range(int(lines[i])):
                sum+=index*counterstart
                index=index+1
            counterstart=counterstart+1
            i=i+1
        else:
            if int(lines[i])<int(lines[j]):
                lines[j]=str(int(lines[j])-int(lines[i]))
                for q in range(int(lines[i])):
                    sum+=index*counterend
                    index=index+1
                i=i+1
            else:
                lines[i]=str(int(lines[i])-int(lines[j]))
                for r in range(int(lines[j])):
                    sum+=index*counterend
                    index=index+1
                counterend=counterend-1
                j=j-2    
    print(sum)            

if __name__ == "__main__":
    main()