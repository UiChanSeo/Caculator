class ButtonInfo:
    def __init__(self, text, row, col, width, callback_fn):
        self._text = text
        self._row = row
        self._col = col
        self._width = width
        self._callback_fn = callback_fn


    @property
    def text(self):
        return self._text
    
    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col
    
    @property
    def width(self):
        return self._width

    @property
    def callback(self):
        return self._callback_fn
