from User import User


class Exercise10:

    def input_users(self):
        while True:
            try:
                number_users = input()
                number_users = int(number_users)
                break
            except ValueError:
                print("Could not parse a number. Please, try again")

        users_list = []
        while len(users_list) < number_users:
            name = input()
            try:
                age = int(input())
                if age <= 0:
                    print("Incorrect input. Age <= 0")
                    continue
                users_list.append(User(name, age))
            except ValueError:
                print("Could not parse a number. Please, try again")

        return users_list

    def filter_and_print(self, users):
        adult_name = [u.name for u in users if u.age >= 18]
        print(", ".join(adult_name))


obj10 = Exercise10()
array = obj10.input_users()
obj10.filter_and_print(array)

