INPUT_FILE_PATH = './input7.txt'
def rec(ans,curr,digits,position):
    if((ans==curr*digits[position] or ans==curr+digits[position]) and position==len(digits)-1):
        return 1
    if(position==len(digits)-1):
        return 0
    else:
        plus=rec(ans,curr+digits[position],digits,position+1)
        mul=rec(ans,curr*digits[position],digits,position+1)
        if(plus==1 or mul==1):
            return 1
            
        
        

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
        sum=0
    for line in lines:
        ans,digits=line.split(": ")
        ans=int(ans)
        digits=digits.split(" ")
        numbers=[]
        for digit in digits:
            numbers.append(int(digit))
        if rec(ans,numbers[0],numbers,1)==1:
            sum+=ans
    print(sum)
        
if __name__ == "__main__":
    main()