import tkinter
import tkinter.messagebox

def main():
    flag=True
    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg=('red',"no change label")
        if flag:
            True
        else:
            color,msg=("blue","change label")
        label.config(text=msg,fg=color)
    def confirm_to_qiut():
        if tkinter.messagebox.askokcancel("are you srue to quit?"):
            top.quit()
    top=tkinter.Tk()
    top.geometry("240x160")
    top.title("gui test")
    label=tkinter.Label(top,text="defult label",font="Arial-32",fg="red")
    label.pack(expand=1)
    panel=tkinter.Frame(top)
    button1=tkinter.Button(panel,text="change",command=change_label_text)
    button1.pack(side="left")
    button2=tkinter.Button(panel,text="qiut",command=confirm_to_qiut)
    button2.pack(side="right")
    panel.pack(side="bottom")
    tkinter.mainloop()

if __name__=="__main__":
    main()