## CS-UY 1114 — Lab 6
# Lists, Tuples, and Everything In Between
#### October 22th & 23th, 2020

**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab. **The points awarded by the auto-grader on GradeScope will not be counted
towards your lab's grade, so don't worry if you don't pass every or any of its tests!**

Please do not hesitate to check with your TAs if you are ever confused as to how to proceed!

---

### Congrats on getting through the first midterm!

I hope everyone was able to do their best on the midterm this week (and even if you feel like you didn't, congrats on 
surviving it anyway)! The first midterm covered a lot of the core principles of programming that give beginners trouble
(I certainly had trouble with them), and as such, making it through it is an achievement in and of itself.

From this point forward, we'll be covering concepts that start to tie programming in with more real-world problems, and 
so it will start getting more interesting (in my opinion, anyway). As always, we are on standby should you need any 
help. Don't hesitate to ask; the second midterm will come faster than you think. Good luck!

— Sebastian.

### Problem 1: Now you're doing the CS student shuffle.

We'll start with another question from pedagogical programming's great canon: the list shuffle. In the file 
[**shuffling_lists.py**](shuffling_lists.py), create two simple functions.

1. The first, **`shuffle_create`**, will accept one list parameter and return a **new list** with the same elements 
from the list that was passed in, but shuffled in any random order.
2. The second, **`shuffle_in_place`**, will accept one list parameter and shuffle its elements in-place (that is, it 
does not create a new list) in any random order.

See the sample behavior below:

```python
def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy", "Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))

    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))

    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))

    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))

main()
```
A possible output (since the behavior is pseudo-random):

```text
ORIGINAL LIST_ONE: ['Jean Valjean', 'Javert', 'Fantine', 'Cosette', 'Marius Pontmercy', 'Eponine', 'Enjolras']
LIST CREATED BY SHUFFLE_CREATE: ['Enjolras', 'Fantine', 'Jean Valjean', 'Eponine', 'Cosette', 'Javert', 'Marius Pontmercy']

ORIGINAL LIST_TWO: ['A', 0, 0, 5, 1, 3, 2]
LIST_TWO AFTER SHUFFLE_IN_PLACE: [0, 1, 2, 'A', 5, 3, 0]
```

