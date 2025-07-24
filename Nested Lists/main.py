def main():
    n = int(input())
    list1 = []
    list2 = []
    for i in range(0, n):
        name = input()
        list1.append(name)
        
        value = float(input())
        list2.append(value)
    
    list3 = []
    mini = min(list2)
    
    i = 0
    m = len(list2)
    while(i < m):
        if list2[i] == mini:
            list2.pop(i)
            list1.pop(i)
            i = i-1
            m = len(list2)
        i = i+1
    
    mini = min(list2)
    i = 0
    m = len(list2)
    while i < m:
        if list2[i] == mini:
            list3.append(list1[i])
        i = i+1
    
    list3.sort()
    
    for i in range(0, len(list3)):
        print(list3[i])

if __name__ == '__main__':
    main()