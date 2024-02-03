from PySide6.QtCore import QEasingCurve


class UiFunctions(object):

    @staticmethod
    def extend_animation(self, max_value: int, min_value: int) -> None:
        """
        组件展开收起动画
        :param self:
        :param max_value:
        :param min_value:
        :return:
        """
        self.btn_home.setText('annn')
        width = self.width()
        if width == max_value:
            width_extended = min_value
        elif width == min_value:
            width_extended = max_value
        else:
            return
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
