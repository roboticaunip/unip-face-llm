import re
def clean_text_for_tts(text):
    if not text:
        return ""
    text = re.sub(r"[#*_~^=<>{}\[\]|]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
