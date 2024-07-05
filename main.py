import string
import tkinter as tk


def is_hebrew(char):
    return 'א' <= char <= 'ת' or char == ' ' or '0' <= char <= '9' or char in string.punctuation


def is_english(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ' or '0' <= char <= '9' or char in string.punctuation


def move_spaces(s):
    if not s:
        return s

    num_start_spaces = 0
    num_end_spaces = 0

    # Count leading spaces
    for char in s:
        if char == " ":
            num_start_spaces += 1
        else:
            break

    # Count trailing spaces
    for char in s[::-1]:
        if char == " ":
            num_end_spaces += 1
        else:
            break

    # Construct the modified string
    return " " * num_end_spaces + s.strip() + " " * num_start_spaces


def hebrew_reshaper(text):
    sub_texts = text.split('\n')
    new_strings = []
    for text in sub_texts:
        last_string_puncs = ''
        while text[-1] in string.punctuation:
            last_string_puncs += text[-1]
            text = text[:-1]

        breaks = []
        is_current_hebrew = is_hebrew(text[0])
        current_text = ''

        for char in text:
            if is_current_hebrew:
                if is_hebrew(char):
                    current_text += char
                else:
                    breaks.append((current_text, is_current_hebrew))
                    current_text = char
                    is_current_hebrew = False
            else:
                if is_english(char):
                    current_text += char
                else:
                    breaks.append((current_text, is_current_hebrew))
                    current_text = char
                    is_current_hebrew = True
        breaks.append((current_text, is_current_hebrew))
        breaks = breaks[::-1]

        for i in range(len(breaks)):
            part, is_heb = breaks[i]
            part = move_spaces(part)
            breaks[i] = (part, is_heb)
        new_string = ''.join([part for part, _ in breaks])

        if len(breaks) > 1:
            new_string = last_string_puncs + new_string
        else:
            new_string += last_string_puncs
        new_strings.append(new_string)
    return '\n'.join(new_strings)


def main():
    root = tk.Tk()
    root.title("Hebrew Reshaper")
    text = 'זה משפט WITH ENGLISH ועברית TOGETHER!'
    text = hebrew_reshaper(text)
    # Create a Label widget to display the reshaped text
    label = tk.Label(root, text=text, font=("Arial", 14))
    label.pack(fill=tk.BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
