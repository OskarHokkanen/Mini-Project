# Reads a file and returns a list of words
def read_file(path):
    with open(path, 'r') as file:
        for row in file:
            lst = row.split(" ")
    return lst


# Uses set to get the amount of unique words in a list
# Returns a set of words
def get_unique_words(lst):
    st = set()
    for w in lst:
        st.add(w)
    return st


# Uses a dictionary to add
def get_top_ten(lst):
    dct = {}
    for w in lst:
        if len(w) > 4:
            if w in dct:
                dct[w] += 1
            else:
                dct[w] = 1
    dct = sorted(dct.items(), key=lambda tpl: tpl[1], reverse=True)
    temp = {}
    for i in range(10):
        temp[dct[i][0]] = dct[i][1]
    dct = temp
    return dct
