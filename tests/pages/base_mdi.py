import time

class BaseMDIWindow:
    def __init__(self, dashboard_window):
        self.dashboard = dashboard_window

    def preview_menu(self, shortcut_key):
        """
        Opens a top-level menu using a shortcut and closes it immediately.
        """
        self.dashboard.set_focus()
        self.dashboard.type_keys(shortcut_key)
        time.sleep(1)
        self.dashboard.type_keys("{ESC}")
