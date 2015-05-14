from .. import ui
from .raw_input_mocker import rawinput
ui.raw_input = rawinput
temp_ui = ui.Ui()
def test_prompt():
    assert temp_ui.prompt("testing") == "test"

def test_get_details():
    assert temp_ui.get_details()==('test','test','test','test','test')

def test_main():
    assert ui.main() == None
