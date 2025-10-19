def total_salary(path)-> tuple:
  try:
    total = 0
    average = 0
    with open(path, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      for line in lines:
        salary = line.split(',')[1]
        total += int(salary)
      average = total / len(lines)
    return (total, average)
  except FileNotFoundError:
    print('File not found')
    return (0, 0)
  except ValueError:
    print('Incorrect data format')
    return (0, 0)

(total, average) = total_salary("files/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")