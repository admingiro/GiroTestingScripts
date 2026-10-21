# ui_components.py
import time

class MenuPaths():
    ALTAS_EMPLEADOS = ["%e","a"]

def click_button(window, button_title):
    """Locates a standard GIRO RH button by its title and clicks it."""
    btn = window.child_window(title=button_title, class_name="TBitBtn")
    btn.wait("visible", timeout=5)
    btn.click_input()
    
def enter_text(window, target_index, text_to_type):
    """Locates a text box by its ID and types the specified text."""
    # Assuming text boxes in Delphi use 'TCampoStr' or 'Edit'
    txt_box = window.child_window(found_index=target_index, class_name="TCampoStr")
    txt_box.wait("visible", timeout=5)
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
    new_window = Desktop(backend="win32").window(title_re=target_title)
    new_window.wait("visible", timeout=3)
    new_window.set_focus()
    return new_window

def verify_window_closed(window, timeout_seconds=5):
    """Waits for a window to disappear from the screen."""
    window.wait_not("visible", timeout=timeout_seconds)
    return True

