import tkinter
from PIL import ImageTk, Image


def display_image():
    global image_by_pillow

    image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
    label_by_pillow = tkinter.Label(root, image=image_by_pillow)
    label_by_pillow.pack()


# ウィンドウの作成
root = tkinter.Tk()
root.title('Image practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# 画像の配置
image_1 = tkinter.PhotoImage(file='dice.png')
label_1 = tkinter.Label(root, image=image_1)
label_1.pack()

button_1 = tkinter.Button(root, image=image_1)
button_1.pack()


# jpgの利用
# image_2 = tkinter.PhotoImage(file='mountain.jpg')
# label_2 = tkinter.Label(root, image=image_2)
# label_2.pack()


# pillowによってjpgを読み込んで表示
# image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
# label_by_pillow = tkinter.Label(root, image=image_by_pillow)
# label_by_pillow.pack()

display_image()

# ウィンドウのループ処理
root.mainloop()
