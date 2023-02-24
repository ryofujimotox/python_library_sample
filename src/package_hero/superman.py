import json
import os


# サンプルデータ
def greeting():
    json_open = open(getLibraryDir() + "/common/text.json", "r")
    texts = json.load(json_open)

    for text in texts:
        print("hero: " + text)

    return


# ライブラリのパス取得
def getLibraryDir():
    return os.path.dirname(os.path.abspath(__file__))
