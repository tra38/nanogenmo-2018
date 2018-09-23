import json
import os
import random

# set up boilerplate methods

# Append text to the novel file
def write_to_novel(text):
  with open('novel.md', 'a') as out:
      out.write(text + '\n\n')

# Randomize an array
def randomize_array(array):
  random.seed(42) # fixed seed ensures reproducability
  random.shuffle(array)
  return array

# Generate a citation in the form of '{shortened version of quote in story} is from {source}, {license_link}. Quote modified from the original - original quote is {shortened version of original quote}'
def generate_citation(passage):
  shortened_new_quote = generate_quote_shortner(passage['quote'])
  shortened_original_quote = generate_quote_shortner(passage['original_quote'])
  source_link = passage['source']
  license_link = generate_link(passage['license'], passage['license_url'])
  template = "- {shortened_new_quote} is from {source_link}, {license_link}. Quote modified from original - original quote is {shortened_original_quote}"
  final_response = template.format(shortened_new_quote=shortened_new_quote, shortened_original_quote=shortened_original_quote, source_link=source_link, license_link=license_link)
  return final_response

# generate a shortened version of the quote in the form of '{first three words} ... {last three words}'
def generate_quote_shortner(quote):
  text_array = quote.split()
  first_phrase = ' '.join(text_array[0:3])
  second_phrase = ' '.join(text_array[-3:])
  template = '"{first_phrase} ... {second_phrase}"'
  final_response = template.format(first_phrase=first_phrase, second_phrase=second_phrase)
  return final_response

# Generate a Markdown-formatted version of the link
def generate_link(license, license_url):
  license_link_template = "[{license}]({license_url})"
  license_link = license_link_template.format(license=license, license_url=license_url)
  return license_link

# remove our existing novel if it already exists
try:
    os.remove("novel.md")
except OSError:
    pass

# Now let's load up our data, making sure to randomize the order of the paragraphs in the middle section
with open("corpus.json", 'r') as stream:
  data = json.load(stream)

starting_paragraphs = data['begin']
middle_paragraphs = randomize_array(data['missions'])
ending_paragraphs = data['ending']

# Write the introductory paragraphs, with a horizontal bar after the introduction
for passage in starting_paragraphs:
  write_to_novel(passage['quote'])
write_to_novel("---")

# Write the missions, with a horizontal bar after each mission
for passage in middle_paragraphs:
  write_to_novel(passage['quote'])
  write_to_novel("---")

# Write the ending paragraph, with a horizontal bar after the ending
for passage in ending_paragraphs:
  write_to_novel(passage['quote'])
write_to_novel("---")

# Now, let's write the citations!

write_to_novel("Citations:")

all_paragraphs = starting_paragraphs + middle_paragraphs + ending_paragraphs

for passage in all_paragraphs:
  write_to_novel(generate_citation(passage))

write_to_novel("Manual Citation:")
write_to_novel(generate_citation({
    "quote": "Book of Azathoth, the Book of Eibon, the Book of Iod, the Celaeno Fragments, the Cultes des Goules, De Vermis Mysteriis, the Dhol Chants, the Eltdown Shards, the G'harne Fragments, the King in Yellow, the Libre Ivonis, the Necronomicon, On the Sending Out of Souls, the Parchments of Pnom, the Pnakotic Manuscripts, the Poakotic Fragments, the Ponape Scripture, Las Reglas de Ruina, the Relevations of Gla'aki, the Seven Cryptical Books of Hsna, the Tarsioid Psalms, the Moloch Diaries, the Testaments of Carnamagos, the Unaussprechilche Kulte, the Zanthu Tablets, the Zhou Texts, the Structure and Interpretation of Computer Programs, and Artificial Intelligence: A Modern Approach",
    "original_quote": "Book of Azathoth, the Book of Eibon, the Book of Iod, the Celaeno Fragments, the Cultes des Goules, De Vermis Mysteriis, the Dhol Chants, the Eltdown Shards, the G'harne Fragments, the King in Yellow, the Libre Ivonis, the Necronomicon, On the Sending Out of Souls, the Parchments of Pnom, the Pnakotic Manuscripts, the Poakotic Fragments, the Ponape Scripture, Las Reglas de Ruina, the Relevations of Gla'aki, the Seven Cryptical Books of Hsna, the Tarsioid Psalms, the Testaments of Carnamagos, the Unaussprechilche Kulte, the Zanthu Tablets, the Zhou Texts",
    "source": "https://github.com/NaNoGenMo/2016/issues/12",
    "license": "Copyrighted text, used under a 'fair use' defense",
    "license_url": "https://en.wikiquote.org/wiki/Wikiquote:Copyrights#Copyrights_and_quotations"}))

# And just a little wrapup to meet word counts

write_to_novel("---")

write_to_novel("The following is a summary from the novel 'The Moloch Diaries'...")

the_final_welp = "meow " * 50000

write_to_novel(the_final_welp)