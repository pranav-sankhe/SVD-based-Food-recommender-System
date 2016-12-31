import client 

import schedule
import time

def job():
	client.train()

def update():
	schedule.every(12).hour.do(job)
	# schedule.every().day.at("10:30").do(job)
	# schedule.every().monday.do(job)
	# schedule.every().wednesday.at("13:15").do(job)

	while True:
	    schedule.run_pending()
	    time.sleep(1) 
