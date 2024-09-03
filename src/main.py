import time as _time


def main() -> None:
    while True:
        try:
            # !Get numbers
            num_one = int(input("First number: "))
            num_two = int(input("Second number: "))

            while True:
                # !Get calculation method
                print("Commands:")
                print(f"Addition(add or plus): {num_one} + {num_two}")
                print(f"Subtraction(subtract or minus): {num_one} - {num_two}")
                print(f"Multiplication(multiply or times): {num_one} * {num_two}")
                print(f"Division(divide): {num_one} / {num_two}")
                print(f"Exponentiation: {num_one} to the power of {num_two}")
                print("Exit")
                print()
                print("Commands are not case sensitive")

                command = input("Command: ").lower()

                # !Process input
                if command in ("addition", "add", "plus"):
                    print(num_one + num_two)
                elif command in ("subtraction", "subtract", "minus"):
                    print(num_one - num_two)
                elif command in ("multiplication", "multiply", "times"):
                    print(num_one * num_two)
                elif command in ("division", "divide"):
                    print(num_one / num_two)
                elif command == "exponentiation":
                    print(num_one**num_two)
                elif not command == "exit":
                    print("Invalid command")
                    _time.sleep(2)
                    continue
                break

            if command == "exit":
                break
        except ValueError:
            print("Enter a valid integer")
        except KeyboardInterrupt:
            break
