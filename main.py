import re
import os
import sys

if not os.path.exists("your_text.txt"):
    with open("your_text.txt","w") as f:
        f.write("")
    print("I have created a 'your_text.txt' file. Place your text in there separated by newlines.")
    sys.exit()
elif os.stat("your_text.txt").st_size == 0:
    print("'your_text.txt' file is empty. Please paste something in it.")
    sys.exit()
with open("your_text.txt") as f:
    text = f.read()
lines = [i.split(" ") for i in text.split("\n")]
fixed_lines = [' '.join([re.sub(r"(?<!^)\w","_",word) for word in line]) for line in lines]
final = [f"{hidden}\t{normal}" for normal, hidden in zip(text.split("\n"),fixed_lines)]    
with open("final.txt","w",encoding="utf-8") as f:
    f.write("\n".join(final))
print("'final.txt' created! Import this to Anki.")    