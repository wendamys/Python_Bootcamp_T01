class Exercise8:

    def input_user(self):
        pred_vvod = float('-inf')
        k = 0
        while True:
            user_in = input().split()
            try:
                for x in user_in:
                    if x == " ":
                        pass
                    else:
                        user_in = int(x)
                        if user_in > pred_vvod:
                            pred_vvod = user_in
                        else:
                            print(f"The sequence is not ordered from the ordinal number of the number {k}")
                            return
                        k += 1
            except ValueError:
                if pred_vvod != float('-inf'):
                    print("The sequence is ordered in ascending order")
                    return
                print("Input error")
                return


obj8 = Exercise8()
obj8.input_user()