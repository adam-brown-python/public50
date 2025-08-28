from PIL import Image,ImageOps
import sys
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1] or sys.arg[2]).endswith(".jpg" or ".jpeg" or ".png"):
        sys.exit("Invalid input")

    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("input and output have different extensions")
    else:
        img = Image.open(sys.argv[1])
        img2  = Image.open("shirt.png")
        size = img2.size
        muppet = ImageOps.fit(img,size)
        muppet.paste(img2,img2)
        muppet.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File does not exist")
