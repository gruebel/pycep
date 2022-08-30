class BicepValidator:
    @staticmethod
    def is_valid(bicep_text: str) -> bool:
        return BicepValidator.multi_line_string_valid(bicep_text)

    @staticmethod
    def multi_line_string_valid(bicep_text: str) -> bool:
        return bicep_text.count("'''") % 2 == 0
