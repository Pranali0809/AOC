import re
INPUT_FILE_PATH = './input3.txt'
def main():
    regex="+/d"
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    sum=0;
    for line in lines:
        # print(line)
        muls=re.findall(r'mul\([0-9]\d{0,2},[0-9]\d{0,2}\)',line)
        print(muls)
        for mul in muls:
            digits=re.findall(r'[0-9]\d{0,2}',mul)
            sum+=int(digits[0])*int(digits[1])
    print(sum)
if __name__ == "__main__":
    main()