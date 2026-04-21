
class Exercise7:


    def write_file(self, args):
        if args is None:
            return None
        try:
            with open('result.txt', 'w', encoding='utf-8') as f:
                f.write(f"{args}")
                print("Saving min and max values in file")
        except: pass


    def search_min_max(self, args):
        if args is None:
            return None
        min_number = float('inf')
        max_number = float('-inf')
        for i in range(len(args)):
            if max_number < args[i]:
                max_number = args[i]
            if min_number > args[i]:
                min_number = args[i]
        array_float = [min_number, max_number]
        array = " ".join(map(str, array_float))
        return array


    def input_user(self):
        user_input = input()
        return user_input


    def read_line_file(self, name_file):
        k = 0
        try:
            with open(name_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if k == 0:
                        n_line = line
                        k += 1
                    else:
                        array = line
        except FileNotFoundError:
            print("Input error. File doesn't exist")
            return None
        try:
            n_line = int(n_line)
            if n_line <= 0:
                print("Input error. Size <= 0")
                return None
        except ValueError:
            print("Input error. Not number")
            return None
        array2 = []
        array = list(array.split(" "))
        for i in range(len(array)):
            try:
                x = float(array[i])
                array2.append(x)
            except ValueError: pass

        if len(array2) != n_line:
            print("Input error. Insufficient number of elements")
            return None

        print(n_line)
        result = " ".join(map(str, array2))
        print(result)
        return array2


obj7 = Exercise7()
text = obj7.input_user()
array = obj7.read_line_file(text)
array2 = obj7.search_min_max(array)
obj7.write_file(array2)
