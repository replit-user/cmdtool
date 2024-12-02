import argparse
parser=argparse.ArgumentParser()
parser.add_argument("filename",help="the filename that contains the specified text")
parser.add_argument("text",help="the text to include in the file, use .n for a new line")
parser.add_argument("-a","--append",help="opens the file in append mode which adds to an existing file rather than overwriting it",action="store_true")
args=parser.parse_args()
text=args.text
filename=args.filename
text=text.replace(".n","\n")
if args.append:
    with open(filename,"a") as file:
        file.write(text)
else:
    with open(filename,"w") as file:
        file.write(text)
