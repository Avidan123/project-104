from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("multiplication")

num1=Label(root,text="number 1 is 6")
num1.pack()
num2=Label(root,text="number 2 is 5")
num2.pack()

result=Label(root)
def multi():
    a=6*5
    result["text"]=a

btn=Button(root,text="multiply",command=multi)
btn.pack()
result.pack()




root.mainloop()