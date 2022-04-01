from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

print("URLを入力してください")
driver.get(input())

subject = driver.find_element_by_xpath(
    "//*[@id='wrap']/div[4]/div/div/div[1]/div/div[1]/h1").text
wariaiLabel = driver.find_element_by_xpath(
    "//*[@id='MainContent_SubjectSyllabus_wariaiTable']/tbody/tr[1]").find_elements_by_tag_name("th")
wariaiValue = driver.find_element_by_xpath(
    "//*[@id='MainContent_SubjectSyllabus_wariaiTable']/tbody/tr[2]").find_elements_by_tag_name("td")

regularExam = "0"
littleExam = "0"
report = "0"
attitude = "0"
others = "0"
annual = "false"

count = 0
for element in wariaiLabel:
    if "試験" in element.text:
        regularExam = wariaiValue[count].text
    if "小テスト" == element.text:
        littleExam = wariaiValue[count].text
    if "レポート" in element.text or "ポートフォリオ" == element.text:
        report = wariaiValue[count].text
    if "発表" in element.text:
        attitude = wariaiValue[count].text
    if "その他" == element.text:
        others = wariaiValue[count].text
    count += 1
if driver.find_element_by_xpath("//*[@id='MainContent_SubjectSyllabus_UpdatePanelSyllabus']/div/table/tbody/tr[6]/td[1]").text == "通年":
    annual = "true"

print(",\n    {\n        subject: \"" + subject + "\",\n        regularExam: " + regularExam + ",\n        littleExam: " + littleExam +
      ",\n        report: " + report + ",\n        attitude: " + attitude + ",\n        others: " + others + ",\n        annual: " + annual + "\n    }")

driver.quit()
