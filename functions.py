def area(radius):
    return 3.14*pow(radius,2)

def vol(area,length):
    volume = area*length
    print(f'volume is {volume}')

radius_in=int(input('enter radius '))
len_in=int(input('enter length '))

vol(area(radius_in),len_in)