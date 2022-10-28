from tkinter import ttk

import qrcode
from PIL import Image, ImageTk


class qrcode_tool:
    def __init__(self, frame):
        self.entry_in = ttk.Entry(frame,
                             bootstyle="danger",
                             width=64)
        self.entry_in.focus()
        self.entry_in.grid(row=0, column=0)

        # 生成按钮
        create_qr_code_btn = ttk.Button(frame,
                                        text="生成",
                                        bootstyle="success",
                                        command=lambda: self.create_qr_code(frame, self.entry_in.get()))
        create_qr_code_btn.grid(row=0, column=1)

        # 可以配置的参数
        self.version_scale = ttk.Scale(frame,
                                       bootstyle="primary",
                                       from_=10,
                                       value=1,
                                       to=0,
                                       command=self.t
                                       )
        self.version_scale.grid(row=1, column=1)

    # 生成二维码
    def create_qr_code(self, frame, text):
        info_label = ttk.Label(text="", bootstyle="danger")
        info_label.place(x=668, y=70)
        if len(text) == 0:
            info_label.configure(text="输入为空,请重新输入")
        else:
            qr = qrcode.QRCode(version=4,
                               box_size=10,
                               border=4,
                               image_factory=None,
                               mask_pattern=None)
            qr.add_data(text)
            img = qr.make_image()
            img.save("qrcode.png")
            pic = Image.open("qrcode.png")
            pic_r = ImageTk.PhotoImage(pic)
            l = ttk.Label(frame, image=pic_r)
            l.grid(row=2, column=0)

    def t(self):
        print(self.version_scale.getint())