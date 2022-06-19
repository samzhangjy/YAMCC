import codecs


class YAMCC(object):
    def __init__(
        self,
        short_code: str = ".",
        long_code: str = "-",
        sep: str = " ",
        space: str = "/",
        unicode_start: str = "\\",
        unicode_end: str = "|"
    ):
        """Yet another morse code converter, but supports unicode.

        Args:
            short_code (str, optional): The short code representation. Defaults to ".".
            long_code (str, optional): The long code representation. Defaults to "-".
            sep (str, optional): The separator representation. Defaults to " ".
            space (str, optional): The space representation. Defaults to "/".
            unicode_start (str, optional): The unicode start sign. Defaults to "\".
            unicode_end (str, optional): The unicode end sign. Defaults to "|".
        """
        super().__init__()
        self.MORSE_TO_CHAR = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            ".-.-.-": ".",
            "--..--": ",",
            "..--..": "?",
            ".----.": "'",
            "-.-.--": "!",
            "-..-.": "/",
            "-.--.": "(",
            "-.--.-": ")",
            ".-...": "&",
            "---...": ":",
            "----..": ";",
            "-.-.-.": "=",
            "-...-": "-"
        }
        self.CHAR_TO_MORSE = {v: k for k, v in self.MORSE_TO_CHAR.items()}

        self.short_code = short_code
        self.long_code = long_code
        self.sep = sep
        self.unicode_start = unicode_start
        self.unicode_end = unicode_end
        self.space = space

    def __get_morse_code(self, char: str) -> str:
        if char == " ":
            return self.space
        return self.CHAR_TO_MORSE.get(char, "[ERROR]").replace(".", self.short_code).replace("-", self.long_code)

    def text_to_morse(self, text: str, separated_by: str = " ") -> str:
        """Converts a text to morse code.

        Args:
            text (str): The unicode string to convert.
            separated_by (str, optional): How words are separated. Defaults to " ".

        Returns:
            str: The converted morse code.
        """
        separated_by = separated_by.encode("utf-8")
        converted_morse_code = ""
        for char in text:
            cur = char.upper()
            if cur.isascii():
                converted_morse_code += self.__get_morse_code(cur) + self.sep
                continue
            converted_morse_code += self.unicode_start + self.sep
            cur = char.encode("unicode_escape").decode("utf-8")
            for unicode_char in cur[1:]:
                converted_morse_code += self.__get_morse_code(
                    unicode_char.upper()) + self.sep
            converted_morse_code += self.unicode_end + self.sep
        return converted_morse_code.strip(self.sep)

    def morse_to_text(self, morse: str) -> str:
        """Convert generated morse code to unicode string.

        Args:
            morse (str): The morse code to convert.

        Returns:
            str: The converted unicode string.
        """
        converted_text = ""
        current_unicode = ""
        is_unicode_mode = False
        normalized_morse = morse.replace(
            self.short_code, ".").replace(self.long_code, "-")
        for morse_code in normalized_morse.split(self.sep):
            morse_code = morse_code.strip()
            if morse_code == self.unicode_start:
                is_unicode_mode = True
                current_unicode = "\\"
                continue
            if morse_code == self.unicode_end:
                is_unicode_mode = False
                converted_text += codecs.decode(
                    current_unicode.lower(), "unicode_escape")
                continue
            if is_unicode_mode:
                current_unicode += self.MORSE_TO_CHAR.get(
                    morse_code, "[ERROR]")
                continue
            if morse_code in self.MORSE_TO_CHAR:
                converted_text += self.MORSE_TO_CHAR[morse_code]
                continue
            if morse_code == self.space:
                converted_text += " "
                continue
        return converted_text


if __name__ == "__main__":
    converter = YAMCC(
        short_code="咕",
        long_code="噜",
        sep="，",
        space="哝",
        unicode_start="汪",
        unicode_end="喵"
    )
    morse = converter.text_to_morse("Hello World 你好，世界")
    converted = converter.morse_to_text(morse)
    print("Morse Code:", morse)
    print("Translated:", converted)
