import re
INPUT_FILE_PATH = './input5.txt'
myrules={'a':['b']}
def rec(first,vec):
    for i in vec:
        myrules[first].append(rec(i,myrules[i]))
    return myrules[first]
        
def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        rules,updates = f.read().split("\n\n")
    rules = rules.split("\n")
    updates=updates.split("\n")   
    
    for rule in rules:
        first,sec=rule.split("|")
        if first not in myrules.keys():
            myrules[first]=[sec]  
        curr=myrules[first]
        if sec not in curr:
            curr.append(sec)
            myrules[first]=curr
        print(first,":",myrules[first])
    for i in myrules:
        rec(i[0],i[1])
        
if __name__ == "__main__":
    main()