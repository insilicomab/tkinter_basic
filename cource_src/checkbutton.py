import tkinter


# ウィンドウの作成
root = tkinter.Tk()
root.title('Checkbutton Practice!')
root.geometry('300x200')
root.resizable(0, 0)


# 関数の作成
def print_value():
    radio_value = number.get()
    boolean_1_value = boolean_1.get()
    boolean_2_value = boolean_2.get()
    print('ラジオボタン：' + str(radio_value))
    print('チェックボタン1：' + str(boolean_1_value))
    print('チェックボタン2：' + str(boolean_2_value))


# ラジオボタンの整数値
number = tkinter.IntVar()
number.set(0)


# ラジオボタンの作成
radiobutton_1 = tkinter.Radiobutton(root, text='ラジオボタン1', variable=number, value=0)
radiobutton_2 = tkinter.Radiobutton(root, text='ラジオボタン2', variable=number, value=1)
radiobutton_1.grid(row=0, column=0, padx=30, pady=10)
radiobutton_2.grid(row=0, column=1, padx=30, pady=10)


# チェックボタンのON/OFF
boolean_1 = tkinter.BooleanVar()
boolean_2 = tkinter.BooleanVar()

# チェックボタンの作成
checkbutton_1 = tkinter.Checkbutton(root, text='チェックボタン1', variable=boolean_1)
checkbutton_2 = tkinter.Checkbutton(root, text='チェックボタン2', variable=boolean_2)
checkbutton_1.grid(row=1, column=0)
checkbutton_2.grid(row=1, column=1)


# ボタンの作成
button_1 = tkinter.Button(root, text='テスト', command=print_value)
button_1.grid(row=2, column=0, columnspan=2, padx=100, pady=10, ipadx=10)


# ループ処理
root.mainloop()
