from User import User


class Exercise10(User):

    def input_user(self):
        number_users = input()
        user_obj_items = []
        try:
            number_users = int(number_users)
            i = 0
            while number_users > i:
                name_user_input = input()
                age_user_input = int(input())
                if age_user_input > 0:
                    user_obj_items.append(User(name_user_input, age_user_input))
                    i += 1
                else:
                    print("Incorrect input. Age <= 0")
        except ValueError:
            print("Could not parse a number. Please, try again")
            return None
        return user_obj_items

    def adult_obj_and_print(self, args):
        items_user_name = []
        for user in args:
            if user.age >= 18:
                items_user_name.append(user.name)
        result = ", ".join(items_user_name)
        print(result)





obj10 = Exercise10()
array = obj10.input_user()
obj10.adult_obj_and_print(array)

