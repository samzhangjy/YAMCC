import codecs
import string
import random


class YAMCC(object):

    TAKEOVER_SHORT_CODE = string.ascii_lowercase
    TAKEOVER_LONG_CODE = string.ascii_uppercase
    TAKEOVER_SEP = string.digits
    TAKEOVER_SPACE = "+"
    TAKEOVER_UNICODE_START = "_"
    TAKEOVER_UNICODE_END = "$"

    def __init__(
        self,
        short_code: str = ".",
        long_code: str = "-",
        sep: str = " ",
        space: str = "/",
        unicode_start: str = "\\",
        unicode_end: str = "|",
        takeover = False
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
        self.takeover = takeover

    def __get_morse_code(self, char: str) -> str:
        if self.takeover:
            if char == " ":
                return self.TAKEOVER_SPACE
            plain = self.CHAR_TO_MORSE.get(char, "[ERROR]")
            result = ""
            for ch in plain:
                if ch == ".":
                    result += random.choice(self.TAKEOVER_SHORT_CODE)
                elif ch == "-":
                    result += random.choice(self.TAKEOVER_LONG_CODE)
                else:
                    result += ch
            return result
        if char == " ":
            return self.space
        return self.CHAR_TO_MORSE.get(char, "[ERROR]").replace(".", self.short_code).replace("-", self.long_code)
    
    def __split_morse_code(self, morse: str) -> list[str]:
        if not self.takeover:
            return morse.split(self.sep)
        result = []
        cur_section = ""
        for ch in morse:
            if ch in self.TAKEOVER_SEP:
                result.append(cur_section)
                cur_section = ""
            else:
                cur_section += ch
        return result
    
    def __get_seperator(self) -> str:
        if self.takeover:
            return random.choice(self.TAKEOVER_SEP)
        return self.sep

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
                converted_morse_code += self.__get_morse_code(cur) + self.__get_seperator()
                continue
            converted_morse_code += (self.TAKEOVER_UNICODE_START if self.takeover else self.unicode_start) + self.__get_seperator()
            cur = char.encode("unicode_escape").decode("utf-8")
            for unicode_char in cur[1:]:
                converted_morse_code += self.__get_morse_code(
                    unicode_char.upper()) + self.__get_seperator()
            converted_morse_code += (self.TAKEOVER_UNICODE_END if self.takeover else self.unicode_end) + self.__get_seperator()
        return converted_morse_code

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
        if self.takeover:
            normalized_morse = ""
            for ch in morse:
                if ch in self.TAKEOVER_SHORT_CODE:
                    normalized_morse += "."
                elif ch in self.TAKEOVER_LONG_CODE:
                    normalized_morse += "-"
                else:
                    normalized_morse += ch

        for morse_code in self.__split_morse_code(normalized_morse):
            morse_code = morse_code.strip()
            if morse_code == (self.TAKEOVER_UNICODE_START if self.takeover else self.unicode_start):
                is_unicode_mode = True
                current_unicode = "\\"
                continue
            if morse_code == (self.TAKEOVER_UNICODE_END if self.takeover else self.unicode_end):
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
            if morse_code == (self.TAKEOVER_SPACE if self.takeover else self.space):
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
        unicode_end="喵",
        takeover=True
    )
    morse = converter.text_to_morse("Hello World 你好，世界")
    converted = converter.morse_to_text(morse)
    print("Morse Code:", morse)
    print("Translated:", converted)
