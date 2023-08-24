if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        print(scores)
        student_marks[name] = scores
    query_name = input()
    print(student_marks.get(query_name))
    temp =0
    for i in student_marks.get(query_name):
        temp=temp
    print("%.2f"%(temp/3))