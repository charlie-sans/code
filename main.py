import argparse

parser = argparse.ArgumentParser(description="Translate a file from cal to python")
parser.add_argument("input_file", help="The file to translate")
parser.add_argument("output_file", help="The file to output to")
args = parser.parse_args()

input_file = open(args.input_file, "r")
input_contents = input_file.read()
input_file.close()


dictionary_file = open("dictonary.jst", "r")
dictionary_contents = dictionary_file.read()
dictionary_file.close()

dictionary = {}
for line in dictionary_contents.split("\n"):
    key, value = line.split(":")
    dictionary[key] = value

translated_contents = ""
for word in input_contents.split():
    if word in dictionary: 
        translated_contents += dictionary[word] + " "
    else:
        translated_contents += word + " "

output_file = open(args.output_file, "w")
output_file.write(translated_contents)
output_file.close()