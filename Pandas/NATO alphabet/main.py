# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

woed = input("Enter the word : ").upper()
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# to check what iterrows method does 
# for i in df.iterrows():
#     print(i)

nato_d = {r.letter:r.code for i, r in df.iterrows()}
# nato_d = {i:r for (i, r) in df.iterrows()}
# print(nato_d)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
l = [nato_d[i] for i in woed ]
print(l)