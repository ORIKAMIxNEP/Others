function paste() {
  navigator.clipboard.readText().then((text) => {
    document.getElementById("url").value = text;
    ScrapeSyllabus(text);
  });
}

async function quitDriver() {
  await eel.CallQuitDriver()();
  window.open("", "_self").close();
}
