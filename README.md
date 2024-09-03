# bookbot
"Book Bot" - A simple python program that can analyze an entire book or .txt file and print out an interesting stat report.

## The Why

This project is to showcase how to read data from a file and traverse its content and grab necessary/specific pieces.

## The How

To start, we read data from our desired `.txt` file, found in [books](./books/)
``` py
def get_book_text(path):
  with open(path) as f:
    return f.read()
```
> This little bit of code defines a function that takes in our `path` as a parameter, opens that file, then starts reading the content inside.

Next, we get the number of words within the text file:
``` py
def get_num_words(text):
  words = text.split()
  return len(words)
```
> Pretty simple, just take in the text file, split the words into a list, then return the numbered length of that list. This is that number you see in the console before each letter!

Then, we get the number of letters from the text file. A little trickier than totaling the word count:
``` py
def get_num_letters(text):
  letters = {}
  for letter in text:
    lowered_string = letter.lower()
    if lowered_string in letters:
      letters[lowered_string] += 1
    else:
      letters[lowered_string] = 1
  return letters
```
> Like I said, a little trickier, but let's break it down. Assign an empty dictionary (dict for short). Loop over each letter, convert to lower case to make matching easier, then validate whether or not the letter already exists in our dict. If it does, add 1 to it, if not assign 1. When all is said and done, return the dictionary!

Finally, we convert our dict to a list so we can format the output and make it easier to read:
``` py
def convert_dict_to_list(letters):
  new_list = []
  for k,v in letters.items():
    if not k.isalpha():
      continue
    new_list.append(f"The '{k}' character was found {v} times")
    formatted_list = "\n".join(new_list)
  return formatted_list # type: ignore
```
> Here, we take in our letters and create a new, empty list. For every `key` and `value` in our dictionary - remember when adding to a dict you assign the key, which was our letter, and the number of times it appeared - we check to see if it is an alphabetical character or not. If it isn't one, we continue forward, if it is, then we append it to our empty list with the formatted text string. After that, we join it all back together and create that line-by-line output you see in the images below!

## Conclusion

Anyways, this project was super fun and taught me a lot about how to traverse and manipulate dictionaries and lists using a simulated real-world example of data in python, hope you like it!

## Images

### Image 1 Using frankenstein.txt
![image](/images/00_bookbot_screenshot.png)

---

### Image 2 Using random_text_file.txt
![image](/images/01_bookbot_screenshot.png)