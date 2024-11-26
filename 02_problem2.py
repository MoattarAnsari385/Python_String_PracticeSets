# Write a program to fill in a letter template given below woth name and date.

letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|> '''

print(letter.replace("<|Name|>", "Moattar Ansari").replace("<|Date|>", "12 - 11 - 2024"))