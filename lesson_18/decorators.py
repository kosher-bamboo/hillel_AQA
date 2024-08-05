import logging

logging.basicConfig(filename='logfile.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def log_args_and_result(func):
    def wrapper(arg):
        logging.debug(f"Calling '{func.__name__}' with: {arg}")
        result = func(arg)
        logging.debug(f"'{func.__name__}' returned {result}")
        return result
    return wrapper


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def error_handler(func):
    def wrapper(arg):
        try:
            return func(arg)
        except Exception as e:
            print(f"An error occurred in '{func.__name__}' function")
    return wrapper


@error_handler
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


# the function waits for int as input, but receives str to demonstrate the operation of the error_handler decorator
if __name__ == '__main__':
    multiplication_table(3)
    multiplication_table('3')
