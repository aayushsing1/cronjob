import schedule
import time
import requests

def visit_webpage():
    response = requests.get('http://currencyapi-x8iy.onrender.com/convert_currency?amount=1&from_currency=USD&to_currency=INR')
    # You can handle the response if needed
    print('Visited webpage:', response.status_code)

# Schedule the job to run every 20 minutes
schedule.every(20).minutes.do(visit_webpage)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
