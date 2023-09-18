# Comma Code
# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with
# all the items separated by a comma and a space, with and inserted before the
# last item. For example, passing the previous spam list to the function would
# return 'apples, bananas, tofu, and cats'. But your function should be able to
# work with any list value passed to it. Be sure to test the case where an empty
# list [] is passed to your function.

# spam = ['apples', 'bananas', 'tofu', 'cats', 'sushi', 'katamari', 'takoyaki', 'fish balls']
spam = []


def function(list):
    # if list == None:
    #     print('please, input at least 2')
    try:
        if len(list) >= 2:
            print("'", end="")
            for i in list:
                if i != list[-1]:
                    print(i + ', ', end="")

                if i == list[-1]:
                    print('and ' + i + "'")
        else:
            print("'", end="")
            print(list[0] + "'")


    except IndexError:
        print("You need a value in your list if you want this to work'")

function(spam)



