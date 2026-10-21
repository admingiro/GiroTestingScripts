#pyhton pytest config

from pywinauto import Desktop
import pytest
import subprocess
import time
import os

exe_path = r"S:\Recursos_Humanos\Giro.exe"
work_dir = r"S:\Recursos_Humanos"
giro_rh_version = "v1.0.6.100"


def kill_giro():
        os.system("taskkill /F /IM Giro.exe /T")

@pytest.fixture(scope="session")
def app_GIRO_RH():
        """
        Open an instance of GIRO RH and start a testing session
        """

        subprocess.Popen(exe_path, cwd=work_dir)
        time.sleep(1)

        dlg = Desktop(backend="win32").window(
        title_re="^Giro v.*",
        found_index=0
        )

        dlg.wait("visible",timeout=10)
        dlg.set_focus()

        try:
                yield dlg
        finally:
                print("\n[TEARDOWN] Shutting down GIRO RH...")
                kill_giro()
