from tkinter import *
from PIL import Image, ImageTk

def every_100(text):
    final_text = ""
    for i in range(len(text)):
        final_text += text[i]
        if i%100 == 0 and i != 0:
            final_text += "\n"
    return final_text
    

root = Tk()
root.geometry("1000x1000")
root.title("Times Newspaper")

photos=[]
texts=[]
for i in range(3):
    with open(f"C:\SIMAR\PycharmProjects\TkinterCourse/{i + 1}.txt", encoding="utf8") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"C:\SIMAR\PycharmProjects\TkinterCourse\photos/{i + 1}.png")
    # TODO: Resize the images
    image = image.resize((225,225), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width= 800 , height= 70)
Label(f0 , text = "Indian Times News" , font = "Lucida 33 bold").pack()
f0.pack()

f0 = Frame(root, width= 800 , height= 70)
Label(f0 , text = "22 july, 2034" , font = "Lucida 13 bold").pack()
f0.pack()

for i in range(3):
    if i == 0 or i == 2:
        f1 = Frame(root, width =900, height =200)
        Label(f1, text = texts[i],padx=5,pady=5).pack(side = "left")
        Label(f1, image= photos[i], anchor='e').pack()
        f1.pack(anchor= 'w')
    if i==1 :
        f1 = Frame(root, width =900, height =200,padx=22)
        Label(f1, text = texts[1],padx=5,pady=5).pack(side = "right")
        Label(f1, image= photos[1], anchor='e').pack()
        f1.pack(anchor= 'w')


root.mainloop()
