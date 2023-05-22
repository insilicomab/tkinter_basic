import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Frame practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# なぜframeを使うのか？
# tkinter.Label(root, text='test').pack()
# tkinter.Button(root, text='test').grid(row=0, column=0)

# frameの作成
frame_1 = tkinter.Frame(root, bg='yellow')
frame_2 = tkinter.Frame(root, bg='green')
frame_3 = tkinter.LabelFrame(root, text='ラベルフレームです', borderwidth=5)

# frameをroot上に配置
frame_1.pack(fill='both', expand=True)
frame_2.pack(fill='both', expand=True)
frame_3.pack(fill='both', expand=True)

# ウィジェットの配置
tkinter.Label(frame_1, text='テスト').pack()
tkinter.Label(frame_1, text='テスト').pack()
tkinter.Label(frame_1, text='テスト').pack()

tkinter.Label(frame_2, text='テスト').grid(row=0, column=0)
tkinter.Label(frame_2, text='テスト').grid(row=1, column=1)
tkinter.Label(frame_2, text='テスト').grid(row=2, column=2)
# tkinter.Label(frame_2, text='ggggggggggggggggggggggggggggggggggggg').grid(row=3, column=0)

tkinter.Label(frame_3, text='ggggggggggggggggggggggggggggggggggggg').grid(row=0, column=0)


# ウィンドウのループ処理
root.mainloop()
