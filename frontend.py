'''
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View  all records
Search an entry
Add entry
Update entry
Delete
Close

listbox, scroll bar
grid method(we will use), pack method
'''

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    # index = list1.curselection()[0] this line is IMPORTANT
    # NULL POINTER EXCEPTION:
    # If listbox is empty,  list1.curselection()  will be an empty list with no items. 
    #list1.curselection()[0] caused indexError
    try:
        index = list1.curselection()[0] # list1.curselection() returns (2,) which is a tuple
        selected_tuple= list1.get(index) #from listbox, get the tuple of index x
        #print(index)
        #return selected_tuple
        #print(selected_tuple) #(5, 'New', 'New', 1212, 1212121)
        #print(selected_tuple[0])  # id
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1]) # insert method must has two parameters
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError: # python is case sensitive
        pass #The pass  statement means "do nothing". 

def view_command(): # returned is "tuples in a list"
    list1.delete(0, END) # delete from index 0 to END of this list box
    for row in backend.view():
        list1.insert(END, row) # special 'END" index means the new row will put in the end of the list box

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        #title_text.get() convert the string var object (type) to string type
        list1.insert(END, row) 

def insert_command():
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.delete(0, END)
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
   
def delete_command():
        backend.delete(selected_tuple[0]) # (6, 'wonderlands', 'helena', 1944, 2442424)

def update_command():
        backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window=Tk()
window.wm_title("Bookshop")

l1 = Label(window, text="Title")
# crl + enter can let cursor move to the next line
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar() # define the data type (object not type actuallly) of textvriable(input) 
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar() # define the data type of textvriable(input)
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar() # define the data type of textvriable(input)
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = StringVar() # define the data type of textvriable(input)
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row=2, column=0, rowspan=6, columnspan= 2)
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)  #event type is listboxselect

b1=Button(window, text="View all", width = 12, command=view_command)
b1.grid(row=2, column=3)
b2=Button(window, text="Search entry", width = 12, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window, text="Add entry", width = 12, command=insert_command)
b3.grid(row=4, column=3)
b4=Button(window, text="Update selected", width = 12, command=update_command)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete selected", width = 12, command=delete_command)
b5.grid(row=6, column=3)
b6=Button(window, text="Close", width = 12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()

#$ pyinstaller --onefile --window frontend.py
#PS E:\Python> pyinstaller --onefile --windowed --name "BookStore" "E:\Python\frontend.py"
'''
def from_kg():
    #print(e1_value.get())
    #miles = float(e1_value.get())*1.6
    gram = float(e1_value.get())*1000.0
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
     # Deletes the content of the Text box from start to END
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)
    
# Create a Label widget with "Kg" as label
e2=Label(window, text="Kg")
e2.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1=Button(window, text="Convert", command=from_kg)
#b1.pack()
b1.grid(row=0,column=2) # rowspan=2 means all widgets will be within row 0 and row 1 in this case

t1=Text(window, height=1, width=20)
t2=Text(window, height=1, width=20)
t3=Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2.grid(row=1, column=1)
t3.grid(row=1, column=2)
'''
