def main():
    n = int(input())
    list1 = list(map(int, input().split()))
    
    maxi = max(list1)
    #print(maxi)
    
    i = 0
    m = len(list1)
    while(i < m):
        if list1[i] == maxi:
            list1.pop(i)
            i = i-1
            m = len(list1)
        i = i+1
    
    maxi = max(list1)
    print(maxi)
    
if __name__ == '__main__':
    main()