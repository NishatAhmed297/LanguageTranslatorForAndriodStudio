import xml.etree.ElementTree as ET
import google_trans_fixed
import argparse
import os

def filter_text(text):
    excluding_symbols = ["\\n", "\\'", "\\\"", "\\t"]
    for sym in excluding_symbols:
        if sym in text:
            splits = text.split(sym)
            text = ""
            for s in splits:
                text += s
    return text


parser = argparse.ArgumentParser()
parser.add_argument(
    "src_file", help="File path of original strings.xml", type=str)
parser.add_argument("target_language_code", nargs="+",
                    help="Language Code of target language,if there are more than one, please add space between their names")
args = parser.parse_args()

src_file = args.src_file
target_language_code = args.target_language_code

for lang in target_language_code:
    translator = google_trans_fixed.google_translator()
    tree = ET.parse(src_file)
    root = tree.getroot()

    print("Translating "+lang+"...")
    for rt in root:
        if "translatable" in rt.attrib and rt.attrib.get("translatable") == "false":
            continue

        if rt.tag == "string-array":
            for elem in rt.iter():
                if elem.tag == "item":
                    elem.text = filter_text(elem.text)
                    txt = translator.translate(str(elem.text), lang_tgt=lang)
                    if (type(txt) is list):
                        elem.text = txt[0]
                    else:
                        elem.text = txt
        else:
            rt.text = filter_text(rt.text)
            txt = translator.translate(str(rt.text), lang_tgt=lang)
            if (type(txt) is list):
                rt.text = txt[0]
            else:
                rt.text = txt

    translated = ET.ElementTree(root)

    output_path = "Output/values-"+lang
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output = output_path + "/" + src_file

    translated.write(output, encoding="UTF-8", xml_declaration=True)
    print(lang+" is done, Moving to next")

print("Translation is completed")
