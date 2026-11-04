import pytest
import time
import ui_components as ui
from pages.base_mdi import BaseMDIWindow

class TestGiroSucursales():
    @pytest.mark.code(reason="Coding more tests")
    def test_open_sucursales_window(self,app_GIRO_RH):
        """
        Opens the Sucursales window and create a new register from "mock_data"
        """
        page = BaseMDIWindow(app_GIRO_RH)
        try:
            suc_window = page.open_screen(screen_key="sucursales",target_title_re="Catálogo de Sucursales.*")
            time.sleep(0.5)
            page.action_insert(suc_window)
            forced_enter_text(rp_window,20,"Hello World")
            forced_enter_text(rp_window,19,"Hello World")
            forced_enter_text(rp_window,18,"Hello World")
            forced_enter_text(rp_window,17,"Hello World")
            forced_enter_text(rp_window,16,"Hello World")
            forced_enter_text(rp_window,15,"Hello World")
            
        except Exception as e:
            pytest.fail(f"Open RP window failed, {e}")
