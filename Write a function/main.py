def is_leap(year) -> bool:
    if year%4 == 0:
        
        if year%100 == 0 and year%400 != 0:
            return False
    
        if year%100 == 0 and year%400 == 0:
            return True
    
        return True
    else:
        return False

def main():
    year = int(input())
    print(is_leap(year))

if __name__ == '__main__':
    main()