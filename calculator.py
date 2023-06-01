import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk();
        self.window.geometry("300x420")
        self.window.title("Calculator")
        self.window.minsize(300, 420)

        self.var1 = tk.StringVar()
        self.var1.set("")
        self.text_area = tk.Entry(self.window, textvariable=self.var1, font=('Arial', 60), justify='right')
        self.text_area.pack(fill='both', pady=40,)

        self.btn_frame = tk.Frame(self.window, cursor='dot')
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)
        self.btn_frame.columnconfigure(3, weight=1)

        self.btn9 = tk.Button(self.btn_frame, text="9", font=('Arial', 18))
        self.btn9.bind("<Button-1>", self.click)
        self.btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(self.btn_frame, text="8", font=('Arial', 18))
        self.btn8.bind("<Button-1>", self.click)
        self.btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.btn_frame, text="7", font=('Arial', 18))
        self.btn7.bind("<Button-1>", self.click)
        self.btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.btn_frame, text="6", font=('Arial', 18))
        self.btn6.bind("<Button-1>", self.click)
        self.btn6.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(self.btn_frame, text="5", font=('Arial', 18))
        self.btn5.bind("<Button-1>", self.click)
        self.btn5.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.btn_frame, text="4", font=('Arial', 18))
        self.btn4.bind("<Button-1>", self.click)
        self.btn4.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.btn_frame, text="3", font=('Arial', 18))
        self.btn3.bind("<Button-1>", self.click)
        self.btn3.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.btn_frame, text="2", font=('Arial', 18))
        self.btn2.bind("<Button-1>", self.click)
        self.btn2.grid(row=4, column=1, sticky=tk.W + tk.E)

        self.btn1 = tk.Button(self.btn_frame, text="1", font=('Arial', 18))
        self.btn1.bind("<Button-1>", self.click)
        self.btn1.grid(row=4, column=0, sticky=tk.W + tk.E)

        self.btn0 = tk.Button(self.btn_frame, text="0", font=('Arial', 18))
        self.btn0.bind("<Button-1>", self.click)
        self.btn0.grid(row=5, column=1, sticky=tk.W + tk.E)

        self.btnDot = tk.Button(self.btn_frame, text=".", font=('Arial', 18))
        self.btnDot.bind("<Button-1>", self.click)
        self.btnDot.grid(row=5, column=0, sticky=tk.W + tk.E)

        self.btn_eql = tk.Button(self.btn_frame, text="=", font=('Arial', 18))
        self.btn_eql.bind("<Button-1>", self.click)
        self.btn_eql.grid(row=5, column=2, sticky=tk.W + tk.E)

        self.btn_add = tk.Button(self.btn_frame, text="+", font=('Arial', 18))
        self.btn_add.bind("<Button-1>", self.click)
        self.btn_add.grid(row=5, column=3, sticky=tk.W + tk.E)

        self.btn_sub = tk.Button(self.btn_frame, text="-", font=('Arial', 18))
        self.btn_sub.bind("<Button-1>", self.click)
        self.btn_sub.grid(row=4, column=3, sticky=tk.W + tk.E)

        self.btn_mul = tk.Button(self.btn_frame, text="x", font=('Arial', 18))
        self.btn_mul.bind("<Button-1>", self.click)
        self.btn_mul.grid(row=3, column=3, sticky=tk.W + tk.E)

        self.btn_div = tk.Button(self.btn_frame, text="/", font=('Arial', 18))
        self.btn_div.bind("<Button-1>", self.click)
        self.btn_div.grid(row=2, column=3, sticky=tk.W + tk.E)

        self.btn_mod1 = tk.Button(self.btn_frame, text="%", font=('Arial', 18))
        self.btn_mod1.bind("<Button-1>", self.click)
        self.btn_mod1.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.btn_right_bracket = tk.Button(self.btn_frame, text=")", font=('Arial', 18))
        self.btn_right_bracket.bind("<Button-1>", self.click)
        self.btn_right_bracket.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btn_left_bracket = tk.Button(self.btn_frame, text="(", font=('Arial', 18))
        self.btn_left_bracket.bind("<Button-1>", self.click)
        self.btn_left_bracket.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.btn_clear_all = tk.Button(self.btn_frame, text="CA", font=('Arial', 18))
        self.btn_clear_all.bind("<Button-1>", self.click)
        self.btn_clear_all.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn_frame.pack(fill='x', side='bottom')

        self.window.mainloop();
        

    def click(self, event):
        self.var1;
        text = event.widget.cget("text");
        print("text:-", text)

        if text == "=":
            if self.var1.get().isdigit():
                value = int(self.var1.get())
            else:
                try:
                    value = eval(self.var1.get())
                except Exception as e:
                    print("error:- ", e)
                    
            self.var1.set(value)
            self.text_area.update()
        elif text == "CA":
            self.var1.set("")
            self.text_area.update()
        else:
            self.var1.set(self.var1.get()+text)
            self.text_area.update()


Calculator()
