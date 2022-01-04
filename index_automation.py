import schedule
import time
from index import getCelebrationFromName


########### TEST #########

#schedule.every().day.at("07:00").do(lambda: sendMessageAutoAllergies())
schedule.every(2).seconds.do(lambda: getCelebrationFromName("Philippe"))

########### TEST #########

while 1:
    schedule.run_pending()
    time.sleep(1)