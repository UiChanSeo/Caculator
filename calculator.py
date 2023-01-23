import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

from dialog import Dialog
from button import ButtonInfo


operate={
    "+": lambda a,b:round(float(a)+float(b),2),
    "-": lambda a,b:round(float(a)-float(b),2),
    "*": lambda a,b:round(float(a)*float(b),2),
    "/": lambda a,b:round(float(a)/float(b),2),
    "%": lambda a,b:round(float(a)%float(b),2) 
}


class Calculator(Dialog):
    _text_view= None

    def update_text_view(self):
        if len(self.op_str) == 0:
            display_text = self.left_str
        else:
            display_text = self.left_str 
            display_text += ' '
            display_text += self.op_str
            display_text += ' '
            display_text += self.right_str
        self._text_view.delete("1.0", "end")
        self._text_view.insert(INSERT, display_text)

    def on_pressed_num(self, num_str):
        if num_str.isnumeric() or num_str == '.':
            if len(self.op_str) == 0:
                self.left_str += num_str
            else:
                self.right_str += num_str
            self.update_text_view()

    def reset(self):
        self.left_str = ''
        self.right_str = ''
        self.op_str = ''

    def op_equal(self):
        result = 0
        if len(self.left_str) == 0:
            result = "0"
        elif len(self.right_str) == 0:
            result = self.left_str
        else:
            result = operate[self.op_str](self.left_str, self.right_str)
    
        self.reset()

        self._text_view.insert(INSERT, " = "+str(result))

    def op_clear(self):
        self.reset()
        self._text_view.delete("1.0", "end")

    def op_erase(self):
        if len(self.right_str) > 0:
            self.right_str = self.right_str[:-1]
        elif len(self.op_str) > 0:
            self.op_str = ''
        elif len(self.left_str) > 0:
            self.left_str = self.left_str[:-1]
        else:
            self.reset()
        self.update_text_view()

    def op_others(self):
        self.update_text_view()

    def on_pressed_op(self, op_str):
        if op_str == "=":
            self.op_equal()
        elif op_str == "C":
            self.op_clear()
        elif op_str == "<":
            self.op_erase()
        else:
            self.op_str = op_str
            self.op_others()
    
    def __init__(self):
        super().__init__()

        self._is_calc_ended = False
        self._left_str = ''
        self._right_str = ''
        self._op_str = ''
        self._text_view = self.draw_text_view(root=self._window)

        self._btns = self.draw_buttons(root=self._window,
                                       dlg_width=self._window_width)

    @property
    def left_str(self):
        return self._left_str

    @left_str.setter
    def left_str(self, val):
        self._left_str = val
        
    @property
    def right_str(self):
        return self._right_str

    @right_str.setter
    def right_str(self, val):
        self._right_str = val
    
    @property
    def op_str(self):
        return self._op_str

    @op_str.setter
    def op_str(self, val):
        self._op_str = val

    def draw_button(self, root: Tk, button, width):

        btn=tkinter.Button(root,
                           text=button.text,
                           width=button.width,
                           command=lambda: button.callback(button.text))
        btn.grid(row=button.row, column=button.col)
        return btn
    
    def draw_buttons(self, root: Tk, dlg_width)->[]:
        width = (int(dlg_width / 4) % 10)
        buttons = [
            ButtonInfo("<", 1, 0, width, self.on_pressed_op),
            ButtonInfo("C", 1, 1, width, self.on_pressed_op),
            ButtonInfo("%", 1, 2, width, self.on_pressed_op),
            ButtonInfo("/", 1, 3, width, self.on_pressed_op),
            ButtonInfo("7", 2, 0, width, self.on_pressed_num),
            ButtonInfo("8", 2, 1, width, self.on_pressed_num),
            ButtonInfo("9", 2, 2, width, self.on_pressed_num),
            ButtonInfo("*", 2, 3, width, self.on_pressed_op),
            ButtonInfo("4", 3, 0, width, self.on_pressed_num),
            ButtonInfo("5", 3, 1, width, self.on_pressed_num),
            ButtonInfo("6", 3, 2, width, self.on_pressed_num),
            ButtonInfo("-", 3, 3, width, self.on_pressed_op),
            ButtonInfo("1", 4, 0, width, self.on_pressed_num),
            ButtonInfo("2", 4, 1, width, self.on_pressed_num),
            ButtonInfo("3", 4, 2, width, self.on_pressed_num),
            ButtonInfo("+", 4, 3, width, self.on_pressed_op),
            ButtonInfo("0", 5, 0, width, self.on_pressed_num),
            ButtonInfo(".", 5, 2, width, self.on_pressed_num),
            ButtonInfo("=", 5, 3, width, self.on_pressed_op)]

        btn_list = []
        for button in buttons:
            btn_list.append(self.draw_button(root=root,
                                             button=button,
                                             width=width))
        return btn_list 
    
    def draw_text_view(self, root: Tk):
        text_view= tkinter.Text(root,
                                height=self.display_height,
                                width=self.display_width, wrap=None)
        text_view.grid(row=0, column=0, columnspan=4, sticky="ew")
        return text_view
    
    def show(self):
        if self._window is not None:
            self._window.mainloop()

