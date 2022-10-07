import eel

from ScrapeSyllabus import QuitDriver, ScrapeSyllabus


@eel.expose
def CallScrapeSyllabus(url):
    return ScrapeSyllabus(url)


@eel.expose
def CallQuitDriver():
    QuitDriver()


eel.init("web")
eel.start("index.html", size=(960, 640))
