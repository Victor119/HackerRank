def weird(value):
    if value % 2 == 1:
        return "Weird"
    
    if value % 2 == 0 and value>=2 and value<=5:
        return "Not Weird"

    if value % 2 == 0 and value>=6 and value<=20:
        return "Weird"
    
    if value % 2 == 0 and value>=20:
        return "Not Weird"

def main():
    n = int(input().strip())
    
    print(weird(n))

if __name__ == '__main__':
    main()