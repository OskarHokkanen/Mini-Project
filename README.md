# Mini-project report 

Members: Oskar Hokkanen Eriksson, Philip Khoshaba, and Ammar Shihabi  
Program: Electrical Engineering (and Interactive media and webbtechnologies)  
Course: 1DV501 
Date of submission: 2021-11-05

## Introduction  

In this project we had to work as a group to implement two different and hopefully faster algorithms to sort large files faster than the python version, which iterates through the whole file element after element. The files that have been used are the two large files that we have previously used in lab 3. One of the files called ``eng_news_100K-sentences`` had a number of nearly 2 million words, which made the normal iteration method quite inefficient to do the task quickly. That is basically what the idea of this project is.

## Part 1: Count unique words 1
The number of words in the file ``holy_grail`` was ``11106`` and the number of words in ``eng_news_100K-sentences`` was ``1949499``.
The Top-10 part of the problem was solved similar to exercise 8 from assignment 3 (``count_numbers.py``). After reading the file with the method ``read_file``, the returned list of words is used in the function ``get_top_ten``. The function creates a empty dictionary then loops trough the list of words and checks if each word's length is more than 4. If thats the case the function checks if the word is in the list. If so the count of the word is increased by 1. Otherwise the word is added to the dictionary with the value of 1.

After the words have been counted the list is sorted using the sorted function including a lambda-function and the keyword ``reverse=True``. The returned dictionary is then used in the loop to pick out the words.
#### Method get_top_ten
```python
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
```

| File                        | Unique words    |
|       :------------:        | :-------------: |
| ``holy_grail``              | ``1877``        |
| ``eng_news_100K-sentences`` | ``87545``       |

|   Top-10       | holy_grail         | eng_news_100K-sentences |
| :------------: | :-------------:    | :------------:          |
| 1              | ``arthur: 261``    | ``their: 6145``         |
| 2              | ``launcelot: 101`` | ``about: 4612``         |
| 3              | ``knight: 85``     | ``there: 4298``         |
| 4              | ``galahad: 81``    | ``would: 3884``         |
| 5              | ``father: 74``     | ``people: 3883``        |
| 6              | ``bedevere: 68``   | ``which: 3578``         |
| 7              | ``knights: 65``    | ``after: 3016``         |
| 8              | ``robin: 58``      | ``first: 2888``         |
| 9              | ``guard: 58``      | ``years: 2815``         |
| 10             | ``right: 57``      | ``other: 2757``         |

## Part 2: Implementing data structures

### Hash set
#### Method add
```python
def add(self, word):
        val = self.get_hash(word)
        if word not in self.buckets[val]:
            self.buckets[val].append(word)
            self.size += 1
        if self.size > len(self.buckets):
            self.rehash()
```
The *add*-method works as follows:
1. The method first calls the method *get_hash* (see section Hash-value for more information) which returns a hash value representing the word. 
2. After the hash-value has been returned the method checks if the values bucket does not contain the word since there should be no duplicates. 
    * If thats the case the word gets added to the bucket and the size increases by one. 
3. The method then checks if the size is more than the length of the buckets.
    * If thats the case the method calls the method *rehash* (see section Rehash for more information).

#### Hash-value
To compute the hash-value for a given word, each letter of the word is converted to its ASCII value and added to a sum. The the modulous opperator is then used to get the position in which the word should be in. The words hash-value will be different depending on how many buckets are in the hash set. 

#### Rehash
When the hash sets size is more than the amount of buckets the hash set is rehashed. The *rehash*-method adds all of the current words in the hash set in a list and changes its size to 0. It then multiplies the amount of buckets by two which doubles the size of the hash set. At last all of the words which were in the hash set gets added again and the hashing can go on.

#### Differences from ``hash_main.py``
There weren't that many differences from the output when the hash set is used. The only difference is the order in which the words are retured when using the method *to_string*. The diffrence in *to_string* is probably because either the method picks out the words from the hash set differently, or, the method *get_hash* calculates the hash-value in a different way than we are (since there are lots of ways to calculate a hash value).

