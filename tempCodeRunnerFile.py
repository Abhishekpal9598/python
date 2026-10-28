import pywhatkit as kit
import time

# List of numbers (include country code, e.g., +91 for India)
numbers = ["+917880625494", "+917983874285", "+919648158367","9598253687"]

# Message you want to send
message = "hey buddy what are you ding now "

# Loop through all numbers and send message
for number in numbers:
    kit.sendwhatmsg_instantly(number, message, 15, True, 3)
    time.sleep(5)  # wait before sending to the next person