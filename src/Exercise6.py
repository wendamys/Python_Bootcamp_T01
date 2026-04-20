class SortMass:

    def sort_by_selection(self, args):
        if not args:
            return
        mass = args
        k = 0
        min_idx = k
        while k < len(mass)-1:
            for i in range(k, len(mass)):
                if mass[min_idx] > mass[i]:
                    min_idx = i
            mass[k], mass[min_idx] = mass[min_idx], mass[k]
            k += 1
            min_idx = k
        print(mass)


    def input_user(self):
        while True:
            raw_size = input()
            try:
                n_len = int(raw_size)
                if n_len <= 0:
                    print("Input error. Size <= 0")
                    return []
                my_arr = []
                user_numbers = input().split()
                for x in user_numbers:
                    try:
                        val = float(x)
                        my_arr.append(val)
                        if n_len == len(my_arr):
                            return my_arr
                    except ValueError:
                        print("Could not parse a number. Please, try again")
                return my_arr
            except ValueError:
                print("Could not parse a number. Please, try again")


obj6 = SortMass()
array = obj6.input_user()
obj6.sort_by_selection(array)


