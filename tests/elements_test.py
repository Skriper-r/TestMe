# import time

from pages.element_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'http://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_addr, output_permanent_addr = text_box_page.check_filled_form()

            assert full_name == output_name, 'the full name does not match'
            assert email == output_email, 'the email does not match'
            assert current_address == output_current_addr, 'the full name does not match'
            assert permanent_address == output_permanent_addr, 'the full name does not match'
