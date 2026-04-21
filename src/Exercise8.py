class Exercise8:

    def input_user(self):
        pred_vvod = float('-inf')
        k = 0
        while True:
            user_in = input()
            try:
                for x in user_in:
                    if x == " ":
                        pass
                    else:
                        try:
                            user_in = int(x)
                            if pred_vvod == float('-inf'):
                                pred_vvod = user_in
                            elif user_in > pred_vvod:
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
            except ValueError:
                if pred_vvod != float('-inf'):
                    print("The sequence is ordered in ascending order")
                    return
                print("Input error")
                return


obj8 = Exercise8()
obj8.input_user()