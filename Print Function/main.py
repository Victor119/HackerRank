def custom_multiply(n):
    list1 = []
    
    i=1
    while(i<n+1):
        list1.append(i)
        i = i+1

    p = 0
    for i in range(0, len(list1)):
        if list1[i] < 10:
            p = p*10 + list1[i]
        if list1[i] > 9 and list1[i] < 100:
            p = p*100 + list1[i]
        if list1[i] > 99 and list1[i] < 151:
            p = p*1000 + list1[i]
    return p

def main():
    n = int(input())
    n = custom_multiply(n)
    print(n)

if __name__ == '__main__':
    main()