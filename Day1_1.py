
import re
INPUT_FILE_PATH = './input1.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    
    list1=[]
    list2=[]
    for line in lines:
        word=line.split("   ")
        list1.append(int(word[0]))
        list2.append(int(word[1]))

    list1.sort()
    list2.sort()
    sum1=0
    for i in range(len(list1)):
        sum1+=abs(list2[i]-list1[i])
    print(sum1)  
if __name__ == "__main__":
    main()