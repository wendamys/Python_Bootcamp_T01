class Time:

    def user_input(self):
        while True:
            user_input = input()
            try:
                seconds = int(user_input)
                if seconds >= 0:
                    return seconds
                print("Incorrect time")
                return None
            except ValueError:
                print("Could not parse a number. Please, try again")

    def search_time_hh_mm_ss(self, seconds):
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        Array = [hour, minutes, seconds]
        return Array

    def print_time(self, Array):
        print(f"{Array[0]:02}:{Array[1]:02}:{Array[2]:02}")


Time_obj = Time()
second = Time_obj.user_input()
if second is not None:
    myArray = Time_obj.search_time_hh_mm_ss(second)
    Time_obj.print_time(myArray)
