from bs4 import BeautifulSoup
from datetime import date
import urllib.request

def lambda_handler(event, context):
    TOKEN = 'your bot token'
    CHAT_ID = 'your chatid'
    today = date.today().isoformat()
    pgnum = -1
    todayMessage = f"https://api.telegram.org/bot6067319279:AAGCkixuNEDpc3UnAr02b77dovKZZFYbgIA/sendMessage?chat_id=5889946400&text={today+'----------------------------'}"
    urllib.request.urlopen(todayMessage)
    while True:
        pgnum += 1
        html = urllib.request.urlopen(f"https://www.skku.edu/skku/campus/skk_comm/notice01.do?mode=list&&articleLimit=10&article.offset={pgnum*10}").read()
        noticeList = BeautifulSoup(html, "html.parser").select("#jwxe_main_content > div > div > div.container > div.board-name-list.board-wrap > ul > li")
        for notice in noticeList:
            noticeDate = notice.select_one('dl > dd > ul > li:nth-of-type(3)').text
            if not noticeDate == today:
                break
            category = notice.select_one('dl > dt > span').text.strip()
            title = notice.select_one('dl > dt > a').text.strip()
            url = ('https://www.skku.edu/skku/campus/skk_comm/notice01.do' +
                    notice.select_one('dl > dt > a')['href']).strip()
            content = urllib.parse.quote(category+title+'\n'+url)
            sendurl = f"https://api.telegram.org/bot6067319279:AAGCkixuNEDpc3UnAr02b77dovKZZFYbgIA/sendMessage?chat_id=5889946400&text={content}"
            urllib.request.urlopen(sendurl)
        else:
            continue
        break
                
