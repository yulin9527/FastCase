class Functions:
    @staticmethod
    def set_widget_marg(obj, spacing: int = 0, left: int = 0, top: int = 0, right: int = 0, bottom: int = 0):
        obj.setContentsMargins(left, top, right, bottom)
        obj.setSpacing(spacing)
