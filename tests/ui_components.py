# ui_components.py
import time
from pywinauto import Desktop

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

def click_button(window, button_title):
    """Locates a standard GIRO RH button by its title and clicks it."""
    btn = window.child_window(title=button_title, class_name="TBitBtn")
    btn.wait("visible", timeout=5)
    btn.click_input()
    
def enter_text(window, target_index, text_to_type, target_class):
    """Locates a text box by its ID and types the specified text."""
    # Assuming text boxes in Delphi use 'TCampoStr' or 'Edit'
    txt_box = window.child_window(found_index=target_index, class_name=target_class)
    txt_box.wait("visible", timeout=3)
    txt_box.set_focus()
    txt_box.type_keys(f"^a{{BACKSPACE}}{text_to_type}", with_spaces=True)

def select_option_toolbar(window, target_index, option):
    """Locates the nearest toolbar option/button and press it. """
    # Assuming tool bar in Delpi used 'TooolBar' and option as 'Buttons'
    tool_bar = window.child_window(found_index=target_index, class_name="TToolBar")
    tool_bar.wait("visible",timeout=3)
    tool_bar.press_button(option)

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

