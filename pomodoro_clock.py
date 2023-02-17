from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

print("-------------------------")
print("Welcome The CLI-Pomodoro!")
print("-------------------------")


def get_pomodoro_length():
    while True:
        print("Please Choose A Length For Your Pomodoros:")
        print("")
        print("A. 25 Minutes")
        print("B. 40 Minutes")
        print("C. 50 Minutes")
        print("")

        user_pomodoro_length_input = input("Type A, B or C: ")

        if user_pomodoro_length_input == "A":
            return 25 * 60
        elif user_pomodoro_length_input == "B":
            return 40 * 60
        elif user_pomodoro_length_input == "C":
            return 50 * 60
        else:
            print("\033[91m" + "Invalid input. Please choose A, B or C." + "\033[0m")
            print("-------------------------")


def get_break_length():
    while True:
        print("-------------------------")
        print("Please Choose A Length For Your Breaks:")
        print("")
        print("A. 5 Minutes")
        print("B. 10 Minutes")
        print("C. 15 Minutes")
        print("")
        user_break_length_input = input("Type A, B or C: ")

        if user_break_length_input == "A":
            return 5 * 60
        elif user_break_length_input == "B":
            return 10 * 60
        elif user_break_length_input == "C":
            return 15 * 60
        else:
            print("\033[91m" + "Invalid input. Please choose A, B or C." + "\033[0m")


while True:
    time_elapsed = 0
    user_pomodoro_length = get_pomodoro_length()
    user_break_length = get_break_length()

    print(CLEAR)
    while time_elapsed < user_pomodoro_length:
        time.sleep(1)
        time_elapsed += 1

        time_left = user_pomodoro_length - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Pomodoro will end in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < user_break_length:
        time.sleep(1)
        time_elapsed += 1

        time_left = user_break_length - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Break will end in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")
