import re
INPUT_FILE_PATH = './input1.txt'
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    list1=[]
    list2=[]
    freq = {}
    
    for line in lines:
        word=line.split("   ")
        list1.append(int(word[0]))
        list2.append(int(word[1]))
    

    for item in list2:
        if (item in freq):
            freq[item] += item
        else:
            freq[item] = item
    sum1=0      
    for item in list1:
        if (item in freq):
            sum1+=freq[item]
        else:
            sum1+=0
    print(sum1)
if __name__ == "__main__":
    main()