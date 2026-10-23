import pytest
import time
import ui_components as ui
from pages.base_mdi import BaseMDIWindow

class TestGiroNavigation:

    def test_homepage_navigation(self, app_GIRO_RH):
        """
        Verifies all top-level menus open and close without crashing the application.
        """
        page = BaseMDIWindow(app_GIRO_RH)
        
        menu_shortcuts = ["%e", "%c", "%r", "%p", "%o", "%a", "%v", "%y"]
        
        try:
            for shortcut in menu_shortcuts:
                page.preview_menu(shortcut)
            
        except Exception as e:
            pytest.fail(f"Navigation sequence failed: {e}")
