# This file contains some refactoring hints!
# 
# Refactoring is a process of improving the code without changing its behavior.
# It's a natural part of developing software - noticing when you can make
# the code better, clearer, or when you can remove repetitive code which
# can the source of bugs.

def move_old(dir):
    if dir == "up":
        s1.setheading(90)
        s1.forward(10)
    elif dir == "down":
        s1.setheading(270)
        s1.forward(10)
    elif dir == "left":
        s1.setheading(180)
        s1.forward(10)
    elif dir == "right":
        s1.setheading(0)
        s1.forward(10)

# COMMON CODE REFACTORING 
# 
# You can see that the code is repeated for each direction.
# We can use a function to avoid this repetition.
# 
# The function should take a direction as an argument and move the sprite in that direction.
# Now, if you want to change what happens when the sprite moves, you can change it in one place
# rather than in four places.

def move(sprite,heading):
    """Turn the sprint to the given heading and move forward 10 steps"""
    sprite.setheading(heading)
    sprite.forward(10)  

def move_new(dir):
    if dir == "up":
        move(s1,90)
    elif dir == "down":
        move(s1,270)
    elif dir == "left":
        move(s1,180)
    elif dir == "right":
        move(s1,0)  

# You can use this technique in your code in these places:
# - costume changes
# - bunny_move_ and bear_move_ functions





# DATA-BASED REFACTORING
#
# Sometimes, you can use a set of data to continue to eliminate repetitive code.
# In the example above, each direction ("up", "down", etc.) corresponds to a different
# heading.  Python has a built-in data type for this called a dictionary that can help
# you associate data.
#
# heading_dictionary = {
#     "up": 90,
#     "down": 270,
#     "left": 180,
#     "right": 0
# }
#
# You can use this dictionary to look up the heading for a given direction.
# Each "value" (e.g. 90) is associated with a "key" (e.g. "up") that you can use
# to look it up, using square brackets.
#
# heading = heading_dictionary[dir]

# First, some examples of working with dictionaries!

def working_with_dictionaries():
    # An empty dictionary!
    empty_dict = {}
    # A dictionary
    my_dict = {"apple": 1, "banana": 2, "cherry": 3}
    # Accessing a value (these are the same)
    print(my_dict["apple"])
    print(my_dict.get("apple"))
    # Adding a new key and value
    my_dict["date"] = 4
    # Changing a value
    my_dict["apple"] = 100
    # Removing a value
    del my_dict["banana"]

    # Getting all keys
    print(my_dict.keys())
    # Getting all values
    print(my_dict.values())

    # Checking if a key is in the dictionary
    print("apple" in my_dict)
    print("banana" in my_dict)

    # Getting all items
    print(my_dict.items())

    # Iterating over a dictionary
    for key, value in my_dict.items():
        # This code is called for each key/value pair in the dictionary
        print(key, value)

    # Getting the length (i.e. number of key/value pairs in a dictionary
    print(len(my_dict))

    # Clearing a dictionary
    my_dict.clear()

# Seeing all of this, we can refactor the code to use the dictionary.

heading_dictionary = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}

def move_dictionary(dir):
     heading = heading_dictionary[dir]
     move(s1,heading)

# values in dictionaries can be mostly anything you want!

def make_sprites():
    s1 = create_sprite("jelly cat bunny", -200, -190)
    s2 = create_sprite("jelly cat teddy bear", 200, -190)
    s3 = create_sprite("milk", 5, 40)
    s4 = create_sprite("frosting", 70, 30)
    sprites = {
        "bunny": s1,
        "bear": s2,
        "milk": s3,
        "frosting": s4
    }
    return sprites

# After this, the sprites_dictinoary variable will be a dictionary mapping the four
# words "bunny", "bear", "milk", and "frosting" to the four sprites.
#
sprites_dictionary = make_sprites()

# You can use this technique in your code to make the follow logic easier to understand.
# After all, only one of the "follow" variables should be true at a time.
# So, instead of follow_whisk = True, follow_milk = True, etc., you can instead
# say follow = "whisk", and use a dictionary to look up the sprite that should be followed.


# You can also use data-based approaches to make the bunny_grab and bear_grab functions easier to understand.
# Let's start with a simpler example.  Suppose I have variables a,b,c,d,e all of which are numbers
# and I want to figure out which one is closest to a number I provide called x.
#
# Here's the long-hand way to do it - we figure out if the distance from x to a is less than
# all other distances, and if so, we return a.  If not, we repeat this process for b, c, d, and e.

def closest1(a,b,c,d,e,x):
    if abs(a-x) < abs(b-x) and abs(a-x) < abs(c-x) and abs(a-x) < abs(d-x) and abs(a-x) < abs(e-x):
        return a
    elif abs(b-x) < abs(a-x) and abs(b-x) < abs(c-x) and abs(b-x) < abs(d-x) and abs(b-x) < abs(e-x):
        return b
    elif abs(c-x) < abs(a-x) and abs(c-x) < abs(b-x) and abs(c-x) < abs(d-x) and abs(c-x) < abs(e-x):
        return c
    elif abs(d-x) < abs(a-x) and abs(d-x) < abs(b-x) and abs(d-x) < abs(c-x) and abs(d-x) < abs(e-x):
        return d
    else:
        return e
    
# This repeating process is a common pattern in programming, and so is natually solved using loops and lists.

def closest2(a,b,c,d,e,x):
    arr = [a,b,c,d,e]
    # Now, which of these numbers is closest to x?
    # Start by computing all of my distances!
    distances = []
    for y in arr:
        # Append each distance to the distances list
        distances.append(abs(y-x))
    # Now, which of these is smallest?
    smallest = distances[0]
    smallest_index = 0

    # Iterate over the indexes of the distances list (i.e. 0, 1, 2, 3, 4)
    for i in range(len(distances)):
        if distances[i] < smallest:
            smallest = distances[i]
            smallest_index = i
    # Now, return the number at that index
    return arr[smallest_index]


# This is a bit more concise.  But it is also nice that it works even if we add more numbers!

# MORE ADVANCED!
#
# Python has ways of making this even more concise.  But we can cover that in a later lesson!