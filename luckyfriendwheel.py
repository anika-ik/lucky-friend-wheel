from tkinter import* 
import random

root=Tk()
root.title("luck friend wheel")
root.geometry("400x400")

list1 = ["neysa", "abhay", "manya", "nakul"]
print(list1)

def random_number():
    random_no = random.randint(0, 3)
    print(random_no)
    random_lucky_friend= list1[random_no]
    print("your lucky friend is " + random_lucky_friend)
    
    
btn = Button(root)
btn = Button(root, text="who is your luck friend ", command = random_number)
btn.place(relx= 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()