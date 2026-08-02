import tkinter as tk

root = tk.Tk()
root.title('amir')
root.geometry('400x500')
root.configure(bg='green')

entry_var = tk.StringVar()
entry = tk.Entry(root , textvar = entry_var , font='Arial 20 bold' , justify='right' , bg='black' , fg='white')

entry.pack(fill='both' , ipadx=8 , padx=10 , pady=10)

buttons = [
         
  [ '7' , '8' , '9' , '/'],
  [ '4' , '5' , '3' , '*'],
  [ '1' , '2' , '3' , '-'],
  [ 'C' , '0' , '=' , '+'],
         
]



def on_click(event) :
    text = event.widget.cget('text')
    if text == '=':
         try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
         except Exception as e:
                   entry_var.set('Error')
                   
    elif text == 'C' :
              entry_var.set('')
    else : 
     
         entry_var.set(entry_var.get() + text)


for row in buttons:
   frame = tk.Frame(root , bg='black')
   frame.pack(expand=True , fill='both')
   for button in row:
        btn = tk.Button(frame ,text=button , font='Arial 15 bold', height=2 , width=5 ,bg='#00ff00' , fg='black')
        btn.pack(side='left' , expand=True , fill='both')
        btn.bind('<Button-1>' , on_click)

root.mainloop()