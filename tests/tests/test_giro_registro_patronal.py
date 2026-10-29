import pytest
import time
import ui_components as ui
from pages.base_mdi import BaseMDIWindow

class TestGiroRegistroPatronal:
    def test_open_rp_window(self, app_GIRO_RH):
        mock_data = {
        "Clave": "03",
        "Nombre": "PRUEBA SA. DE C.V.",
        "Reg_Patronal": "P1323215135",
        "Representante": "JUAN LOPEZ",
        "RFC": "PBD2135465451",
        "Regimen_Fiscal": "REGIMEN DE LA EMPRESA",
        "Clase": "1",
        "Guia_Magnetica": "1321654654",
        "Zona_Economica": "B",
        "RT": "0.6",
        "Calle": "CALLE DE PRUEBA",
        "Numero": "0001",
        "Int": "",
        "Colonia": "OCAMPO",
        "CP": "00000",
        "Delegacion": "FCO VILLA",
        "Municipio": "SANTIAGO",
        "Estado": "CAMPECHE",
        "Ciudad": "CAMPECHE",
        "Fax": "135484632184",
        "Telefono": "218465216384"
        }
        
        """
        Opens the RP window and create a new registerfrom "xxx.xlsx"
        """
        page = BaseMDIWindow(app_GIRO_RH)
        try:
            rp_window = page.open_screen(screen_key="registros_patronales",target_title_re="Catálogo de Registros Patronales.*")
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"Open RP window failed, {e}")
        """
        Opens the RP window and create a new registerfrom "xxx.xlsx"
        """
        try:
            page.action_insert(rp_window)
            rp_window.print_control_identifiers(filename="ui_rp_debug.txt")
            time.sleep(0.5)
            ui.enter_text(rp_window,20,mock_data["Clave"],class_name="TDBCampoStr")
            ui.enter_text(rp_window,19,mock_data["Nombre"],class_name="TDBCampoStr")
            ui.enter_text(rp_window,18,mock_data["RFC"],class_name="TDBCampoStr")
            ui.enter_text(rp_window,17,mock_data["Reg_Patronal"],class_name="TDBCampoStr")
            ui.enter_text(rp_window,5,mock_data["Representante"],class_name="TDBCampoStr")
            ui.enter_text(rp_window,4,mock_data["Regimen_Fiscal"],class_name="TDBCampoStr")

        except Exception as e:
            pytest.fail(f"Insertion process failed: {e}")
        
        
