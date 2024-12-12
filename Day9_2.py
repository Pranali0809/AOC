INPUT_FILE_PATH = './temp.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read()
        sum=0
    i=0
    lines = [c for c in lines]
    dot=[]
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
    
    i=0
    j=len(lines)-1
    if(len(lines)%2==0):
        j=j-1

    print(numbers)

    start=1
    for i in range(j,0,-2):
        print("i:",i)
        while(start<i):
            print("start: ",start)
            if numbers[start]!='' and numbers[start][0]=='.' and len(numbers[i])<len(numbers[start]):
                numbers.insert(start,numbers[i])
                start=start+1
                numbers[start]=numbers[start][len(numbers[i]):]
                numbers[i+1]='.'*len(numbers[i+1])
                print("t:",numbers[i+1],i+1)
                break
            else:
                start=start+1

    print(numbers)
                        


        

     



        
            
                
            
            
            
            




#     index=0
#     counterstart=0
#     counterend=int(len(lines)/2)

#     if len(lines)%2!=0:
#         j=len(lines)-1
#     else:
#         j=len(lines)-2
   
#     while i<=j:
#         if i%2==0:
#             for s in range(int(lines[i])):
#                 sum+=index*counterstart
#                 index=index+1
#             counterstart=counterstart+1
#             i=i+1
#         else:
#             if int(lines[i])<int(lines[j]):
#                 lines[j]=str(int(lines[j])-int(lines[i]))
#                 for q in range(int(lines[i])):
#                     sum+=index*counterend
#                     index=index+1
#                 i=i+1
#             else:
#                 lines[i]=str(int(lines[i])-int(lines[j]))
#                 for r in range(int(lines[j])):
#                     sum+=index*counterend
#                     index=index+1
#                 counterend=counterend-1
#                 j=j-2    
#     print(sum)            

if __name__ == "__main__":
    main()