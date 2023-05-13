import threading
import time
import queue
import tkinter
'''
exitflag=0
queueLock = threading.Lock()
class mythread(threading.Thread):
    def __init__(self,threadid,name,q):
        super().__init__()
        self.threadid=threadid
        self.name=name
        self.q=q
    def run(self):
        print("开始线程："+self.name)
        process_data(self.name,self.q)
        print("结束进程："+self.name)
def process_data(threadname,q):
    while not exitflag:
        queueLock.acquire()
        if not workqueue.empty():
            data=q.get()
            queueLock.release()
            print("{} process {}".format(threadname,data))
        else:
            queueLock.release()
        time.sleep(1)
threadlist=["one",'two','three','four','five']
workqueue=queue.Queue(10)
threads=[]
threadid=1
for i in range(4):
    threadname='thread'+str(i)
    thread=mythread(threadid, threadname, workqueue)
    thread.start()
    threads.append(thread)
    threadid+=1

queueLock.acquire()
for word in threadlist:
    workqueue.put(word)
queueLock.release()
while not workqueue.empty():
    pass
exitflag=1
for t in threads:
    t.join()
print("exit")'''

def download():
    flag=True
    time.sleep(2)
    tkinter.messagebox.showinfo("下载完成！")
    flag = not flag
    color, msg = ('red', '1')\
            if flag else ('blue', 'Goodbye, world')
    label.config(text=msg, fg=color)

def showabout():
    tkinter.messagebox.showinfo("作者：刘波 版本：1.0X")
def main():
    top=tkinter.Tk()
    top.title("单线程")
    top.geometry('400x300')
    label = tkinter.Label(top, text='1 ', font='Arial -32', fg='red')
    label.pack(expand=1)
    top.wm_attributes('-topmost', True)
    panel=tkinter.Frame(top)
    button1=tkinter.Button(panel,text="download",command=download)
    button1.pack(side="left")
    button2=tkinter.Button(panel,text="show",command=showabout)
    button2.pack(side='right')
    panel.pack(side="bottom")
    tkinter.mainloop()


if __name__=="__main__":
    main()