def input_user():
    f0 = 0
    f1 = 1
    Fn = 0
    count = 1
    while True:
        number_is_user = input()
        if number_is_user.isdigit():
            number_is_user = int(number_is_user)
            if number_is_user > 50:
                print("\tToo large n")
                return None
            if 0 <= number_is_user <= 1:
                print(number_is_user)
                return None
            my_arr = [f0, f1, Fn, number_is_user, count]
            return my_arr
        else:
            print("Could not parse a number. Please, try again")


class Exercise3:

    def recursive(self, f0, f1, Fn, number_is_user, count):
        if number_is_user > count:
            Fn = f0 + f1
            f0 = f1
            f1 = Fn
            count += 1
            self.recursive(f0, f1, Fn, number_is_user, count)
        else:
            print(Fn)


object3 = Exercise3()
arr_user_input = input_user()
if arr_user_input is not None:
    object3.recursive(*arr_user_input)
