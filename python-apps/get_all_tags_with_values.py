import sys
from pylogix import PLC
import time
from datetime import datetime

# Check to ensure we were passed the 2 arguments we need.
script = sys.argv[0]
if len(sys.argv) < 3:
    print(f'SYNTAX: python ${script} <ip> <slot-no>')
    sys.exit(1)

ip = sys.argv[1]
slot = sys.argv[2]

plc = PLC()
plc.IPAddress = ip

# Get the tag list
response = plc.GetTagList()
if response.Status == 'Success':
    tag_list = response.Value
    # variable with current time in milliseconds
    start_time = datetime.now()
    print(f'Tag list retrieved at {start_time.strftime("%Y-%m-%d %H:%M:%S.%f")}')
    for tag in tag_list:
        tag_name = tag.TagName
        try:
            response = plc.Read(tag_name)
            if response.Status == 'Success':
                tag_value = response.Value
                tag_type = tag.DataType
                print(f'Tag: {tag_name}, Type: {tag_type}, Value: {tag_value}')
            else:
                print(f'Error reading tag: {response.Status}')
        except Exception as e:
            print(f'Error reading tag: {tag_name}: {str(e)}')
    end_time = datetime.now()
    print(f'Tag list retrieved at {end_time.strftime("%Y-%m-%d %H:%M:%S.%f")}')
    # print the time elapsed between start_time and end_time variables
    print(f'Time to pull: {end_time - start_time}')

else:
    print(f'Error retrieving tag list: {response.Status}')

plc.Close()
