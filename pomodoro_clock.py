from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

print("-------------------------")
print("Welcome The CLI-Pomodoro!")
print("-------------------------")
print("Please Choose A Length For Your Pomodoros:")
print("")
print("A. 25 Minutes")
print("B. 40 Minutes")
print("C. 50 Minutes")
print("")
user_pomodoro_length_input = input("Type A, B or C: ")
print("-------------------------")
print("Please Choose A Length For Your Breaks:")
print("")
print("A. 5 Minutes")
print("B. 10 Minutes")
print("C. 15 Minutes")
print("")
user_break_length_input = input("Type A, B or C: ")


if user_pomodoro_length_input == "A":
    user_pomodoro_length = 25 * 60
elif user_pomodoro_length_input == "B":
    user_pomodoro_length = 40 * 60
elif user_pomodoro_length_input == "C":
    user_pomodoro_length = 50 * 60
else:
    print("Invalid input. Please choose A, B or C.")

if user_break_length_input == "A":
    user_break_length = 5 * 60
elif user_break_length_input == "B":
    user_break_length = 10 * 60
elif user_break_length_input == "C":
    user_break_length = 15 * 60
else:
    print("Invalid input. Please choose A, B or C.")

while True:
    time_elapsed = 0

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
