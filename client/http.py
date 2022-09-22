import json

import requests
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox


class http:
    def __init__(self, app):
        # url变量
        self.url_var = ttk.StringVar()

        # http client container
        frame = ttk.Frame(master=app)
        frame.grid(column=0, row=1)

        # request容器
        req_header_frame = ttk.LabelFrame(master=frame, text="request")
        req_header_frame.grid(column=0, row=0, padx=8)

        # 下拉框
        self.options = ttk.Combobox(master=req_header_frame,
                                    bootstyle="primary",

                                    values=['GET', 'POST'],
                                    width=6)
        self.options.current(0)
        self.options.grid(column=0, row=1, padx=8, pady=4)

        # url
        self.url_entry = ttk.Entry(master=req_header_frame,
                                   bootstyle="primary",
                                   textvariable=self.url_var,
                                   width=82)
        self.url_entry.grid(column=1, row=1)
        self.url_entry.insert('0',
                              "https://json.tewx.cn/json/API_kdd531mytfdzm06i?sdAS1dsnuUa3sd=190001&Jsdh4bajs99dii=sohpuisypf4nfaei")

        # request_btn
        req_btn = ttk.Button(master=req_header_frame,
                             text="请求",
                             command=self.req,
                             bootstyle="success")
        req_btn.grid(column=2, row=1, padx=8, ipadx=12)

        # 参数容器
        param_frame = ttk.LabelFrame(master=frame, text="param")
        param_frame.grid(column=0, row=1)

        # 参数面板
        param_book = ttk.Notebook(master=param_frame)
        param_book.grid(column=0, row=0, padx=8)

        # header
        param_book.add(ttk.Label(text="panel a", width=102), text="header")

        # param
        param_param_text = ttk.Text(height=2)
        param_book.add(param_param_text, text="param")

        # body
        param_body_text = ttk.Text(height=2)
        param_book.add(param_body_text, text="body")

        # response container
        resp_frame = ttk.LabelFrame(master=frame, text="response")
        resp_frame.grid(column=0, row=2, padx=8)

        self.resp_text = ttk.Text(master=resp_frame, width=102)
        # text.delete("0.0",'end') #删除内容
        self.resp_text.insert('insert', '这里显示请求响应结果')
        self.resp_text.see(ttk.END)
        self.resp_text.grid(column=0, row=0, padx=8)

    def req(self):
        url_value = self.url_var.get()
        if len(url_value) < 7:
            self.url_entry.configure(bootstyle="danger")
            Messagebox.show_warning(message="错误的请求地址",
                                    title="提示")
        else:
            resp = requests.get(url_value)
            self.resp_text.delete("0.0", 'end')
            self.resp_text.insert('insert',
                                  json.dumps(json.loads(resp.content), sort_keys=True, indent=4, ensure_ascii=False))
