# Write a program to check if a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward), ignoring spaces and case.

string = "Madam"
clean_string = string.replace(" ", "").lower()

is_palindrome = clean_string == clean_string[::-1]

print(is_palindrome)
