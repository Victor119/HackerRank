def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    list1 = student_marks[query_name]
    
    
    median = 0
    total = 0
    for i in range(0, len(list1)):
        median = median + list1[i]
        total = total + 1
    
    median = median/total
    print("{:.2f}".format(median))

if __name__ == '__main__':
    main()