from chatterbot import chatbot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot=chatbot("my Bot")                 #bot name

convo=[                               #data for conversion.(dataset)
    'Hello',
    'hi there',
    'what is your name?',
    'my name is my bot, i am created by pratik',
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'In which city you live?',
    'i am live in pune',
    'In which langauge you talk?',
    'I mostly talk in english.',
    'You are welcome.',
]

trainer=ListTrainer(bot)             #object for training a bot.

trainer.train(convo)                 #now training the bot with help of trainer.

print('talk to my bot')
while True:                          #function call.
    query=input()                    #user input.
    if query == 'exit':              #do not ans to bot then exist.
        break
    answer=bot.get_response(query)
    print('bot : ', answer)


#Creating a GUI Using tkinter.

main = Tk()

main.geometry('500x650')            #set for Height & Width.

main.title('my Bot')                #Window Title
img = PhotoImage(file='bot.png')       #img object

photoL=Lable(main,image=img)        #for lable

photoL.pack(pady=5)

 #function (ask from bot).

def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,'you : ' + query)
    msgs.insert(END,'bot : ' + str(answer_from_bot))
    textF.delet(0,END)

#crating Frame

frame=Frame(main)

sc=scrollbar(frame)                    #scrollbar
msg=Listbox(frame,width=80,height=20)

sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT,fill=Both,pady=10)

frame.pack()

#Creating text field.

textF=Entry(main,font=('Verdana',20))

textF.pack(fill=X,pady=10)

#creating button

btn=Button(main,text='Ask from bot',font=('Verdana',20),command=ask_from_bot)

btn.pack()

main.mainloop()











