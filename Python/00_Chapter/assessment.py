# First Assessment :: Write a program to print Twinkle twinkle little star poem in python.

poem = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.'''

print(poem)

# Second Assessment :: Use REPL and print the table of 5 using it. 

for i in range(1, 11):print(f"5 x {i} = {5 * i}")

# Third Assessment :: Install an external module and use it to perform an operation of your interest. 

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Ganda")
engine.runAndWait()

# fourth Assessment :: Write a python program to print the contents of a directory using the os module. Search online for the function which does that

import os
directory_path = '.'
contents = os.listdir(directory_path)

for item in contents:
    print(item)


# fifth Assessment :: Label the program written in problem 4 with comments. 

import os
directory_path = '.'
print("Contents of the directory:")
contents = os.listdir(directory_path)

for item in contents:
    print(item)