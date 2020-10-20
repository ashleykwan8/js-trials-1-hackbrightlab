"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)

output_all_items([1, 'hello', 'true'])

def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums
print(get_all_evens([7,8,10,1,2,2]))

def get_odd_indices(items):
    # TODO: replace this line with your code
    results = []

    for i in range(len(items)):

        if i % 2 != 0:
            results.append(item[i])

    return results

print(get_odd_indices([1, 'hello', true, 500]))


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}.{item} ") 
        i +=1 

print_as_numbered_list([1,"hello", true])

def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    num = start

    while True:
        if num < stop:
            num += 1
            nums.append(num)
    
    return nums
            
print(get_range(0, 5))

def censor_vowels(word):
    chars = []
    for letter in word:
        if 'aeiou' in letter:
            chars.append('*')
        else:
            chars.append(letter)
    return "".join(chars)

print(censor_vowels("Hello World"))

def snake_to_camel(string):
    # TODO: replace this line with your code
    camel_case = []
    string = string.split('_')

    for word in string:
        camel_case.append(f"{word[0].title()}{word[1:].title()}")

    return "".join(camel_case)

print(snake_to_camel("hello_word"))

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
