#pyhton pytest config

import os
import time
import subprocess
import pytest
from pywinauto import Desktop
import ui_components as ui
import time_components as now

exe_path = r"S:\Recursos_Humanos\Giro.exe"
work_dir = r"S:\Recursos_Humanos"
giro_rh_version = "v1.0.7.1"
giro_rh_database = "001"
giro_rh_password = "CAPAS"
giro_rh_username = ""


def kill_giro():
        os.system("taskkill /F /IM Giro.exe /T")

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


def app_dialog():
        app_dlg = get_current_giro_window()
        app_dlg.type_keys("{ENTER}")

        
def log_in_giro():
        login_window = Desktop(backend="win32").window(title_re="^Giro v.*", class_name="TFLogIn")

        ui.enter_text(login_window, 2, giro_rh_password+now.get_actual_date(), "TCampoStr")
        ui.enter_text(login_window, 4, giro_rh_username, "TCampoStr")
        ui.enter_text(login_window, 3, giro_rh_database, "TCampoStr")
        
        ui.click_button(login_window, "Aceptar")
        error_popup = Desktop(backend="win32").window(title="Aviso !")
        if error_popup.exists(timeout=3):
                error_text = error_popup.window_text()
                error_popup.type_keys("{ENTER}")
                pytest.exit(f"CRITICAL: Login failed.")
        ui.verify_window_closed(login_window, timeout_seconds=3)


def recordatorios_popup():
        homepage_window = get_current_giro_window()
        recordatorios_win = homepage_window.child_window(title="Recordatorios", class_name="TFRecordatorios", found_index=0)
        salir_btn = recordatorios_win.child_window(title="&Salir", class_name="TBitBtn")
        salir_btn.click_input()
       
                
@pytest.fixture(scope="session")
def app_GIRO_RH():
        """
        Open an instance of GIRO RH and start a testing session
        """
        
        subprocess.Popen(exe_path, cwd=work_dir)
        time.sleep(1.5)
        dlg = Desktop(backend="win32").window(
        title_re="^Giro v.*",
        found_index=0
        )
        
        dlg.wait("visible",timeout=10)
        dlg.set_focus()

        app_dialog()
        log_in_giro()
        recordatorios_popup()
        try:
                yield dlg

        finally:
                print("\n[TEARDOWN] Shutting down GIRO RH...")
                kill_giro()
