class Exercise4:

    def input_user(self):
        while True:
            raw_size = input()
            try:
                n_len = int(raw_size)
                if n_len <= 0:
                    print("Input error. Size <= 0")
                    return []
                my_array = []
                while len(my_array) < n_len:
                    val = input()
                    try:
                        num = int(val)
                        my_array.append(num)
                    except ValueError:
                        print("Could not parse a number. Please, try again")
                return my_array
            except ValueError:
                print("Could not parse a number. Please, try again")

    def find_mean_negative_numbers(self, arr):
        if not arr:
            return
        negative_sum = 0
        negative_count = 0
        for x in arr:
            if x < 0:
                negative_sum += x
                negative_count += 1
        if negative_count > 0:
            print(negative_sum / negative_count)
        else:
            print("There are no negative elements")


obj4 = Exercise4()
arr_user = obj4.input_user()
obj4.find_mean_negative_numbers(arr_user)
