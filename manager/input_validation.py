import re
import datetime
from datetime import datetime

class InputValidator:
    
    @staticmethod
    def get_string_input(prompt, error_message="Invalid input. Please enter valid text."):
        while True:
            user_input = input(prompt)
            if user_input.isalpha() or all(x.isspace() for x in user_input): 
                return user_input
            else:
                print(error_message)

    @staticmethod
    def get_float_input(prompt, min_value=None, max_value=None, error_message="Invalid input. Please enter a valid number."):
        while True:
            try:
                user_input = float(input(prompt))
                if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                    print(f"Input must be between {min_value} and {max_value}.")
                else:
                    return user_input
            except ValueError:
                print(error_message)

    @staticmethod
    def get_int_input(prompt, min_value=None, max_value=None, error_message="Invalid input. Please enter a valid integer."):
        while True:
            try:
                user_input = int(input(prompt))
                if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                    print(f"Input must be between {min_value} and {max_value}.")
                else:
                    return user_input
            except ValueError:
                print(error_message)

    @staticmethod
    def get_date_input(prompt, error_message="Invalid date format. Please enter date in YYYY-MM-DD format."):
        while True:
            user_input = input(prompt)
            if re.match(r"\d{4}-\d{2}-\d{2}", user_input):
                try:
                    input_date = datetime.strptime(user_input, "%Y-%m-%d")
                    today_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    
                    if input_date > today_date:
                        print("The date cannot be in the future. Please enter a valid date.")
                    else:
                        return user_input
                except ValueError:
                    print("The date doesn't exist. Please enter a valid date.")
            else:
                print(error_message)