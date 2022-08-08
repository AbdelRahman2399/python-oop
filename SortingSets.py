def count(dict):
    colors = list(dict.values())

    for color in set(colors):
        num = colors.count(color)
        print(f'There are {num} {color} cars')







cars = {}

while True :
    car_key=input('enter car name ')
    car_val=input('enter car color ')
    cars[car_key]=car_val
    ans=input('add another? ')

    if ans == 'y':
        continue
    else:
        break


count(cars)