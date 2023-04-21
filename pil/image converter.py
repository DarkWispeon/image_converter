from PIL import Image,ImageFilter
import os
import time

print("\033c")

pic = ""
used = ""

def pick():
    print("Which photo would you like to edit?")
    time.sleep(1.5)
    p = Image.open('test.jpeg')
    p.show()

    while True:
        usr = input()
        usr = int(usr)
        global pic
        print("Is this the right one?")
        time.sleep(1.5)

        if usr == 1:
            p = Image.open("eevee.jpeg")
            p.show()
            pic = "eevee.jpeg"
            break

        elif usr == 2:
            p = Image.open("arsene.jpeg")
            p.show()
            pic = "arsene.jpeg"
            break

        elif usr == 3:
            p = Image.open("zelda.jpeg")
            p.show()
            pic = "zelda.jpeg"
            break

        elif usr == 4:
            p = Image.open("hutao.jpeg")
            p.show()
            pic = "hutao.jpeg"
            break

        elif usr == 5:
            p = Image.open("kirby.jpeg")
            p.show()
            pic = "kirby.jpeg"
            break

        elif usr == 6:
            p = Image.open("hat.jpeg")
            p.show()
            pic = "hat.jpeg"
            break

        elif usr == 7:
            p = Image.open("nezuko.jpeg")
            p.show()
            pic = "nezuko.jpeg"
            break

        elif usr == 8:
            p = Image.open("joker.jpeg")
            p.show()
            pic = "joker.jpeg"
            break

        elif usr == 9:
            p = Image.open("persona.jpeg")
            p.show()
            pic = "persona.jpeg"
            break

        elif usr == 10:
            p = Image.open("ganyu.jpeg")
            p.show()
            pic = "ganyu.jpeg"
            break

        else:
            print("That's an invalid option")
            time.sleep(1.5)

    usr = input("Is this the right one?\ny/n\n")
    time.sleep(1.5)

    if usr.lower() == "n":
        pick()

    elif usr.lower() != "y":
        print("That's an invalid option")

    show_options()

def rotate():
    global pic
    global used
    if pic == "":
        pick()
    im = Image.open(pic)
    angle = int(input("By how many degrees do you want to rotate the image? "))
    rotated_image = im.rotate(angle, expand=True)
    rotated_image.show()
    
    
    used = "rotated"
    save(rotated_image)
    pic = rotated_image

def black_and_white():
    global pic
    global used
    if pic == "":
        pick()
    im = Image.open(pic)
    black_and_white = im.convert('L')
    black_and_white.show()
    
    
    used = "bw"
    save(black_and_white)
    pic = black_and_white


def blur():
    global pic
    global used
    if pic == "":
        pick()
    im = Image.open(pic)
    radius = int(input("Enter the blur radius: "))
    blurred_image = im.filter(ImageFilter.GaussianBlur(radius=radius))
    blurred_image.show()
    
    
    used = "blur"
    save(blurred_image)
    pic = blurred_image

def thumbnail():
    global pic
    global used
    global size
    if pic == "":
        pick()
    im = Image.open(pic)
    size = int(input("What size do you want the thumbnail to be? (200, 400, or 600) "))
    if size not in [200, 400, 600]:
        print("Invalid size")
        return
    im.thumbnail((size, size))
    im.show()
    
    used = "thumbnail"
    
    save(im)
    pic = im

def show_options():

    print("what would you like to do?")
    time.sleep(1.5)
    print("1. Rotate")
    time.sleep(1.5)
    print("2. Black and White")
    time.sleep(1.5)
    print("3. Blur")
    time.sleep(1.5)
    print("4. Thumbnail")
    time.sleep(1.5)
    print("5. Jpeg to PNG")
    time.sleep(1.5)
    print("6. Quit")
    time.sleep(1.5)
    print("\n")
    usr = input("type the number: ")
    if usr == "1":
        rotate()

    elif usr == "2":
        black_and_white()

    elif usr == "3":
        blur()

    elif usr == "4":
        thumbnail()

    elif usr == "5":
        png()

    elif usr == "6":
        quit()
    
def png():
    global pic
    global used
    with Image.open(pic) as img:
        img.save(f"{os.path.splitext(pic)[0]}.png", 'PNG')
        
    # Remove the JPEG file if it was successfully converted to PNG
    if os.path.exists(f"{os.path.splitext(pic)[0]}.png"):
        print(f"{pic} was successfully converted to {os.path.splitext(pic)[0]}.png")
        os.remove(pic)
    else:
        print(f"Failed to convert {pic} to {os.path.splitext(pic)[0]}.png")
        pic = img
        used = "png"


    

    
    # create save folder if it doesn't exist
    if not os.path.exists("png"):
        os.makedirs("png")

    # save edited image
    save(f"png/{img}")

    print("Image saved!")
    pic = img
    show_options()  # allow user to choose to edit another image or quit

def save(image):
    global pic
    global used
    if pic == "":
        pick()

    name = input("Enter a name for the edited image: ")
    extension = pic.split(".")[1]
    if used == "bw":
        save_folder = f"black_and_white"

    elif used == "rotated":
        save_folder = f"rotated"

    elif used == "thumbnail":
        save_folder = f"thumbnail"

    elif used == "blur":
        save_folder = f"blur"

    elif used == "png":
        save_folder = f"png"
        
    
    

    
    # create save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # save edited image
    if extension == "jpeg" or extension == "png":
    
        image.save(f"{save_folder}/{name}.{extension}")

    elif extension == "jpg":
        Image.save(f"{save_folder}/{size}/{name}.png")
    print("Image saved!")
    show_options()  # allow user to choose to edit another image or quit

pick()

