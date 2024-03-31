from customtkinter import *
from tkinter import *

root = Tk()
root.geometry("800x480")
root.config(bg='white')



# box = CTkFrame(master=root, fg_color='white', height=100, width=100, corner_radius=10, border_width=2, border_color='blue')
# box.pack(expand=YES)

# lbl = CTkLabel(master=box, text='khra', text_color='black')
# lbl.pack(fill="none", expand=YES)  # Set fill to "none" and expand to False for the label

button = CTkButton(master=root,fg_color='white',text='A',text_color='black',border_color='blue',border_width=2,corner_radius=4,hover=None)
button.pack()


box12 = CTkButton(master=frm_1,text='A',text_color='#1679EF',fg_color='#F2F7F9',height=100,width=50,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box12.grid(row=1,column=2,padx=0.5,pady=0.5)

box13 = CTkButton(master=frm_1,text='A',text_color='#1679EF',fg_color='#F2F7F9',height=100,width=50,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box13.grid(row=1,column=3,padx=0.5,pady=0.5)

root.mainloop()