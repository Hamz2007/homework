from tkinter import *

window = Tk()

window.title("how old are you")
window.geometry("500x410+75+80")
label = Label(
    window,
    text = "Enter age",
    font=(
        "Arial",
        25,
        "bold"

    )
)

label.pack()
Name_enter=Entry(
    window,
    width=25,
    font=(
        "Arial",
        25,
        "bold"

    )
)

Name_enter.pack()
def show_name():
    text=Label(
        window,
        text = f"your age after 10 years will be {int(Name_enter.get())+10}",
        font=(
        "Arail",
        20,
        ""
        )
    )
    text.pack()
button = Button(
    window,
    text = "print age",
    width = 10,
    height = 1,
    command=show_name,
    font=(
        "Arial",
        25,
        "bold"

    )
)

button.pack()



window.mainloop()


