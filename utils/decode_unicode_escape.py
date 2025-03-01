import re

def decode_unicode_escape(s):
    # Исправленное декодирование для MicroPython
    def repl(m):
        try:
            return chr(int(m.group(1), 16))
        except:
            return m.group(0)
    return re.sub(r'\\u([a-fA-F0-9]{4})', repl, s)