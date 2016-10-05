import os
from element.error_dialog import ErrorDialog
import json


def exit_app():
    exit()


def one_up(directory):
    head, tail = os.path.split(directory)
    return head


def display_error(message):
    dialog = ErrorDialog(message)
    dialog.exec_()


def debug_action(text):
    def inner():
        print(text)

    return inner


def show_simple_dialog(cls):
    def inner():
        dialog = cls()
        dialog.exec_()

    return inner


def get_json_data(file_location):
    with open(file_location, 'r') as in_file:
        return json.load(in_file)