from sys import argv
import json
import makker

ansi = {
    "white": "\033[0;37m",
    "green": "\033[0;32m",
    "yellow": "\033[0;33m",
    "red": "\033[0;31m",
}

if len(argv) != 2:
    print(ansi["red"], "Usage:\tmain.py 'file.json'")
    quit()

with open(argv[1]) as json_file:
    try:
        classes = json.load(json_file)
    except json.JSONDecodeError:
        classes = {}

while True:
    try:
        # painful formatting
        print(ansi["white"])
        action = input(
            """Action:
C = make class,
E = edit class,
G = make groups,
Q = quit
INPUT: """
        ).upper()
        if len(action) != 1:
            print(ansi["red"], "Input too long or short.")
            continue

        match action:
            case "C":
                name = input("Class name: ")
                students = []
                while True:
                    student = input("Student: ")
                    if student == "":
                        print(ansi["green"], "Class created!")
                        break
                    students.append(student)
                    classes[name] = makker.make_class(students)

            case "E":
                print("coolio")

            case "G":
                class_name = input("Class name: ")
                if class_name in classes:
                    size = int(input("Group size: "))
                    groups, student_info = makker.make_groups(size, classes[class_name])
                    classes[class_name] = student_info
                    for i in groups:
                        print(list(i))
                    break

            case "Q":
                print(ansi["yellow"], "Exiting!")
                break

            case _:
                print(ansi["red"], "Unknown command!")
                continue

        with open(argv[1], "w") as json_file:
            json.dump(classes, json_file)

    except ValueError:
        print(ansi["red"], "Value error")
    except IndexError:
        print(ansi["red"], "IndexError")
    except KeyboardInterrupt:
        print(ansi["yellow"], "\nExiting!")
        break
