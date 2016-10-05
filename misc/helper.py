import os
from element.error_dialog import ErrorDialog


def exit_app():
    exit()


def one_up(directory):
    head, tail = os.path.split(directory.path())
    return head


def display_error(message):
    dialog = ErrorDialog(message)
    dialog.exec_()
