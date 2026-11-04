# ui_components.py
import time
from pywinauto import Desktop
from pywinauto.controls.win32_controls import EditWrapper, ComboBoxWrapper

SHORTCUTS = {
# --- CATÁLOGOS > GENERAL ---
    
    "estructura_empresa": ["%c", "g", "e"],
    "registros_patronales": ["%c", "g", "r"],
    "sucursales": ["%c", "g", "s"],
    "centros_costo": ["%c", "g", "c"],
    "departamentos": ["%c", "g", "d"],
    
    "calendario_dias_inhabiles": ["%c", "g", "a"], 
    "tipos_empleados": ["%c", "g", "t"],
    "puestos": ["%c", "g", "p"],
    
    "salarios_minimos": ["%c", "g", "l"], # 'l' en Salarios
    "tipos_ausentismo": ["%c", "g", "o"], # 'o' en Tipos
    "modificaciones_salario": ["%c", "g", "m"],
    "causas_baja": ["%c", "g", "u"], # 'u' en Causas

    "turnos": ["%c", "g", "t", "{ENTER}"], # Comparte 'T' con Tipos de Empleados
    "esquemas_rotacion": ["%c", "g", "e", "e", "{ENTER}"], # Comparte 'E' con Estructura
    "turnos_rotativos": ["%c", "g", "v"], # 'v' en Rotativos
    "calendario_turnos_rotativos": ["%c", "g", "c", "c", "{ENTER}"], # Comparte 'C' con Centros de Costo
    "turnos_inteligentes": ["%c", "g", "i"]
    
}

def get_current_giro_window(title):
        """
        Pauses briefly, rescans the desktop for the active Giro window,
        and returns the fresh window object.
        """
        time.sleep(1.5)
        new_window = Desktop(backend="win32").window(title_re=title, found_index=0)
        new_window.wait("visible", timeout=5)
        new_window.set_focus()
        return new_window

def click_button(window, button_title):
    """
    Locates a standard GIRO RH button by its title and clicks it.
    """
    btn = window.child_window(title=button_title, class_name="TBitBtn")
    btn.wait("visible", timeout=5)
    btn.click_input()
    
def enter_text_t(window, target_index, text_to_type, target_class="TCampoStr"):
    """
    Locates a text box by its ID and types the specified text.
    """
    # Assuming text boxes in Delphi use 'TCampoStr' or 'Edit'
    txt_box = window.child_window(found_index=target_index, class_name=target_class)
    txt_box.wait("visible", timeout=5)
    #txt_box.set_focus()
    txt_box.type_keys(f"^a{{BACKSPACE}}{text_to_type}", with_spaces=True)

def enter_text_tdb(panel, target_index, text_to_type, target_class="TDBCampoStr"):
    """
    Locates a control by index and forces text insertion bypassing Delphi restrictions.
    """
    raw_control = panel.child_window(found_index=target_index, class_name=target_class)
    raw_control.wait("visible", timeout=5)
    txt_box = EditWrapper(raw_control.wrapper_object())
    try:
        txt_box.set_text(text_to_type)
    except Exception:
        # Fallback to direct character messaging if Delphi blocks the text injection
        txt_box.send_chars(text_to_type)
        
def enter_number_tdb(panel, target_index, text_to_type, target_class="TDBCampoStr"):
    """
    Locates a control by index and forces text insertion bypassing Delphi restrictions.
    """
    raw_control = panel.child_window(found_index=target_index, class_name=target_class)
    raw_control.wait("visible", timeout=5)
    txt_box = EditWrapper(raw_control.wrapper_object())
    try:
        txt_box.set_text(text_to_type)
    except Exception:
        # Fallback to direct character messaging if Delphi blocks the text injection
        txt_box.send_chars(text_to_type)
        
def select_text_tdb(panel, target_index, option_text, target_class="TDBCampoComb"):
    """
    Locates a ComboBox and select an valid option.
    """
    raw_control = panel.child_window(found_index=target_index, class_name=target_class)
    raw_control.wait("visible", timeout=5)
    txt_box = ComboBoxWrapper(raw_control.wrapper_object())
    txt_box.select(option_text)

def select_option_toolbar(window, target_index, option):
    """
    Locates the nearest toolbar option/button and press it. 
    """
    # Assuming tool bar in Delpi used 'TooolBar' and option as 'Buttons'
    tool_bar = window.child_window(found_index=target_index, class_name="TToolBar")
    tool_bar.wait("visible",timeout=3)
    tool_bar.press_button(option)

def catch_warning_popup(popup_title="Aviso !", button_title="Aceptar", wait_time=3):
    """
    Searches the top-level Desktop for a pop-up warning, dismisses it, 
    and returns the extracted error message safely.
    """
    desktop = Desktop(backend="win32")
    popup = desktop.window(title=popup_title)
    
    if popup.exists(timeout=wait_time):
        try:
            raw_texts = popup.texts()
            filtered_texts = [t for t in raw_texts if t and t not in (popup_title, button_title)]
            error_msg = " ".join(filtered_texts)
            if not error_msg.strip():
                error_msg = "Popup detected but no readable text found."
        except Exception:
            error_msg = "Warning text could not be extracted."  
        btn = popup.child_window(title=button_title)
        btn.click()
        
        popup.wait_not("visible", timeout=wait_time)
        return error_msg
        
    return None
    
def handle_calendar_popup(popup_title="Calendario", action="today", wait_time=3):
    """
    Searches the top-level Desktop for the calendar window, selects a date 
    (clicking 'Today' by default), and confirms it.
    """
    desktop = Desktop(backend="win32")
    calendar_popup = desktop.window(title=popup_title)
    
    if calendar_popup.exists(timeout=wait_time):
        calendar_popup.set_focus()
        try:
            if action == "today":
                calendar_popup.child_window(title="Today Button").click()
            else:
                calendar_popup.type_keys("{ENTER}")
        except Exception:
            calendar_popup.type_keys("{ENTER}")
            
        calendar_popup.wait_not("visible", timeout=wait_time)
        return True
        
    return False
    
def navigate_menu(window, key_sequence, target_title):
    window.set_focus()
    for key in key_sequence:
        window.type_keys(key)
        time.sleep(0.5)
    new_window = window.child_window(title_re=target_title)
    new_window.wait("visible", timeout=10)
    new_window.set_focus()
    return new_window

def verify_window_closed(window, timeout_seconds=5):
    """Waits for a window to disappear from the screen."""
    window.wait_not("visible", timeout=timeout_seconds)
    return True

