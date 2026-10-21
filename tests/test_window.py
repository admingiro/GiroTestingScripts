import ui_components as ui
import time_components as now
from pywinauto import Desktop
import pytest
import time

giro_rh_database = "001"
giro_rh_password = "CAPAS"
giro_rh_username = ""

def get_current_giro_window():
        """
        Pauses briefly, rescans the desktop for the active Giro window,
        and returns the fresh window object.
        """
        time.sleep(1.5)
        new_window = Desktop(backend="win32").window(title_re="^Giro v.*", found_index=0)
        new_window.wait("visible", timeout=5)
        new_window.set_focus()
        return new_window

class TestGiro:

        def test_open_GIRO(self, app_GIRO_RH):
                assert app_GIRO_RH.exists()

        def test_click_accept(self, app_GIRO_RH):
                assert app_GIRO_RH.type_keys("{ENTER}")

        def test_log_in_giro(self, app_GIRO_RH):
                login_window = Desktop(backend="win32").window(title_re="^Giro v.*", class_name="TFLogIn")

                ui.enter_text(login_window, 2, giro_rh_password+now.get_actual_date())
                ui.enter_text(login_window, 4, giro_rh_username)
                ui.enter_text(login_window, 3, giro_rh_database)
                
                ui.click_button(login_window, "Aceptar")
                error_popup = Desktop(backend="win32").window(title="Aviso !")
                if error_popup.exists(timeout=3):
                        error_text = error_popup.window_text()
                        error_popup.type_keys("{ENTER}")
                        #pytest.xfail(reason="CRITICAL: Login failed. Aborting testing flow. Application returned: {error_text}")
                        pytest.exit(f"CRITICAL: Login failed.")
                assert ui.verify_window_closed(login_window, timeout_seconds=3)
                
        def test_recordatorios_popup(self):
                homepage_window = get_current_giro_window()
                recordatorios_win = homepage_window.child_window(title="Recordatorios", class_name="TFRecordatorios", found_index=0)
                salir_btn = recordatorios_win.child_window(title="&Salir", class_name="TBitBtn")
                salir_btn.click_input()
                
        def test_homepage_navigation(self, app_GIRO_RH):
                homepage_window = get_current_giro_window()
                try:
                        homepage_window.type_keys("%e")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%c")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%r")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%p")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%o")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%a")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%v")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%y")
                        time.sleep(1)
                        homepage_window.type_keys("{ESC}")
                        homepage_window.type_keys("%b")
                        time.sleep(1)
                        ui.click_button(homepage_window, "Close")

                except Exception:
                        assert False

##	def test_click_close(self, app_GIRO_RH):
##                login_window = get_current_giro_window()
##                ui.click_button(login_window, "Salir")
##                ui.verify_window_closed(login_window)
                
