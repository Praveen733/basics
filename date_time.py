from datetime import *
import pytz 
INDIA = pytz.timezone('Asia/Kolkata')  
datetime_INDIA = datetime.now(INDIA) 
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S")) 
