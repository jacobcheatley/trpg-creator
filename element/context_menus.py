from PyQt5.QtWidgets import QMenu


def build(actions):
    result = QMenu()
    for action in actions:
        label, function = action
        new_action = result.addAction(label)
        new_action.triggered.connect(function)
    return result