Some explanation as to what qualifies as a "shuffle" is probably in order. For **`shuffle_create`**, it may be worth 
considering the use of **`random`** and list functions, such as **`randrange`**/**`randint`**, **`pop`**, and 
**`append`**. That is, taking elements randomly from your original list, and adding them to your new list, which of 
course starts empty.

For shuffling in place, it's worth remembering what in-place actually _means_. We're not creating a new list, but rather
editing the original list. In other words, we're replacing the element at index _**x**_ with the element at index 
_**y**_. Think about how to achieve this until none of the elements from the original list are in the same place as 
they were before.

It probably goes without saying, but you should _**not**_ use the **`shuffle`** method from the **`random`** module. If 
you do, you will not receive credit for this problem. The **`sample`** method is also not allowed. In general, if we
ask a question in a homework assignment, lab, or exam that can be solved by making one or two calls to functions that 
already belong to a module, you can assume that we want you to write them yourselves. If you're ever in doubt, please
please please ask!

### Problem 2: Nucleotide Arithmetic

_**NOTE**: The use of Python dictionaries is not allowed in this problem. At least not if you want any credit for it 
:)._

Remember our good ole friend, the DNA sequence? In this case we want to create a function **`update_frequencies`**, that 
will do just that: receive a list containing an existing list of frequencies, as well as a string representing a new 
DNA sequence, and update the previous numbers to reflect their added frequencies. That is, the following code:

```python
def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)

main()
```
will result in the following output:
```text
[('A', 22), ('C', 26), ('T', 127), ('G', 5)]
```

You may assume that the list of old frequencies will be in that exact format and ordering. Your function should be 
written in the file [**update_frequencies.py**](update_frequencies.py).

### Problem 3: Of Code And Poetry

Haiku are poems that follow a 5-7-5 syllabic structure. That is, the first line contains 5 syllables, the second 
contains 7 syllables, and the last contains 5 syllables:

> Clouds murmur darkly
>
> it is a blinding habit—
>
> gazing at the moon

— _Basho_.

The first sentence can be broken down into five syllables (`clouds` + `mur` + `mur` + `dark` + `ly` = 5 syllables), the
second sentence into 7 (`it` + `is` + `a` + `blind` + `ing` + `ha` + `bit` = 7 syllables), and the last into 5 
(`ga` + `zing` + `at` + `the` + `moon` = 5 syllables).

Write a function, **`is_haiku`**, that returns the bool **`True`** if an input string is a haiku, or the bool 
**`False`** if it is not. The function accepts one parameter, **`input_string`**, of the following format:

```python
sample_input_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
```

As you can see, syllables are separated by commas (**`,`**), and lines are separated by forward-slashes (**`/`)**. 
Notice that the final syllables of each word contain an extra space (e.g. `"clouds "`). The function **`is_haiku`** 
will return **`True`** if and only if:

1. The haiku contains 3 lines.
2. The first line contains 5 syllables.
3. The second line contains 7 syllables.
4. The third line contains 5 syllables.

Consider the sample executions below and feel free to try your own:

```python
print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "))  # prints ‘True’

print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing "))  # prints ‘False’
```

Write your function in the file [**haiku.py**](haiku.py).

**HINT**: While there are multiple ways to approach this problem, the string method **`split`** may be particularly
useful. See its official documentation [**here**](https://docs.python.org/3/library/stdtypes.html#str.split) if you 
need a refresher.

### Problem 4: Now, let's make it presentable

Write a function, **`haiku_string_parser`**, that takes in one parameter, **`input_string`**, checks if it is a haiku 
based on its structure and returns a reformatted, easy-to-read string if so:

```python
def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)

main()
```
Output:
```text
clouds murmur darkly
it is a blinding habit
gazing at the moon
```

If **`input_string`** is not a haiku based on its structure, then **`haiku_string_parser`** will simply return an empty 
string (you don’t _have_ to use the **`is_haiku`** function from problem 3 to do this, but it’d be a lot cooler if you 
did). This function should also be written inside the file [**haiku.py**](haiku.py).

**HINTS:**

- In order to create a line-break (newline) in a string, you can use the **`\n`** character.
- You might also want to consider using the **`join`** Python method. See
[**here**](https://docs.python.org/3/library/stdtypes.html#str.join).
- You may also want to keep in mind that the original, un-parsed string includes spaces after every last syllable of a word. While this space is necessary to
separate words in the same line, it should not be included in the _last word_ of each line.

### Problem 5: Matryoshka Lists

The goal of our last problem is to turn a list full of numbers into a list of ascending lists, depending on its 
contents. Here's the algorithm:

1. The program will traverse the list starting at index 0.
2. The program will create a new temporary list for every section of the original list that includes numbers in 
**ascending** order.
3. When a number is encountered that is not in ascending order compared to the number preceding it, no additional items 
will be added to the temporary list, and the temporary list will be added to a “repository” list.
4. When the program reaches the end of the original list, the “repository” list of lists will be returned to the calling
 function.

Here's an example to make this behavior clearer:

```python
def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)

    print(matryoshka_list)

main()
```

This will output:

```text
[[1, 2, 3, 5, 20], [19], [3, 4, 7, 45, 100], [1], [1, 3]]
```

Our function, **`get_matryoshka_list`**, should be written in the file [**matryoshka_list.py**](matryoshka_list.py). By 
the way, this problem is kind of difficult for this level, so don't worry if you don't manage to solve it. Here are
some hints to help you along the way:

- Keep a second, "temporary" list where you will add numbers if you find that they are in ascending order.
- To check if they are in ascending order, you need to check the number that is one index _behind_ the index you are 
currently looking at. Make sure you don't go out of bounds or into negative indexing!
- As you add numbers, check if the number at the index _ahead_ of the one you are looking at (again, making sure you 
don't go out of bounds) is higher than the one at the current index. If it is, then you know you are done with this 
particular temporary list. You can add this temporary list to your final "repository" list and create a new empty 
temporary list for the next sequence of numbers.

In case you are wondering where this nesting concept is coming from, see 
[**here**](https://en.wikipedia.org/wiki/Matryoshka_doll), though any knowledge of Russian traditional toys is not
necessary to solve this problem.

Have a good weekend!