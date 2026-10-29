import time
import ui_components as ui

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

    def open_screen(self, screen_key, target_title_re):
        """
        Looks up the shortcut in the dictionary and uses ui_components 
        to navigate and return the active child window.
        """
        sequence = ui.SHORTCUTS.get(screen_key)
        
        if not sequence:
            raise KeyError(f"CRITICAL: Shortcut '{screen_key}' not found in dictionary.")
            
        child_window = ui.navigate_menu(self.dashboard, sequence, target_title_re)
        return child_window

    def action_insert(self,active_window):
        active_window.type_keys("{F3}")
        time.sleep(0.5)

    def action_save(self,active_window):
        active_window.type_keys("{F2}")
        time.sleep(0.5)

    def action_export_excel(self,active_window):
        active_window.type_keys("^E")
        time.sleep(0.5)

    def action_cancel_changes(self,active_window):
        active_window.type_keys("{ESC}")
        time.sleep(0.5)

    def action_exit(self,active_window):
        active_window.type_keys("^{F4}")
        time.sleep(0.5)


        
