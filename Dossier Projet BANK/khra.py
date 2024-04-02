from customtkinter import *
import kivy.app
import arabic_reshaper
import bidi.algorithm


root = CTk()
root.geometry("800x480")
root.configure(fg_color='white')


reshaped_text7 = arabic_reshaper.reshape( '48 ساعة / 4000 دج')
bidi_text  = bidi.algorithm.get_display(reshaped_text7)

lbl = CTkButton(master=root,
                text=bidi_text,
                font=('Arial',26),
                fg_color='#1679EF',
                text_color='#F2F7F9',
                corner_radius=4,
                height=45,
                width=260,
                border_width=0)
lbl.place(x=66,y=220)



# reshaped_text8 = arabic_reshaper.reshape( '48 ساعة / 4000 دج')
# bidi_text  = bidi.algorithm.get_display(reshaped_text8)
# btn7 = CTkButton(master=root,
#                  text=reshaped_text8,
#                  font=('Arial',26),
#                  fg_color='#1679EF',
#                  text_color='#F2F7F9',
#                  width=260,
#                  height=45,
#                  border_width=0,
#                  corner_radius=4)
# btn7.place(x=66,y=220)
                 




root.mainloop()
