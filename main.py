# Imports
import part_one as p1
import code_skeletons.BstMap as bst
import code_skeletons.HashSet as hset


# Get the number of unique words
# from file a and b using implementations
# from part 1.
def get_set_uniqe_words(a, b):
    a = p1.get_unique_words(a)
    b = p1.get_unique_words(b)
    return (len(a), len(b))


# Get the top 10 most frequent words
# from file a and b using implementations
# from part 1.
def get_dct_top_ten(a, b):
    a = p1.get_top_ten(a)
    b = p1.get_top_ten(b)
    return a, b


# Get the most frequent words using the BST.
# The function returns the top 10
# most frequent words in file a and b.
def get_bst_top_ten(a, b):
    map_a = bst.BstMap()
    map_b = bst.BstMap()
    for w in a:
        if len(w) > 4:
            val = map_a.get(w)
            if val is None:
                map_a.put(w, 1)
            else:
                map_a.put(w, val + 1)
    lst_a = map_a.as_list()
    lst_a.sort(key=lambda x: x[1])
    lst_a = lst_a[::-1]
    for w in b:
        if len(w) > 4:
            val = map_b.get(w)
            if val is None:
                map_b.put(w, 1)
            else:
                map_b.put(w, val + 1)
    lst_b = map_b.as_list()
    lst_b.sort(key=lambda y: y[1])
    lst_b = lst_b[::-1]

    # Print the max depth from file a and b.
    a = map_a.max_depth()
    b = map_b.max_depth()
    print("Max depth file_a: {a}, file_b {b} \n".format(a=a, b=b))
    return lst_a[0:10], lst_b[0:10]


# Uses the hashset to get the unique word count.
# The function returns the count of unique words
# from file a and b.
def get_hash_uniqe_words(a, b):
    words_a = hset.HashSet()
    words_b = hset.HashSet()
    words_a.init()
    words_b.init()
    for w in a:
        words_a.add(w)
    for w in b:
        words_b.add(w)

    # Get max bucket size
    a = words_a.max_bucket_size()
    b = words_b.max_bucket_size()
    print("Max bucket file_a: {a}, file_b: {b} \n".format(a=a, b=b))
    return words_a.get_size(), words_b.get_size()


# Program starts
# Read the files
file_a = p1.read_file("./textfiles/output_11106_words.txt")
file_b = p1.read_file("./textfiles/output_1949499_words.txt")
print("Printing unique words...\n", get_set_uniqe_words(file_a, file_b), "\n")
print("Printing top 10...\n", get_dct_top_ten(file_a, file_b), "\n")
print("Printing top 10 using BST...\n", get_bst_top_ten(file_a, file_b), "\n")
print("Printing unique words using Hash set...\n", get_hash_uniqe_words(
    file_a, file_b), "")
