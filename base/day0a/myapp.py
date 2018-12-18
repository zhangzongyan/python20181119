# -*- coding: utf-8 -*-
#   File Name：     myapp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/18

from tkinter import *

def click_btn():
    # 新建一个新的窗口
    top = Toplevel()
    top.title('另一个新的窗口')
    top.geometry('300x200')
    top.resizable(0, 0)

    if v.get() == '确定':
        v.set('取消')
    else:
        v.set('确定')

root = Tk()
# print(dir(root))
root.geometry('600x400')
root.title('测试窗口')
root.resizable(0, 0) # 是否可伸缩
root.iconbitmap('logo.ico')

# 按钮组件
bnt = Button(root, height=2, width=10)
bnt.config(text='确定')
bnt['fg'] = 'red'
bnt['bg'] = '#00f000'
# bnt.pack(side='bottom')
# bnt['image'] = PhotoImage('ok_btn.gif')
# bnt.place(x=300, y=200) # 绝对布局
# 链接函数
bnt['command'] = click_btn
# 按钮的文字绑定变量
v = StringVar()
v.set('确定')
bnt['textvariable'] = v

# 按钮布局 side = 'top' / 'right' / 'bottom' / 'left' fill=X/Y/BOTH/None
bnt.pack(side='left', fill=Y, padx=10, pady=10, ipadx=50)

# 框架
frm = Frame(root)
frm['bg'] = 'pink'
frm.pack(side='bottom', expand=True, fill=X)

# 输入框
entry = Entry(frm)
entry['width'] = 10
# entry['show'] = '*'
entry.pack()

# 滚动条
scroll = Scrollbar(frm, orient=HORIZONTAL)
scroll.pack()

# 输入框绑定滚动条
scroll['command'] = entry.xview
entry['xscrollcommand'] = scroll.set

# 单选按钮

def click_rbtn():
    print(iv.get())

iv = IntVar()
iv.set(2) # 默认选rbtn2
rbtn1 = Radiobutton(frm, variable=iv, value=1)
rbtn1['text'] = 'Male'
rbtn1['command'] = click_rbtn
rbtn1.pack()

rbtn2 = Radiobutton(frm, variable=iv, value=2)
rbtn2['command'] = click_rbtn
rbtn2['text'] = 'Female'
rbtn2.pack()

# 复选按钮
def get_status():
    print(s1.get(), s2.get())

s1 = StringVar()
check1 = Checkbutton(frm, text='吃饺子', variable=s1, onvalue='choose_dumpling', offvalue='no_dumpling')
check1.pack()
s2 = IntVar()
check2 = Checkbutton(frm, text='吃包子', variable=s2, onvalue=1, offvalue=0)
check2.pack()
check3 = Checkbutton(frm, text='吃面条子')
check3.pack()

commit = Button(frm, text='提交')
commit['command'] = get_status
commit.pack()


root.mainloop()
