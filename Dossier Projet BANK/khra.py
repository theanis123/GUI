from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('AMAN')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

frm1 = Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=X, side=TOP, pady=15)

old_image_frm1 = Image.open('image/AMAN-BLEU.png') 
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)  
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)   
label1 = Label(frm1, image=new_image_frm1, highlightthickness=0, bd=0)
label1.pack(expand=YES)

frm2 = Frame(root, bg='#F2F7F9', height=360, width=800)

img_diag = Image.open('fr/image/diagramme.png')
image_diag = ImageTk.PhotoImage(img_diag)
lbl_diag = Label(frm2, image=image_diag, bg='#F2F7F9', bd=0)
lbl_diag.place(x=20, y=30)

# Position des boutons alignés à gauche dans le milieu
x_pos = 300
y_pos = 50

btn1 = Button(frm2, text='Volume A', font=('Arial', 20), bg='#1679EF', fg='#F2F7F9', width=15, bd=0)
btn1.place(x=x_pos, y=y_pos)

btn2 = Button(frm2, text='Volume B', font=('Arial', 20), bg='#1679EF', fg='#F2F7F9', width=15, bd=0)
btn2.place(x=x_pos, y=y_pos + 100)

btn3 = Button(frm2, text='Volume C', font=('Arial', 20), bg='#1679EF', fg='#F2F7F9', width=15, bd=0)
btn3.place(x=x_pos, y=y_pos + 200)

image_flch1 = Image.open('fleche3.png')
img_flch1 = ImageTk.PhotoImage(image_flch1)
label_flch1 = Label(frm2, image=img_flch1, bg='#F2F7F9')
label_flch1.place(x=735, y=43)

image_flch2 = Image.open('fleche3.png')
img_flch2 = ImageTk.PhotoImage(image_flch2)
label_flch2 = Label(frm2, image=img_flch2, bg='#F2F7F9')
label_flch2.place(x=735, y=243)

image_flch3 = Image.open('fleche3.png')
img_flch3 = ImageTk.PhotoImage(image_flch3)
label_flch3 = Label(frm2, image=img_flch3, bg='#F2F7F9')
label_flch3.place(x=735, y=143)

btn_srt = Button(frm2, text='Sortie', font=('Arial', 15), bg='#1679EF', fg='#F2F7F9', width=7, bd=0)
btn_srt.place(x=45, y=320)

image_flch_srt = Image.open('fleche3.png')
rotated_img = image_flch_srt.rotate(180)
resize = rotated_img.resize((35, 35), Image.LANCZOS)
img_flch_srt = ImageTk.PhotoImage(resize)
label_flch_srt = Label(frm2, image=img_flch_srt, bg='#F2F7F9')
label_flch_srt.place(x=2, y=319)

frm2.pack()

frm3 = Frame(root, bg='#1679EF', height=30)
label2 = Label(frm3, text="03-04-2024  /  05:33", font=('Arial', 12), fg='#F2F7F9', bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
