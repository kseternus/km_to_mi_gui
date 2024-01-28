import tkinter as tk


def convert():
    km = entry_int.get()
    km_to_mi = km * 0.62137
    output_str.set(f'{km} km in miles is: {km_to_mi:.2f} miles')


window = tk.Tk()
window.title('Convert kilometers to miles')
window.geometry('600x250')
window.config(bg='#292929')

title = tk.Label(master=window,
                  text='Convert kilometers to miles',
                  font='Futura 24',
                  foreground='#ffffff',
                  background='#292929')
title.pack(pady=30)

input_window = tk.Frame(master=window,  background='#292929')
entry_int = tk.IntVar()
entry = tk.Entry(master=input_window, textvariable=entry_int,)
button = tk.Button(master=input_window,
                   text='Convert',
                   command=convert,
                   foreground='#ffffff',
                   background='#fb7e14')
entry.pack(side='left', padx=15)
button.pack(side='left')
input_window.pack()

output_str = tk.StringVar()
output_window = tk.Label(master=window,
                          font='Futura 24',
                          textvariable=output_str,
                          foreground='#ffffff',
                          background='#292929')
output_window.pack(pady=30)

window.mainloop()
