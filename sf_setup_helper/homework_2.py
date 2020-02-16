class Star:
    def __init__(self):
        self.colors = {'blue': '#0000FF', 'white': '#FFFFFF',
                       'yellow': '#FFFF00', 'orange': '#FFA000',
                       'red': '#FF0000'}
        self.class_list = dict()

    def print_star_and_temp(self):
        data = input('Enter star & temperature separated by ":" ')
        temp = data.split(':')
        self.class_list[temp[0]] = int(temp[1])
        for key, value in self.class_list.items():
            print('Star: {}, temperature: {}'.format(key, value))

    def convert_temp_to_celsius(self):
        """ according to this image https://www.shutterstock.com/image-vector/
            temperature-conversion-vector-illustration
            -scheme-fahrenheit-1258363516"""
        for value in self.class_list.values():
            if value < 0:
                print('Your  color is : ' + self.colors.get('blue'))
            elif 0 <= self.value < 22:
                print('Your  color is : blue')
            elif value >= 22 and value < 40:
                print('Your  color is : yellow')
            elif value >= 40 and value < 49:
                print('Your  color is : orange')
            elif value >= 49 and value < 100:
                print('Your  color is : red')
            else:
                print('I do not number')




