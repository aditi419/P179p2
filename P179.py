from tkinter import *
import random
root = Tk()
root.geometry('500x500')
root.configure(background='lightblue')

label_name = Label(root,text='Random Color',font=('Sylfean',30,'bold'),bg='lightblue')
label_name.place(relx=0.5,rely=0.4,anchor=CENTER)

label_score = Label(root,text='Score: 0',font=('Sylfean',20),bg='lightblue')
label_score.place(relx=0,rely=0)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5,anchor=CENTER)

class Game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ['Blue','Purple','Green','Pink','Orange','Red','Yellow']
        self.random_number_for_text = random.randint(0,6)
        self.color = ['blue','purple','green','pink','orange','red','yellow']
        self.random_number_for_color = random.randint(0,6)
        label_name['text'] = self.text[self.random_number_for_text]
        label_name['fg'] = self.color[self.random_number_for_color]
        
    def __update_score(self,input_value):
        if input_value == self.color[self.random_number_for_color]:
            print(self.color[self.random_number_for_color])
            random_number_for_score = random.randint(0,10)
            self.__score += random_number_for_score
            label_score['text'] = 'Score: ' + str(self.__score)
            
    def get_user_value(self,input_value1):
        self.__update_score(input_value1)
        
obj = Game()
btn = Button(root,text='Start',command=obj.updateGame,bg='blue',fg='black',padx=3,pady=3,font=('Sylfean',25))
btn.place(relx=0.35,rely=0.6,anchor=CENTER)

def getInput():
    value = input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0,END)
    
btn = Button(root,text='Check',command=getInput,bg='green',fg='black',padx=3,pady=3,font=('Sylfean',25))
btn.place(relx=0.6,rely=0.6,anchor=CENTER)

root.mainloop()