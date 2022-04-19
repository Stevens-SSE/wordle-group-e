import HW06_Shreya_Mohan_utility as util


class Info:

    def __init__(self):
        self.utils = util.Utility()

    def __str__(self):
        return f'Info: ({self.utils})'

# accepts user input with input validations
    def user(self, attempts, prev, all_words):
        try:
            try:
                wordle = input(
                    f"Attempt #{7-attempts}\nEnter a 5 letter word \n")
            except Exception as e:
                self.utils.write_logs(f"ERROR : INPUT ERROR {e}", True)
            self.utils.write_logs(f'USER ENTERED: "{wordle.upper()}"')
            if not wordle:
                print("Thank you for playing, exiting game now")
                self.utils.write_logs(f"USER EXITED THE GAME")
                quit()
            # to convert all input to upper case
            wordle = wordle.upper()
            # to check if the input is not of length 5 and is not consisting of only alphabets
            if len(wordle) != 5 or not wordle.isalpha():
                self.utils.write_logs(
                    f"ERROR : USER ENTERED AN INVALID WORD", True)
                return False, "Please enter a valid 5 letter word consisting of only alphabets."
            # to check if the input is in dictionary
            if wordle.upper() not in all_words:
                self.utils.write_logs(
                    f"ERROR : USER ENTERED A WORD WHICH IS NOT IN THE DICTIONARY", True)
                return False, "Word is not in dictionary"
            # to check if the input has already been entered
            if wordle in prev:
                self.utils.write_logs(
                    f"ERROR : USER ENTERED A USED WORD", True)
                return False, "You have already entered this word."
            # to check if the input is of length 5 and is consisting of only alphabets
            if len(wordle) == 5 and wordle not in prev and wordle.isalpha():
                return True, wordle.upper()
        except Exception as e:
            print(f"Error: {e}")

# function for automation of wordle game using helper function
    def automatic_attempts(self, attempts, wordle):
        self.utils.write_logs(f'USER ENTERED: "{wordle.upper()}"')
        if not wordle:
            print("Thank you for playing, exiting game now")
            self.utils.write_logs(f"USER EXITED THE GAME")
            quit()
        # to convert all input to upper case
        wordle = wordle.upper()
        # to check if the input is not of length 5 and is not consisting of only alphabets
        if len(wordle) != 5 or not wordle.isalpha():
            self.utils.write_logs(
                f"ERROR : USER ENTERED AN INVALID WORD", True)
            return False, "Please enter a valid 5 letter word consisting of only alphabets."
        # to check if the input is of length 5 and is consisting of only alphabets
        if len(wordle) == 5 and wordle.isalpha():
            return True, wordle.upper()
