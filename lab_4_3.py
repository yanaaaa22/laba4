def magic(day, month, year):
    return day * month == year % 100
day, month, year = map(int, input().split())
print(magic(day, month, year))