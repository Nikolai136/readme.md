
def month_to_season(numbers):
    if numbers == 12 or numbers == 1 or numbers == 2:
        print("Зима")
    elif numbers >=3 and numbers <=5:
        print("Весна")
    elif numbers >=6 and numbers <=8:
        print("Лето")
    elif numbers >=9 and numbers <=11:
        print("Осень")
    
month_to_season(13)