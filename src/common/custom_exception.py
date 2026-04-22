import sys


class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception):
        self.error_detail = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_detail)

    @staticmethod
    def get_detailed_error_message(message: str, error_detail: Exception) -> str:
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        detailed_message = f"Error occurred in file: {file_name} at line: {line_number} with message: {message}"
        return detailed_message

    def __str__(self):
        return self.error_detail
