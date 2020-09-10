from tkinter import *
from PIL import Image, ImageTk

def make_happy():
    cat_label.configure(image=happy_cat_img)
    cat_label.image = happy_cat_img

def make_sad():
    cat_label.configure(image=sad_cat_img)
    cat_label.image = sad_cat_img

root = Tk()
root.title("cute cat")

# image declarations
cat_img = ImageTk.PhotoImage(Image.open("cat.jpg"))
happy_cat_img = ImageTk.PhotoImage(Image.open("happy_cat.jpg"))
sad_cat_img = ImageTk.PhotoImage(Image.open("sad_cat.jpg"))

cat_label = Label(image=cat_img)
cat_label.grid(row=0, column=1)

happy_button = Button(root, text="happy", command=make_happy).grid(row=1, column=0)
sad_button = Button(root, text="sad", command=make_sad).grid(row=1, column=2)

root.mainloop()
