def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  num_letters = get_num_letters(text)
  converted_dict = convert_dict_to_list(num_letters)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print(f"{converted_dict}")
  print("--- End Report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_letters(text):
  letters = {}
  for letter in text:
    lowered_string = letter.lower()
    if lowered_string in letters:
      letters[lowered_string] += 1
    else:
      letters[lowered_string] = 1
  return letters

def convert_dict_to_list(letters):
  new_list = []
  for k,v in letters.items():
    if not k.isalpha():
      continue
    new_list.append(f"The '{k}' character was found {v} times")
    formatted_list = "\n".join(new_list)
  return formatted_list

main()