def pascal_triangle(n):  
    result  = []
    for line in range(1, n + 1):  
        num = 1
        section = []
        for i in range(1, line + 1):  
            section.append(num);
            num = int(num * (line - i) / i)
        result.append(section);
    return result
  

n = int(input('this will give you the pascal triangle to the number you have chosen: '))
result = pascal_triangle(n)

for line in result:
    print(line)