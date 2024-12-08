import re
INPUT_FILE_PATH = './input5.txt'
myrules={}
        
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        rules,updates = f.read().split("\n\n")
    rules = rules.split("\n")
    updates=updates.split("\n")   
    for rule in rules:
        first,sec=rule.split("|")
        if first not in myrules.keys():
            myrules[first] = {sec}
        else:
            myrules[first].add(sec)
    
    sum=0
    for update in updates:
        update=update.split(",")
        flag=True
        for i in range(1,len(update)):
            if update[i-1] in myrules.keys() and update[i] in myrules[update[i-1]]:
                continue
            flag=False
        if flag:
            sum+=int(update[int(len(update)/2)])
    print(sum)
        
if __name__ == "__main__":
    main()