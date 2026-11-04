import pytest
import time
import ui_components as ui
from pywinauto import Desktop
from pages.base_mdi import BaseMDIWindow

class TestGiroRegistroPatronal:
    @pytest.mark.debug(reason="Not finished")
    
    def test_open_rp_window(self, app_GIRO_RH):
        mock_data = {
        "Clave": "17",
        "Nombre": "PRUEBA SA. DE C.V.",
        "Reg_Patronal": "P1323215135",
        "Representante": "JUAN LOPEZ",
        "RFC": "PBD2135465451",
        "Regimen_Fiscal": "601",
        "Clase": "5",
        "Guia_Magnetica": "1321654654",
        "Zona_Economica": "B",
        "RT": "0.6142",
        "Calle": "CALLE DE PRUEBA",
        "Numero": "0001",
        "Int": "13",
        "Colonia": "OCAMPO",
        "CP": "99999",
        "Delegacion": "FCO VILLA",
        "Municipio": "SANTIAGO",
        "Estado": "CAMPECHE",
        "Ciudad": "CAMPECHE",
        "Fax": "135484632184",
        "Telefono": "218465216384",
        "Origen": "IM",
        "Nom_Fiscal":"PRUEBA"
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

        try:
            #Opens the editon tab
            page.action_insert(rp_window)
            edition_tab = rp_window.child_window(title="&2. Edición", class_name="TTabSheet")
            edition_panel = edition_tab.child_window(class_name="TPanel")
            time.sleep(0.5)
            ui.enter_text_tdb(edition_panel,19,mock_data["Clave"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,18,mock_data["Nombre"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,17,mock_data["Reg_Patronal"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,16,mock_data["Representante"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,15,mock_data["Guia_Magnetica"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,14,mock_data["Fax"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,13,mock_data["Telefono"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,12,mock_data["Municipio"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,11,mock_data["Delegacion"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,10,mock_data["CP"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,9,mock_data["Colonia"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,8,mock_data["Int"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,7,mock_data["Numero"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,6,mock_data["Calle"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,5,mock_data["Clase"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,4,mock_data["RFC"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,3,mock_data["Regimen_Fiscal"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,2,mock_data["Ciudad"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,1,mock_data["Origen"],target_class="TDBCampoStr")
            ui.enter_text_tdb(edition_panel,0,mock_data["Nom_Fiscal"],target_class="TDBCampoStr")
 
            ui.enter_text_tdb(edition_panel,0,mock_data["RT"],target_class="TDBCampoNum")
            
            ui.select_text_tdb(edition_panel,1,mock_data["Zona_Economica"],target_class="TDBCampoComb")
            ui.select_text_tdb(edition_panel,0,mock_data["Estado"],target_class="TDBCampoComb")
            
        except Exception as e:
            warning_popup = app_GIRO_RH.window(class_name="Advertencia !")
            error_message = warning_popup.child_window(class_name="TStaticText").window_text()
            pytest.fail(f"CRITICAL WARNING: Insertion process failed: {error_message}")
        try:
            page.action_save(edition_tab)
            warning_text = ui.catch_warning_popup(popup_title="Aviso !", button_title="Aceptar")
    
            if warning_text:
                print(f"Warning handled: '{warning_text}'")
                calendar_handled = ui.handle_calendar_popup(popup_title="Calendario", action="today")
                if not calendar_handled:
                    pytest.fail("Save process blocked: Calendar window did not appear after warning.")
        except Exception as e:
            pytest.fail(f"Save process failed due to a system error: {e}")
        
