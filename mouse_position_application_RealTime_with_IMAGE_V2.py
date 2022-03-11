# Get Mouse Position in Real Time
# Version 1.0
# Dev:- Joel Dcosta
# Import the required libraries
from tkinter import *
import pyautogui
from PIL import Image, ImageTk

root=Tk()
root.title("Mouse Position Application in Real Time")

# Getting Your Screen Size
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
print(ws,hs)

i_size = 30
img = Image.open("dot.png")
img = img.resize((img.width//i_size,img.height//i_size))
img= ImageTk.PhotoImage(img)

def mouse_position(event):
   x, y = pyautogui.position()
   m = ("X: "+str(x)+'\n'+ "Y: "+str(y))
   x1=event.x
   y1=event.y
   x2=event.x
   y2=event.y
   # Draw an oval in the given co-ordinates
   #canvas.create_oval(x1,y1,x2,y2,fill="black", width=5)

   # Using PNG Image 
   canvas.create_image(x2,y2,image=img)
   
   # In simple format
   #canvas.create_text(x2+0,y2+15,text=f"{m}")

   # Same as above but with font, size, color
   # Anchor East = e, west = w, north = n, south = s
   canvas.create_text(x2+0,y2-25,text=f"{m}", anchor='e', font=("Courier", 10), fill='red')

# Create a canvas widget
canvas = Canvas(root, width=f"{ws}", height=f"{hs}", bg = '#F6F6F6', highlightthickness = 0)
canvas.pack()

# To Make Full Screen
#canvas.master.overrideredirect(True)

# Make screen transparent using alpha
canvas.master.wm_attributes("-alpha",0.4)

# Keep it above all other window screens
canvas.master.wm_attributes("-topmost",True)

# To show result after release use <ButtonRelease-1>
canvas.bind('<ButtonPress>', mouse_position)

canvas.mainloop()



            

