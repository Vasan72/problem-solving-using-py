if __name__ == '__main__':    
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    grade = [item[1] for item in student]
    
    list_grade = sorted(set(grade))
    second_score = list_grade[1]
    
    result = [item[0] for item in student if item[1] == second_score]
    result.sort() 
    
    for name in result:
        print(name)
