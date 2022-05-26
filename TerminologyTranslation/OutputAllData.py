from python.SelectKey import SelectKey

with open("data/AllData.txt", "w", encoding="utf-8") as AllData:
    AllData.write("ClearCollect(Terminology,")
    wordCount = 0
    for subject in ["Machine", "Electricity", "Information", "Construction", "Chemistry", "Others"]:
        with open("data/" + subject + "Data.txt", "r", encoding="utf-8") as TerminologyData:
            i = 0
            for terminologyDataLine in TerminologyData:
                terminologyDataLine = terminologyDataLine.rstrip()
                AllData.write(SelectKey(i, subject.lower()) +
                              terminologyDataLine.replace("\\", ""))
                i += 1
            wordCount += i/6
    AllData.write(");")
    print("単語数:" + str((int)(wordCount)))
