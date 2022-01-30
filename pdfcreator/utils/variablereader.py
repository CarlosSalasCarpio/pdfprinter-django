# This function reads variables within the text input in the text area, variables are reperesented as follows. "$variable$"
def variablereader(text):

    variable = ''
    variable_list = []
    possible_variable = False

    for word in text:
        if word == '$' and possible_variable == False:
            possible_variable = True

        elif word == '$' and possible_variable == True:
            possible_variable = False
            variable_list.append(variable)
            variable = ''

        elif word != '$' and possible_variable == True:
            variable += str(word)

        else:
            possible_variable = False

    return(variable_list)

# This function modifies variables within the text input in the text area, variables are reperesented as follows. "$variable$"
def variable_modifier(text, variable_list, variable_replace):
    i = 0
    texts = []
    for i in range(3):
        text_2 = text
        for variable in variable_list:
            if variable in variable_replace.keys():
                text_2 = text_2.replace('$' + variable + '$', str(variable_replace[variable][i]))
        texts.append(text_2)
    return(texts)