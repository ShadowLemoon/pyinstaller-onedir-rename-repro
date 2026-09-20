"""Minimal repro: onedir contents directory cannot be renamed while the app runs.

Importing `setuptools` is what makes the difference: PyInstaller then pulls in the
`pyi_rth_setuptools` runtime hook, which imports setuptools at application startup.
With that in the mix, the running app keeps a handle on `.runtime/base_library.zip`.
"""
import time

from PySide6 import QtWidgets

import qfluentwidgets  # noqa: F401  (PySide6-Fluent-Widgets)
import setuptools  # noqa: F401

app = QtWidgets.QApplication([])
print('app running', flush=True)
time.sleep(600)
