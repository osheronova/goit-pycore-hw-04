def get_cats_info(path: str) -> list:
    cats = []
    count=0 # corrupted lines count
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cats.append({
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    })
                else:
                    count+=1  
    except FileNotFoundError:
        print("File not found")
    if count>0:
        print(f"!!! Skipped {count} corrupted line(s)!!!")
    return cats


cats_info = get_cats_info("files/cats.txt")
print(cats_info)
