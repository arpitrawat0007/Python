# import time
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time
timestamp = time.strftime('%H:%M:%S')
Hour = int(time.strftime("%H"))
Minute = int(time.strftime('%M'))
Second = int(time.strftime('%S'))
print(timestamp)