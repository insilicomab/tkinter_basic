import tkinter
import tkinter.font as font

# ウィンドウの作成
root = tkinter.Tk()
root.title("Label practice!")
root.iconbitmap("icon.ico")
root.geometry("550x550")
root.resizable(height=False, width=False)
root.config(bg="red")

# ラベルの作成
label_1 = tkinter.Label(root, text="よろしくお願いします")
label_1.pack()  # ウィンドウ上に設置する

# フォント指定
label_2 = tkinter.Label(root, text="よろしくお願いします", font=("Arial", 10, "bold"))
label_2.pack()

# 背景色、margin
label_3 = tkinter.Label(
    root, text="よろしくお願いします", font=("Arial", 10, "bold"), bg="gray"
)  # 背景：gray
label_3.pack(padx=10, pady=10)  # padx: 横方向にmargin、pady: 縦方向にmargin

# 文字色、padding、ラベルサイズ
label_4 = tkinter.Label(
    root, text="よろしくお願いします", font=("Arial", 10, "bold"), bg="gray", fg="green"
)
label_4.pack(
    padx=10, pady=(0, 10), ipadx=50, ipady=20, anchor="w"
)  # ipadx: 横方向にpadding、ipady: 縦方向にpadding、pady=(上側,下側)
# anchor="w": 左寄せ(west)、anchor="E": 右寄せ(east)

label_5 = tkinter.Label(
    root, text="よろしくお願いします", font=("Arial", 10, "bold"), bg="gray", fg="green"
)
label_5.pack(padx=10, pady=(0, 10), fill="both", expand=True)  # fill: 引き延ばす

# フォントの確認
print(font.families())

# ウィンドウのループ処理
root.mainloop()
