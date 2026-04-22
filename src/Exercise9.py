class Exercise9:

    def input_user(self):
        raw_size = int(input())
        items = []
        for i in range(raw_size):
            items.append(input())
        user_filter = input()
        array_args = [items, user_filter]
        return array_args

    def filter_and_print(self, args, query):
        filtered_list = [x for x in args if query in x]
        result = ", ".join(filtered_list)
        print(result)


obj9 = Exercise9()
array = obj9.input_user()
obj9.filter_and_print(*array)