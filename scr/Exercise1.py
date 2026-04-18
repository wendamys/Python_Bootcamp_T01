import math

class Perimeter:

    def calc_the_perimeter_of_triangle(self, *myArray):

        a = math.sqrt(math.pow(myArray[2] - myArray[0], 2) + math.pow(myArray[3] - myArray[1], 2))
        b = math.sqrt(math.pow(myArray[4] - myArray[0], 2) + math.pow(myArray[5] - myArray[1], 2))
        c = math.sqrt(math.pow(myArray[4] - myArray[2], 2) + math.pow(myArray[5] - myArray[3], 2))

        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
            Perimetr = a + b + c
            return Perimetr
        else: return None

    def user_input(self):
        myArray = []
        i = 0
        while i < 6:
            numbers = input()
            try:
                val = float(numbers)
                myArray.append(val)
                i += 1
            except ValueError:
                print("Could not parse a number. Please, try again")
        return myArray

    def print_result_calc_the_perimeter(self, perimetr):
        if perimetr is not None:
            return print(f'Perimeter: {perimetr:.3f}')
        return print("It's not a triangle")


object1 = Perimeter()
array = object1.user_input()
perimetr = object1.calc_the_perimeter_of_triangle(*array)
object1.print_result_calc_the_perimeter(perimetr)
