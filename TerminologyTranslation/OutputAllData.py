from SelectKey import SelectKey

with open("data/AllData.txt", "w", encoding="utf-8") as AllData:
    AllData.write("ClearCollect(Terminology,")
    with open("data/MachineData.txt", "r", encoding="utf-8") as MachineData:
        i = 0
        for machineDataLine in MachineData:
            machineDataLine = machineDataLine.rstrip()
            AllData.write(SelectKey(i, "machine") +
                          machineDataLine.replace(".", ""))
            i += 1
    with open("data/ElectricityData.txt", "r", encoding="utf-8") as ElectricityData:
        i = 0
        for electricityDataLine in ElectricityData:
            electricityDataLine = electricityDataLine.rstrip()
            AllData.write(SelectKey(i, "electricity") +
                          electricityDataLine.replace(".", ""))
            i += 1
    with open("data/InformationData.txt", "r", encoding="utf-8") as InformationData:
        i = 0
        for informationDataLine in InformationData:
            informationDataLine = informationDataLine.rstrip()
            AllData.write(SelectKey(i, "information") +
                          informationDataLine.replace(".", ""))
            i += 1
    with open("data/ConstructionData.txt", "r", encoding="utf-8") as ConstructionData:
        i = 0
        for constructionDataLine in ConstructionData:
            constructionDataLine = constructionDataLine.rstrip()
            AllData.write(SelectKey(i, "construction") +
                          constructionDataLine.replace(".", ""))
            i += 1
    with open("data/ChemistryData.txt", "r", encoding="utf-8") as ChemistryData:
        i = 0
        for chemistryDataLine in ChemistryData:
            chemistryDataLine = chemistryDataLine.rstrip()
            AllData.write(SelectKey(i, "chemistry") +
                          chemistryDataLine.replace(".", ""))
            i += 1
    with open("data/OthersData.txt", "r", encoding="utf-8") as OthersData:
        i = 0
        for othersDataLine in OthersData:
            othersDataLine = othersDataLine.rstrip()
            AllData.write(SelectKey(i, "others") +
                          othersDataLine.replace("\\", ""))
            i += 1
    AllData.write(");")
