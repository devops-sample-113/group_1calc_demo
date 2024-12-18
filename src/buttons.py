import flet as ft


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=True):
        super().__init__(text=text, expand=expand, on_click=button_clicked)
        self.data = text
        self.height = 500
        self._type = ""

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        assert value in ["digit", "operator",
                         "action","rand"], "Invalid type: must be 'rand', 'digit', 'operator', or 'action'."
        self._type = value


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, value=0, expand=True):
        super().__init__(text, button_clicked, expand)
        self.type = "digit"
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE
        self.value = value


class OperatorButton(CalcButton):
    def __init__(self, text, button_clicked, operations=None):
        super().__init__(text, button_clicked)
        self.type = "operator"
        self.bgcolor = ft.Colors.BLUE_GREY_200
        self.color = ft.Colors.BLACK
        self.operations = operations


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked, action=None):
        super().__init__(text, button_clicked)
        self.type = "action"
        self.bgcolor = ft.Colors.BLUE_GREY_200
        self.color = ft.Colors.BLACK
        self.action = action

class RandomButton(CalcButton):
    def __init__(self, text, button_clicked, value=0, expand=True):
        super().__init__(text, button_clicked, expand)
        self.type = "rand"
        self.bgcolor = ft.Colors.BLUE_GREY_500
        self.color = ft.Colors.BLACK
        self.value = value

