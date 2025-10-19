def total_salary(path)-> tuple:
  try:
    total = 0
    average = 0
    employee=0
    with open(path, 'r', encoding='utf-8') as file:
      for line in file:
        try:
                  lines = line.strip().split(',')
                  total += int(lines[1])
                  employee += 1
        except ValueError:
            continue  # if salary format is not float - skip the line

    average = total / employee if employee > 0 else 0
    return (total, average)

  except FileNotFoundError:
    print('File not found')
    return (0, 0)

  except ValueError:
    print('Incorrect data format')
    return (0, 0)

  except IndexError:
    print('Incorrect data format')
    return (0, 0)

(total, average) = total_salary("files/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")