#### Hash methods
| Name  | Parameters  | Description | Returns |
| :------------: | :-------------: | :------------: | :------------: |
| init            | ``None`` | Initializes HashSet  | ``None`` |
| get_hash      | ``word`` | Returns the hash-value of given word | ``Integer`` |
| rehash          | ``None`` | Doubles the amount of buckets in the HashSet | ``None`` |
| add            | ``word`` | Adds ``word`` to the HashSet | ``None``|
| to_string      | ``None`` | Returns a string representation of the HashSet | ``String`` |
| get_size        | ``None`` | Returns the size of the HashSet | ``Integer`` |
| contains        | ``word`` | Checks if given word is in the HashSet | ``True`` or ``False`` |
| bucket_list_size        | ``None`` | Returns the size of the bucket list | ``Integer`` |
| remove        | ``word`` | Removes given word if it is in the HashSet | ``None`` |
| max_bucket_size        | ``None`` | Returns the size of the largest buecket in HashSet | ``Integer`` |
### Binary Search Tree
A Binary Search Tree (BST) was created to store key-value-pairs. The BST is a ``@dataclass`` with the methods ``put``, ``to_string``, ``count``, ``get``, ``max_depth`` and ``as_list``. The methods ``put`` and ``max_depth`` are described in detail bellow. All methods are described in short in the table [bellow]( ####-Node-methods ).
Each dataset of the BST is of class Node with instances of the methods above plus the properties:
| Name  | Type  | Description | Default |
| :------------: | :-------------: | :------------:       | :------------: |
| Key            | ``Any``         | The key              | ``None``       |
| Value          | ``Any``         | The value            | ``None``       |
| Left           | ``Any``         | Left child (a Node)  | ``None``       |
| Right          | ``Any``         | Right child (a Node) | ``None``       |
#### Method put
```python
def put(self, key, value):
    if self.key is None or self.key == key:
        self.key = key
        self.value = value
    else:
        arr = [self.key, key]
        arr.sort()
        if arr.index(key) == 0:
            if self.left is None:
                m = Node(key, value)
                self.left = m
            else:
                self.left.put(key, value)
        else:
            if self.right is None:
                n = Node(key ,value)
                self.right = n
            else:
                self.right.put(key, value)
```
The *put*-method works as follows:
1. It first checks if the current Node is ``None`` or has the same key as the Node to be inserted.
    * If thats the case the Nodes key and value gets set.
2. If the first case is not true the method checks if the given key is less than the current key.
3. When left/right is determined the method checks if the left/right Node is empty
    * If The Node is empty, create a new node and insert it.
    * If the Node is not empty, the left/right *put*-method gets called and the process is done again.

#### Method max_depth
```python
def max_depth(self):
    l, r = 0, 0
    m = 0
    if self.left is not None: # Left node
        l += self.left.max_depth()
        l += 1
    if self.right is not None: # Right node
        r += self.right.max_depth()
        r += 1
    if self.right is None and self.left is None: # Last node
        m += 1
    m += l if l > r else r
    return m
```
The *max_depth*-method works as follows:
1. It first sets the left, right and max counter to 0.
2. It then checks if there is a left/right node.
    * If true the left/right *max_depth*-method is called.
    * Then the left/right counter increses by 1.
3. It then checks if the current node has no children.
    * If true the max counter increses by 1.
4. The method uses a ternary opperator to return the value of max plus left or right counter depending on which one is higher.

#### Node methods
| Name  | Parameters  | Description | Returns |
| :------------: | :-------------: | :------------: | :------------: |
| put            | ``key``, ``value`` | Adds/Replaces ``key`` in tree  | ``None`` |
| to_string      | ``None`` | Adds all the nodes ``key`` and ``value`` to a string | ``String`` |
| count          | ``None`` | Counts each node in the tree | ``Int`` |
| get            | ``Key`` | Searches tree for given ``key`` | ``Node.value`` or ``None`` |
| max_depth      | ``None`` | Searches deepest path in tree | ``Int`` |
| as_list        | ``lst`` | Converts each node to a tuple and adds it to ``lst`` | ``List[(key, value)...]`` |

## Part 3: Count unique words 2

The implementation for the top-10 part of the problem was almost the same as in part one. The method checks if the current word is more than four letters. If so, the method uses the BST's method *get* to check if the word is in the BST. If it is the word is inserted with its current value plus one. If it is not the word is inserted with the value of one.

The method also prints the max depth of the tree (See table for the result).
```python
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
```
The unique words and the top-10 count was the same as in part one. The table above is displayed for less scrolling ^^.
| File                        | Unique words    |
|       :------------:        | :-------------: |
| ``holy_grail``              | ``1877``        |
| ``eng_news_100K-sentences`` | ``87545``       |

|   Top-10       | holy_grail         | eng_news_100K-sentences |
| :------------: | :-------------:    | :------------:          |
| 1              | ``arthur: 261``    | ``their: 6145``         |
| 2              | ``launcelot: 101`` | ``about: 4612``         |
| 3              | ``knight: 85``     | ``there: 4298``         |
| 4              | ``galahad: 81``    | ``would: 3884``         |
| 5              | ``father: 74``     | ``people: 3883``        |
| 6              | ``bedevere: 68``   | ``which: 3578``         |
| 7              | ``knights: 65``    | ``after: 3016``         |
| 8              | ``robin: 58``      | ``first: 2888``         |
| 9              | ``guard: 58``      | ``years: 2815``         |
| 10             | ``right: 57``      | ``other: 2757``         |


The max bucket size for the Hash set and the max depth for the BST is displayed bellow.
| Max bucket A   |   Max bucket B  | 
| :------------: | :-------------: |
|       17       |      309        |

|   Max depth A  |   Max depth B   | 
| :------------: | :-------------: |
|       22       |        41       |
* What is the max bucket size for HashSet, and the max depth for BstMap, after having added all the words in the two large word files? (Hence, four different numbers.)


## Project conclusions and lessons learned
We did not have the time to complete the VG tasks, but we did pretty solid work implementing the BST map as well as the hashing table. Counting unique words and then sorting the top 10 most frequent words was much faster than iterating through the whole file before starting to sort and collect unique words. Which to us is a pretty solid goal.
 
Working as a group was also something pretty useful, and it was really appreciated to start working with a team so early in the education. It was also really useful to use tools such as git, that are pretty much a standard nowadays in the industry.
 
Regarding the task, we found out that the best way to attack problems based on algorithms and data structure is to find out the special cases first, and later solve the bugs that may appear there before going for the most usual case. So for instance the developer should start solving how an get_index function would do if the first node is empty before going for the normal cases that a list has elements and nodes connected to each other.


We separate technical issues from project related issues.

### Technical issues 

Technical issues are always a factor that the team should be aware of. But all in all we did not have a lot of major technical issues that affected the flow of the project. We had some minor troubles getting cloning and gitlab to work for a team member. But we solved the problem pretty quickly at the beginning.
 
The flow of the work was sometimes slower than other times, and it is mainly because some parts were trickier than others. Mainly the binary search tree, because it uses a lot of recursive calls, which makes the person writing the code think a bit more before getting things to work properly.

If we would do the project again, we would have put more time on planning. That means sketching with paper and pen before getting on the text editors and writing code. We believe that it would have made a big difference, especially with the BST map.

If we had more time to complete this project we would for sure work on the VG parts as well. It is nice to see numeric differences between how fast out implementation is compared to the normal method using iteration. It would have also been good to work with external libraries and see some plots.

### Project issues

We have done a pretty good job dividing the work from the beginning. All the members of the team got some tasks to work with, which made everyone valuable to completing the project. We were not dependent on each other, which means that you could complete your task without having to wait for someone else to complete their part. That did not mean that we worked alone and did not help each other. We were shuffling the resources every time someone has completed their task to help each other progress at the same pace. We did a meeting once every monday to plan and check what was done, and worked full-day on fridays. Our communication was mainly on Messenger. We did also communicate every time someone did a push or a merge request of a completed part.

#### Team members contributions
In the begining of the project each team member was assigned to a specific part. Oskar and Ammar started on the BST and Philip started on the Hash set. Oskar and Philip were responsible for the respective parts and Ammar worked on both of the problems (Approximetly 3 methods in BST and half of the Hash set). All of the team members sat together at times to work on the problems together, brainstorm ideas and to put all of the parts together. All in all we think we cooperated well together.
