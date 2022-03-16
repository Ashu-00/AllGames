from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("1900x1000")


def PhotoImag(file):
    return Image.open(file)


i1 = PhotoImag(file="pics/egg.png")
i2 = PhotoImag(file="pics/pong.png")
i3 = PhotoImag(file="pics/spaceshooter.png")
i4 = PhotoImag(file="pics/tag.png")

back = ImageTk.PhotoImage(PhotoImag(file="pics/back.png"))

bglab = Label(image=back)
bglab.place(x=-180, y=-50)


class label:
    def __init__(self, win, image, posx, posy, func):
        self.win = win
        self.image = image
        self.img = ImageTk.PhotoImage(image)
        self.posx = posx
        self.posy = posy
        self.lab = Label(win, image=self.img)
        self.lab.place(x=posx, y=posy)
        self.lab.bind("<Button-1>", lambda x: self.run(func))
        self.lab.bind("<Enter>", lambda x: self.enter(image))
        self.lab.bind("<Leave>", lambda x: self.leave(image))

    def run(self, abc=1):
        from subprocess import call
        from os import chdir

        if abc == 1:
            chdir(r"egg_catcher")
            call(["python", r"main.py"])
            chdir("..\\")

        elif abc == 2:
            chdir(r"pong")
            call(["python", r"main.py"])
            chdir("..\\")
        elif abc == 3:
            chdir(r"Space_Shooter")
            call(["python", r"main.py"])
            chdir("..\\")
        elif abc == 4:
            chdir(r"Tag")
            call(["python", r"main.py"])
            chdir("..\\")

    def enter(self, image=i1):
        self.image = image.resize((350, 450), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lab.config(image=self.img)
        self.lab.place(x=self.posx-25,y=self.posy-25)

    def leave(self, image=i1):
        self.image = image.resize((300, 400), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lab.config(image=self.img)
        self.lab.place(x=self.posx,y=self.posy)


class main:
    def __init__(self, win):
        self.win = win
        self.l1 = label(win, i1, 100, 0, 1)
        self.l2 = label(win, i2, 1000, 0, 2)
        self.l3 = label(win, i3, 100, 450, 3)
        self.l4 = label(win, i4, 1000, 450, 4)
        Label(win, text="MINIGAMES", fg="blue", font=("Gabriola", 40, "bold")).place(
            x=600, y=400
        )


# root.attributes("-fullscreen", True)

main(root)

root.mainloop()
