# A Text to Morse Code Converter Project

# Notes:
# This Morse code make use of the basic morse code charts which contains 26 alphabets and 10 numerals
# No special characters are currently involved. But can be added in the '.txt ' file based on the requirement.

MORSE_CODE_CHART = "script_texts.txt"


def load_chart():
    """Loads contents of the text file from the directory and returns the output as a Dictionary."""
    with open(file=MORSE_CODE_CHART, mode="r", encoding="utf-8") as file:
        # using dictionary comprehension
        mc_dict = {line.split(" ")[0]: line.split(" ")[1].strip("\n") for line in file.readlines()}
        return mc_dict


def take_user_input():
    """Takes an input from the user and returns it as a STR."""
    while True:
        print("Please enter the text you want to convert:")
        raw_input = input("> ").lower()

        # make sure something was entered
        if raw_input == "":
            print("Please enter some text.")
        else:
            return raw_input


def main():
    # load the chart into a dict
    morse_chart = load_chart()
    print("Welcome to the Morse code converter.\n")

    while True:
        # get input from the user
        input_text = take_user_input()
        converted_text = ""

        # process characters
        for char in input_text:
            # only add valid convertible characters, ignore everything else
            if char in morse_chart:
                # adding a single space after each character for visibility
                converted_text += morse_chart[char] + " "

        # check for empty output
        if len(converted_text) > 0:
            print(f"Your input in morse code: {converted_text}")
        else:
            print("The input did not contain any convertible character.")

        # asking the user for a condition to break out of the loop
        print("Do you want to convert something else? (y/n)")
        if input("> ").lower() == "n":
            break

    print("Goodbye.")


if __name__ == "__main__":
    main()