import re
INPUTFILEPATH = './input3.txt'
def main():
    regex="+/d"
    with open(INPUTFILEPATH, 'r') as f:
        lines = f.read().split("\n")
    sum=0
    flag=True
    for line in lines:
        muls=re.findall(r'mul\([0-9]\d{0,2}\,[0-9]\d{0,2}\)|do\(\)|don\'t\(\)', line)
        for i in muls:
            if i=="don't()":
                flag=False
                continue
            elif i=="do()":
                flag=True
            elif flag:
                inp= re.findall(r'[0-9]\d{0,2}',i)
                sum+= int(inp[0])*int(inp[1])
        print(muls)
    print(sum)

if __name__ == "__main__":
    main()