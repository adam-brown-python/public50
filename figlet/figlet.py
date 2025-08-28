from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts_list = figlet.getFonts()
if len(sys.argv) == 1:
    font = random.choice(fonts_list)
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts_list:
            font = sys.argv[2]
        else:
            sys.exit("invalid command-line argument")
    else:
        sys.exit("provide '-f' or '--font' as second command-line argument")
if len(sys.argv) == 2:
    sys.exit("too many command-line arguments")
s = input("type: ")
f = figlet.setFont(font=font)
print(figlet.renderText(s))

