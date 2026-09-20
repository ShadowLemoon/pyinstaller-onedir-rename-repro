"""Minimal repro: onedir contents directory cannot be renamed while the app runs."""
import time

from PySide6 import QtWidgets

import qfluentwidgets  # noqa: F401  (PySide6-Fluent-Widgets)

app = QtWidgets.QApplication([])
print('app running', flush=True)
time.sleep(600)
