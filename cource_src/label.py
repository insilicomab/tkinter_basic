import tkinter
import tkinter.font as font

# ウィンドウの作成
root = tkinter.Tk()
root.title('Label practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)
root.config(bg='red')

# ラベルの作成
label_1 = tkinter.Label(root, text='よろしくお願いします')
label_1.pack()

label_2 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'))
label_2.pack()

label_3 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray')
label_3.pack(padx=10, pady=10)

label_4 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray', fg='green')
label_4.pack(padx=10, pady=(0, 10), ipadx=50, ipady=20, anchor='e')

label_5 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray', fg='green')
label_5.pack(padx=10, pady=(0, 10), fill='both', expand=True)

# フォントの確認
print(font.families())

# ウィンドウのループ処理
root.mainloop()
