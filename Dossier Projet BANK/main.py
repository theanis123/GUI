import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
import locale


#met la localisatin suivant la france      permet davoir la langue française pour la date
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

#partie initialisation de la fenetre
root = tk.Tk()
root.title('AMAN')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

#bande bleu d'en haut avec logo AMAN
frm1 = tk.Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=tk.X, side=tk.TOP,pady=15)

    
old_image_frm1 = Image.open('image/AMAN-BLEU.png') # importe l'image image   
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)  # redimentioner l'image    
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)   # image  final    ---------- si tu veux faire des modifs cest cette Var que tu va utiliser
label1 = tk.Label(frm1, image=new_image_frm1,highlightthickness=0,bd=0)#afficher l'image(image rahi f label)
label1.pack(expand=tk.YES)





#frame2    c'est la partie central de la fenetre 
frm2= tk.Frame(root,bg='#F2F7F9')

old_image_frm2 = Image.open('image/AMAN-WHITE.jpg')
resize_frm2 = old_image_frm2.resize((240,140),Image.LANCZOS)
new_image_frm2 = ImageTk.PhotoImage(resize_frm2)
label = tk.Label(frm2,bg='#1679EF',image=new_image_frm2,bd=0,highlightthickness=0)
label.pack(pady=40)




#partie bouton ----si tu veux ajouter un role pour le bouton ajoute "commad=ta fonction"
button = tk.Button(frm2,text="Start      ابدا ",font=(('Arial'),20),width=20,bg='#1679EF',fg='#F2F7F9',bd=0)
button.pack()
frm2.pack()


#bande bleu d'en bas
frm3 = tk.Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = tk.Label(frm3,text=f"{date:%m-%d-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=tk.YES)

frm3.pack(fill=tk.X, side=tk.BOTTOM)

root.mainloop()


