from yamcc import YAMCC

print("Welcome to Yet Another Morse Code Converter | v0.0.1\n")

mode = input("Enter mode (decode/encode): ") or "encode"

short_code = "."
long_code = "-"
sep = " "
chinese_start = "\\"
chinese_end = "|"
space = "/"

customize = input("Customize output morse code? (y/N): ").lower() or "n"
if customize == "y":
    short_code = input("Short code (.): ") or short_code
    long_code = input("Long code (-): ") or long_code
    sep = input("Separator ( ): ") or sep
    chinese_start = input("Chinese start (\\): ") or chinese_start
    chinese_end = input("Chinese end (|): ") or chinese_end
    space = input("Space Representation (/): ") or space

converter = YAMCC(
    short_code, long_code, sep, chinese_start, chinese_end, space)

if mode == "encode":
    morse = input("Enter text to encode: ")
    print("Encoded successfully!")
    print(converter.text_to_morse(morse))
else:
    morse = input("Enter morse code to decode:")
    print("Decoded successfully!")
    print(converter.morse_to_text(morse))
