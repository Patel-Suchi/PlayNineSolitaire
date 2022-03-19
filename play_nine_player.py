# An example player agent for the Play Nine Solitaire project. This version doesn't
# make any decisions on its own, but asks the human to provide the decisions via
# console input.

# Version December 6, 2021, Ilkka Kokkarinen

# The three functions to implement begin here:
# --------------------------------------------

# Returns a tuple of two strings, the name and the student ID of the author.

def get_author_info():
    return "Suchi Patel", "500922373"


# Choose the drawing action for the current draw. The return value of this function
# must be either string "k" or "d" for taking the known card from the kitty and for
# drawing a random card from the deck, respectively.

def choose_drawing_action(top_concealed, bottom_concealed, draws_left, kitty_card):
    if kitty_card in top_concealed:
        index = get_index(top_concealed, kitty_card)
        for i in index:
            if bottom_concealed[i] != kitty_card:
                action = "k"
                return action
    if kitty_card in bottom_concealed:
        index = get_index(bottom_concealed, kitty_card)
        for i in index:
            if top_concealed[i] != kitty_card:
                action = "k"
                return action

    if kitty_card < 0:
        action = "k"
    elif draws_left < 3 and kitty_card == 0:
        action = "k"
    else:
        action = "d"
    return action


# Choose the replacement action for the current card. The return value of this function
# must be a triple of the form (action, row, column) where
# - action is one of the characters "rRtT", "r" for replace and "t" for turn over
# - row is the row number of the card subject to chosen action
# - column is the column number of the card subject to chosen action

def choose_replacement_action(top_concealed, bottom_concealed, draws_left, current_card):
    if current_card in top_concealed:
        index = get_index(top_concealed, current_card)
        row = 1
        for i in index:
            if bottom_concealed[i] == '*' or ((top_concealed[i] + bottom_concealed[i] > 0)
                                              and (top_concealed[i] != bottom_concealed[i])):
                action = 'r'
                column = i
                return action, row, column

    if current_card in bottom_concealed:
        index = get_index(bottom_concealed, current_card)
        row = 0
        for i in index:
            if top_concealed[i] == '*' or ((top_concealed[i] + bottom_concealed[i] > 0)
                                           and (top_concealed[i] != bottom_concealed[i])):
                action = 'r'
                column = i
                return action, row, column

    if current_card <= 0:
        (a, b) = get_max(top_concealed, bottom_concealed)
        row = a
        column = b
        action = 'r'
    else:
        action = 't'
        (a, b) = turn_card(top_concealed, bottom_concealed)
        row = a
        column = b



    return action, row, column


def turn_card(top_concealed, bottom_concealed):
    if '*' in top_concealed:
        index = get_index(top_concealed, '*')
        for i in index:
            if bottom_concealed[i] != '*':
                a = 0
                b = i
                return a, b
    if '*' in bottom_concealed:
        index = get_index(bottom_concealed, '*')
        for i in index:
            if top_concealed[i] != '*':
                a = 1
                b = i
                return a, b

    if '*' in top_concealed:
        a = 0
        b = top_concealed.index('*')
        return a, b
    else:
        a = 1
        b = bottom_concealed.index('*')
        return a, b


def get_index(index_list, element):
    index = []
    for i in range(len(index_list)):
        if index_list[i] == element:
            index.append(i)
    return index


def get_max(top_concealed, bottom_concealed):
    max_num = -6
    for i in range(len(top_concealed)):
        if top_concealed[i] != '*' and top_concealed[i] > max_num and top_concealed[i] != bottom_concealed[i]:
            max_num = top_concealed[i]
            row = 0
            column = i

    for i in range(len(bottom_concealed)):
        if bottom_concealed[i] != '*' and bottom_concealed[i] > max_num and top_concealed[i] != bottom_concealed[i]:
            max_num = bottom_concealed[i]
            row = 1
            column = i

    if max_num == -6:
        if '*' in top_concealed:
            row = 0
            column = top_concealed.index('*')
            return row, column
        else:
            row = 1
            column = bottom_concealed.index('*')
            return row, column
    return row, column


