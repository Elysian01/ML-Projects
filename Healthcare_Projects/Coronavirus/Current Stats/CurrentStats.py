# This Program gives Current stats of conoravirus cases and death by fetching it from government website

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="ElysianIcon.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)  # gives the html data
    return r.text  # returns in text format


if __name__ == '__main__':
    # notifyMe("Elysian", "Lets stop the spread of virus together")
    myHtmlData = getData("https://www.mohfw.gov.in/")

#     print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, "html.parser")
#     print(soup.prettify())

    # gets only the table from whole html page
    myDataStr = ""
    for tr in soup.find_all("tbody")[1].find_all("tr"):
        myDataStr += tr.get_text()

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")

    states = ["Punjab", "Maharashtra"]
    for item in itemList[0:23]:
        dataList = item.split("\n")
        if dataList[1] in states:
            nTitle = "Cases of Covid-19"
            nText = f"State : {dataList[1]}\nIndian Cases : {dataList[2]} , Foreign Cases : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]}"
            notifyMe(nTitle, nText)
            time.sleep(2)
