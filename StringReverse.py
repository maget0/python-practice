def string_reverse(text):
    reversed = ""
    #Sets the default valur for reversed text to be empty
    for char in text:
        '''
        The for loop iterates every character in the text passed as a 
        parameter. The first letter is passed as the new value of reversed, 
        then the loop iterates with the second letter by adding it before the
        first letter; continuing until all the characters have ended
        '''
        reversed = char + reversed
    return reversed

string_reverse("Mageto")
string_reverse("Strathmore University")
string_reverse("21")