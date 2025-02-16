def is_year_leap(year):
    if year % 4 ==0:
        return True
    else:
        return False
push = 2028
logic = str (is_year_leap(push))
print("год", push, ":", logic)