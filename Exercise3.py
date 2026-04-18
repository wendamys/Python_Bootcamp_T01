class Exercise3:

    def recursive(self, f0, f1, Fn, number_is_user, count):
        if number_is_user == "":
            new_data = self.input_user()
            self.recursive(*new_data)
            return
        if number_is_user > count:
            Fn = f0 + f1
            f0 = f1
            f1 = Fn
            count += 1
            self.recursive(f0, f1, Fn, number_is_user, count)
        else:
            print(Fn)

    def input_user(self):
        f0 = 0
        f1 = 1
        fn = 0
        count = 1
        while True:
            raw_size = input()
            try:
                value = int(raw_size)
                if value > 50:
                    print("\tToo large n")
                    return ""
                if 0 <= value <= 1:
                    print(value)
                    return ""
                my_arr = [f0, f1, fn, value, count]
                return my_arr
            except ValueError:
                print("Could not parse a number. Please, try again")
                my_arr = [f0, f1, fn, "", count]
                return my_arr


object3 = Exercise3()
arr_user_input = object3.input_user()
object3.recursive(*arr_user_input)
