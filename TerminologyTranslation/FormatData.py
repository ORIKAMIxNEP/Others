import requests
import re
from python.InitialCapitalization import InitialCapitalization

subject = int(input("整形するデータの科目 0:機械 1:電気 2:情報 3:建設 4:化学 5:その他："))
subjectData = ["Machine", "Electricity", "Information",
               "Construction", "Chemistry", "Others"]
terminologyData = ""
with open("data/" + subjectData[subject] + "Data.txt", "r", encoding="utf-8") as TerminologyData:
    i = 0
    roman = ""
    for terminologyDataLine in TerminologyData:
        if i % 6 == 1:
            roman = requests.get(
                "https://www.seonet.jp/useful/hebon/api.php?bmp=yes&word=" + terminologyDataLine).text.replace("<br>", "")
            if roman == "Limit":
                print("API Limit")
                exit()
        elif i % 6 == 2:
            if terminologyDataLine != roman + "\n":
                terminologyData += roman + "\n" + \
                    InitialCapitalization(terminologyDataLine)
                i += 2
                continue
        elif i % 6 == 3:
            terminologyData += InitialCapitalization(terminologyDataLine)
            i += 1
            continue
        elif i % 6 == 4:
            meaning = InitialCapitalization(terminologyDataLine)
            if meaning[-2:-1] != ".":
                terminologyData += meaning.rstrip() + ".\n"
            else:
                terminologyData += meaning
            i += 1
            continue
        elif i % 6 == 5:
            if terminologyDataLine != ",\n" and terminologyDataLine != "\\\n":
                if terminologyDataLine == "\n":
                    terminologyData += ","
                else:
                    terminologyData += ",\n"
                    i += 1
        terminologyData += terminologyDataLine
        i += 1
    if subject == 5:
        if terminologyData[-2:-1] != "\\":
            terminologyData += "\\\n"
    elif terminologyData[-2:-1] != ",":
        terminologyData += ",\n"
    terminologyData = re.sub("(?<!\")\"(?!\")", "\"\"", terminologyData)
with open("data/" + subjectData[subject] + "Data.txt", "w", encoding="utf-8") as TerminologyData:
    TerminologyData.write(terminologyData)
