from tkinter import *
window=Tk()
masiv=[]

def btn_click():
    a = text.get()
    masiv=list(map(int, a.split()))
    x='Сума:',sum(masiv)
    y='Середне арефметичне:',sum(masiv)/len(masiv)
    title1.config(text=x)
    title2.config(text=y)


window['bg']='white'
window.title('Сума та середне арефметичне')
window.geometry('500x500')

place = Frame( bg='yellow')
place.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

title = Label(place, text='Введіть числа через пробіл',bg='blue', )
title.pack()

text= Entry(place, bg='black')
text.pack()

btn=Button(place, text='Отримати відповідь', bg='blue', command=btn_click)
btn.pack()

title1 = Label(place, text='Сума',bg='blue')
title1.pack()

title2 = Label(place, text='Середне арефметичне:',bg='blue')
title2.pack()


window.mainloop()