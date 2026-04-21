class SortMass:

    def sort_by_selection(self, args):
        if not args:
            return
        k = 0
        min_idx = k
        while k < len(args)-1:
            for i in range(k, len(args)):
                if args[min_idx] > args[i]:
                    min_idx = i
            args[k], args[min_idx] = args[min_idx], args[k]
            k += 1
            min_idx = k
        return args


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


    def print_by_mass(self, args):
        print(args)


obj6 = SortMass()
array = obj6.input_user()
sorted_mass = obj6.sort_by_selection(array)
obj6.print_by_mass(sorted_mass)

