import tkinter


# 関数の作成
def open_setting():
    subwindow = tkinter.Toplevel()
    subwindow.title("設定")
    subwindow.geometry("200x100+500+150")

    subwindow_label = tkinter.Label(subwindow, text="設定画面です")
    subwindow_label.pack(pady=30)


# ウィンドウの作成
root = tkinter.Tk()
root.title("Menu Practice!")
root.geometry("260x200")
root.resizable(height=False, width=False)

# メニューバーの作成
# メニューバーの親となるコンテナの作成
menubar = tkinter.Menu(root)
root.config(menu=menubar)

# 設定メニューの作成
setting_menu = tkinter.Menu(menubar, tearoff=False)  # tearoff=False: 点線を消す
menubar.add_cascade(label="設定", menu=setting_menu)

# ファイルメニューの作成
file_menu = tkinter.Menu(menubar, tearoff=False)
menubar.add_cascade(label="ファイル", menu=file_menu)

# 設定メニューにプルダウンメニューを追加
setting_menu.add_command(label="環境設定", command=open_setting)
setting_menu.add_command(label="終了")

# ファイルメニューにプルダウンメニューを追加
file_menu.add_command(label="新規ファイル")


# ループ処理
root.mainloop()
