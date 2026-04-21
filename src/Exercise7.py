class Exercise7:

    def search_min_max(self, *args):
        if args is None:
            return None
        list_min_max = [min(args), max(args)]
        return list_min_max

    def input_user(self):
        return input()

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
        if n_line is None:
            print("Input error. File is empty")
            return
        if int(n_line) <= 0:
            print("Input error. Size <= 0")

        print(n_line)
        print(array)




obj7 = Exercise7()
text = obj7.input_user()
obj7.read_line_file(text)
