class Exercise5:

    def det_number_whose_first_and_last_match(self, *args):
        result = []
        for num in args[0]:
            s = str(abs(num))
            if s[0] == s[-1]:
                result.append(num)
        if result:
            for x in result:
                print(x, end=' ')
        else:
            print("There are no such elements")

    def input_user(self):
        my_arr = []
        while True:
            val = input()
            try:
                n_len = int(val)
                if n_len <= 0:
                    print("Input error. Size <= 0")
                user_numbers = input().split()
                for x in user_numbers:
                    try:
                        val = int(x)
                        my_arr.append(val)
                        if n_len == len(my_arr):
                            return my_arr
                    except ValueError:
                        print("Could not parse a number. Please, try again")
                        my_arr = []
            except ValueError:
                print("Could not parse a number. Please, try again")


obj5 = Exercise5()
test = obj5.input_user()
obj5.det_number_whose_first_and_last_match(test)
