#!/usr/local/bin/python3.9

# mac: brew install python-tk@3.9
# pip dependency:
#   pip install ttkbootstrap
#   pip install qrcode
#   pip install Pillow
#   pip install requests
#   pip install pyinstaller

# dist
    # pyinstaller -w -F -n toolKit -i icon.icns main.py
import random
import tkinter as tk

import qrcode
import ttkbootstrap as ttk

from app.qrcode_tool import qrcode_tool
from client.http import http


class App:
    title = "Alex-黑白的工具包 按ESC返回主页"

    def __init__(self):
        self.app = tk.Tk()

        self.app.bind_all("<Key>", self.listen_keyboard)

        self.title = self.title
        self.width = 960
        self.height = 640
        self.geometry = str(self.width) + "x" + str(self.height)

        self.last_scene = ""
        self.current_scene = "root_frame"

        # 子页面 容器
        self.sec_view = tk.Frame(self.app)

        # 按钮风格
        self.btn_style_list = ['primary', 'success', 'info', 'warning',
                               'danger', 'dark']

        # 文本风格
        self.label_style_list = ['primary', 'success', 'info', 'warning',
                                 'danger']

        # 鼠标悬浮风格
        self.cursor_style_list = ['arrow', 'double_arrow', 'man', 'sizing',
                                  'based_arrow_down', 'draft_large', 'middlebutton', 'spider',
                                  'based_arrow_up', 'draft_small', 'mouse', 'spraycan',
                                  'boat', 'draped_box', 'pencil', 'star',
                                  'bogosity', 'exchange', 'pirate', 'target',
                                  'bottom_left_corner', 'fleur', 'plus', 'tcross',
                                  'bottom_right_corner', 'gobbler', 'question_arrow', 'top_left_arrow',
                                  'bottom_side', 'gumby', 'right_ptr', 'top_left_corner',
                                  'bottom_tee', 'hand1', 'right_side', 'top_right_corner',
                                  'box_spiral', 'hand2', 'right_tee', 'top_side',
                                  'center_ptr', 'heart', 'rightbutton', 'top_tee',
                                  'circle', 'icon', 'rtl_logo', 'trek',
                                  'clock', 'iron_cross', 'sailboat', 'ul_angle',
                                  'coffee_mug', 'left_ptr', 'sb_down_arrow', 'umbrella',
                                  'cross', 'left_side', 'sb_h_double_arrow', 'ur_angle',
                                  'cross_reverse', 'left_tee', 'sb_left_arrow', 'watch',
                                  'crosshair', 'leftbutton', 'sb_right_arrow', 'xterm',
                                  'diamond_cross', 'll_angle', 'sb_up_arrow', 'X_cursor',
                                  'dot', 'lr_angle', 'sb_v_double_arrow',
                                  'dotbox', 'shuttle']

        # 主题列表
        self.theme_list = ['cosmo', 'flatly', 'journal', 'litera', 'lumen', 'minty', 'pulse',
                           'sandstone', 'united', 'yeti', 'morph', 'simplex', 'cerculean',
                           'solar', 'superhero', 'darkly', 'cyborg']

        # log操作显示
        # self.sys_operate_log_Label = ttk.Label(self.root_frame, bootstyle=self.label_style_list[self.init_label_random()])
        # self.sys_operate_log_Label.place(x=8, y=self.height - 24)

    # 随机鼠标悬浮样式
    def init_cusor_random(self):
        return random.randint(0, len(self.cursor_style_list) - 1)

    # 随机按钮样式
    def init_btn_random(self):
        return random.randint(0, len(self.btn_style_list) - 1)

    # 随机文本样式
    def init_label_random(self):
        return random.randint(0, len(self.label_style_list) - 1)

    # 随机主题皮肤
    def random_theme(self):
        theme_index = random.randint(0, len(self.theme_list) - 1)
        ttk.Style(self.theme_list[theme_index])

        # 输出主题变更日志
        self.show_operate_log("用户变更了主题，当前使用主题：" + self.theme_list[theme_index])

    # 渲染主页：home
    def render_home(self):
        row_pad_x = 16  # 行左右间距
        row_pad_y = 6  # 行纵坐标间隔
        btn_pad_x = 6  # 按钮col间距
        pad_frame = 10  # frame的padding

        # if hasattr(self, "root_frame"):
        #     self.root_frame.destroy()

        # 主页home容器
        self.root_frame = tk.Frame(self.app)
        self.root_frame.pack(side=tk.LEFT)

        self.frame_client = ttk.LabelFrame(self.root_frame, text="client模拟",
                                           bootstyle=self.btn_style_list[self.init_btn_random()],
                                           padding=pad_frame)
        self.frame_client.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_http = ttk.Button(self.frame_client, text="http",
                              bootstyle=self.btn_style_list[self.init_btn_random()],
                              cursor=self.cursor_style_list[self.init_cusor_random()],
                              command=self.open_http_client)
        btn_http.pack(padx=btn_pad_x, side="left")

        btn_ws = ttk.Button(self.frame_client, text="websocket",
                            bootstyle=self.btn_style_list[self.init_btn_random()],
                            cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_ws.pack(padx=btn_pad_x, side="left")

        btn_tcp = ttk.Button(self.frame_client, text="tcp",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_tcp.pack(padx=btn_pad_x, side="left")

        btn_udp = ttk.Button(self.frame_client, text="udp",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_udp.pack(padx=btn_pad_x, side="left")

        btn_ftp = ttk.Button(self.frame_client, text="ftp",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_ftp.pack(padx=btn_pad_x, side="left")

        btn_fastcgi = ttk.Button(self.frame_client, text="fast-cgi",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_fastcgi.pack(padx=btn_pad_x, side="left")

        self.frame_server = ttk.LabelFrame(self.root_frame, text="server模拟",
                                           bootstyle=self.btn_style_list[self.init_btn_random()],
                                           padding=pad_frame)
        self.frame_server.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_http_server = ttk.Button(self.frame_server, text="http",
                                     bootstyle=self.btn_style_list[self.init_btn_random()],
                                     cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_http_server.pack(padx=btn_pad_x, side="left")

        btn_ws_server = ttk.Button(self.frame_server, text="websocket",
                                   bootstyle=self.btn_style_list[self.init_btn_random()],
                                   cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_ws_server.pack(padx=btn_pad_x, side="left")

        btn_tcp_server = ttk.Button(self.frame_server, text="tcp",
                                    bootstyle=self.btn_style_list[self.init_btn_random()],
                                    cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_tcp_server.pack(padx=btn_pad_x, side="left")

        btn_udp_server = ttk.Button(self.frame_server, text="udp",
                                    bootstyle=self.btn_style_list[self.init_btn_random()],
                                    cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_udp_server.pack(padx=btn_pad_x, side="left")

        btn_ftp_server = ttk.Button(self.frame_server, text="ftp",
                                    bootstyle=self.btn_style_list[self.init_btn_random()],
                                    cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_ftp_server.pack(padx=btn_pad_x, side="left")

        btn_fastcgi_server = ttk.Button(self.frame_server, text="fast-cgi",
                                        bootstyle=self.btn_style_list[self.init_btn_random()],
                                        cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_fastcgi_server.pack(padx=btn_pad_x, side="left")

        self.frame_json = ttk.LabelFrame(self.root_frame, text="json",
                                         bootstyle=self.btn_style_list[self.init_btn_random()],
                                         padding=pad_frame)
        self.frame_json.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_json = ttk.Button(self.frame_json, text="json格式化",
                              bootstyle=self.btn_style_list[self.init_btn_random()],
                              cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_json.pack(padx=btn_pad_x, side="left")

        self.frame_crypto = ttk.LabelFrame(self.root_frame, text="加解密",
                                           bootstyle=self.btn_style_list[self.init_btn_random()],
                                           padding=16)
        self.frame_crypto.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_base64 = ttk.Button(self.frame_crypto, text="base64",
                                bootstyle=self.btn_style_list[self.init_btn_random()],
                                cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_base64.pack(padx=btn_pad_x, side="left")

        btn_url = ttk.Button(self.frame_crypto, text="urlencode",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_url.pack(padx=btn_pad_x, side="left")

        btn_aes = ttk.Button(self.frame_crypto, text="AES",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_aes.pack(padx=btn_pad_x, side="left")

        self.frame_app = ttk.LabelFrame(self.root_frame, text="常用app自实现集合",
                                        bootstyle=self.btn_style_list[self.init_btn_random()],
                                        padding=pad_frame)
        self.frame_app.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_qr_code = ttk.Button(self.frame_app, text="QRCode",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()],
                                 command=self.open_qr_code)
        btn_qr_code.pack(padx=btn_pad_x, side="left")

        btn_sql = ttk.Button(self.frame_app, text="数据库",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_sql.pack(padx=btn_pad_x, side="left")

        btn_pic_diy = ttk.Button(self.frame_app, text="P图",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_pic_diy.pack(padx=btn_pad_x, side="left")

        btn_content = ttk.Button(self.frame_app, text="备忘录",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_content.pack(padx=btn_pad_x, side="left")

        btn_hex = ttk.Button(self.frame_app, text="进制转换",
                             bootstyle=self.btn_style_list[self.init_btn_random()],
                             cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_hex.pack(padx=btn_pad_x, side="left")

        btn_weather = ttk.Button(self.frame_app, text="天气预报",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_weather.pack(padx=btn_pad_x, side="left")

        btn_pmeter = ttk.Button(self.frame_app, text="并发压力测试",
                                bootstyle=self.btn_style_list[self.init_btn_random()],
                                cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_pmeter.pack(padx=btn_pad_x, side="left")

        self.frame_doc = ttk.LabelFrame(self.root_frame, text="主流语言文档",
                                        bootstyle=self.btn_style_list[self.init_btn_random()],
                                        padding=pad_frame)
        self.frame_doc.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_doc_js = ttk.Button(self.frame_doc, text="js",
                                bootstyle=self.btn_style_list[self.init_btn_random()],
                                cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_js.pack(padx=btn_pad_x, side="left")

        btn_doc_php = ttk.Button(self.frame_doc, text="php",
                                 bootstyle=self.btn_style_list[self.init_btn_random()],
                                 cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_php.pack(padx=btn_pad_x, side="left")

        btn_doc_golang = ttk.Button(self.frame_doc, text="golang",
                                    bootstyle=self.btn_style_list[self.init_btn_random()],
                                    cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_golang.pack(padx=btn_pad_x, side="left")

        self.frame_framework_doc = ttk.LabelFrame(self.root_frame, text="主流框架文档",
                                                  bootstyle=self.btn_style_list[self.init_btn_random()],
                                                  padding=pad_frame)
        self.frame_framework_doc.pack(padx=row_pad_x, pady=row_pad_y, anchor="w")

        btn_doc_laravel = ttk.Button(self.frame_framework_doc, text="laravel",
                                     bootstyle=self.btn_style_list[self.init_btn_random()],
                                     cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_laravel.pack(padx=btn_pad_x, side="left")

        btn_doc_react = ttk.Button(self.frame_framework_doc, text="react",
                                   bootstyle=self.btn_style_list[self.init_btn_random()],
                                   cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_react.pack(padx=btn_pad_x, side="left")

        btn_doc_react = ttk.Button(self.frame_framework_doc, text="react",
                                   bootstyle=self.btn_style_list[self.init_btn_random()],
                                   cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_react.pack(padx=btn_pad_x, side="left")

        btn_doc_spring_boot = ttk.Button(self.frame_framework_doc, text="spring-boot",
                                         bootstyle=self.btn_style_list[self.init_btn_random()],
                                         cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_spring_boot.pack(padx=btn_pad_x, side="left")

        btn_doc_spring_cloud = ttk.Button(self.frame_framework_doc, text="spring-cloud",
                                          bootstyle=self.btn_style_list[self.init_btn_random()],
                                          cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_spring_cloud.pack(padx=btn_pad_x, side="left")

        btn_doc_spring_cloud = ttk.Button(self.frame_framework_doc, text="spring-cloud",
                                          bootstyle=self.btn_style_list[self.init_btn_random()],
                                          cursor=self.cursor_style_list[self.init_cusor_random()])
        btn_doc_spring_cloud.pack(padx=btn_pad_x, side="left")

        # 打上作者信息
        self.show_author_info()
        # 把主页所有的frame放进list
        self.frame_list = {self.frame_client, self.frame_json, self.frame_crypto, self.frame_app,
                           self.frame_doc, self.frame_framework_doc, self.frame_server}

    # 渲染client：http
    def render_client_http(self):
        self.sec_view = tk.Frame()
        self.sec_view.pack(side=tk.LEFT)
        http(self.sec_view)

    # 渲染二维码页面
    def render_qr_code(self):
        self.sec_view = tk.Frame()
        self.sec_view.pack(side=tk.TOP, anchor=tk.W)
        qrcode_tool(self.sec_view)


    # 清理home控件
    def clear_home(self):
        self.root_frame.destroy()


    # 打开http_client
    def open_http_client(self):
        self.clear_home()
        self.render_client_http()
        self.current_scene = "sec_view"
        # self.show_operate_log("用户进入了client模块:http")

    # 打开二维码
    def open_qr_code(self):
        self.clear_home()
        self.render_qr_code()
        self.current_scene = "sec_view"
        # self.show_operate_log("用户进入了app模块：qrcode")

    # 打上作者大名
    def show_author_info(self):
        label_author = ttk.Label(self.root_frame, text="designed by: Alex-黑白",
                                 bootstyle=self.label_style_list[self.init_label_random()])
        label_author.pack(side=tk.BOTTOM, anchor=tk.E)

        self.change_theme_btn = ttk.Button(self.root_frame, text="切换主题",
                                           command=self.random_theme)
        self.change_theme_btn.pack(side=tk.BOTTOM, anchor=tk.E)

    # 显示一个操作日志
    def show_operate_log(self, msg):
        self.sys_operate_log_Label.configure(text="")
        self.sys_operate_log_Label.configure(text=msg)

    # 通过返回进入主页
    def go_to_home(self, current_scene):
        # 清理子页面控件
        self.__getattribute__(current_scene).destroy()
        # 渲染home
        self.render_home()
        # self.show_operate_log("用户从" + before_scene + "回到了home")


    def listen_keyboard(self, event):
        if event.keysym == "Escape":
            self.go_to_home(self.current_scene)
            self.current_scene = "root_frame"

    # 启动
    def start(self):
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        # 渲染home
        self.render_home()
        # mainloop
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.start()
