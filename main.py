from morse import string_to_morse

# USER INPUT
text_input = input("What word/sentence would you like to be translated to Morse?: ")

# TRANSLATE TO MORSE
morse_output = string_to_morse(text_input)

# TURN TRANSLATED (LIST) TO STRING
listToStr = ' '.join([str(element) for element in morse_output])

# OUTPUT
print(listToStr)



