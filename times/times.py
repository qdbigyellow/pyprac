import time


#https://www.runoob.com/python/python-date-time.html
#https://mp.weixin.qq.com/s/EtkmVrL9QYiZ7_YYKAQoaQ

# struct_time type
t = time.localtime()
print(t, type(t))

# string type
t = time.ctime()
print(t, type(t))

t = time.ctime(1606395685.1878598)
print(t, type(t))


# string format time
t = time.localtime()  # type:time.struct_time
t_str = time.strftime("%Y-%m-%d", t)  # type:str
print(t_str, type(t_str))


# convert sting to struct_time
t_str = "2020-11-02"
t_time = time.strptime(t_str, "%Y-%m-%d")  # type:time.struct_time
print(t_time, type(t_time))


# DO NOT mix up datetime and time
import datetime

t = datetime.today()  # type:datetime
print(t, type(t))
print(t.year)  # 年份
print(t.month)  # 月份

# return  local time
datetime.now()
print(t,type(t))
datetime.today()
print(t,type(t))


# return utc time
t = datetime.utcnow()  # type:datetime
print("UTC时间:", t)

# timestamp convert to datetime
timestamp = time.time()
print(f"timestamp:{timestamp},type:{type(timestamp)}")
# 时间戳转datetime
t = datetime.fromtimestamp(timestamp)
print(f"t:{t},type:{type(t)}")


# From datetime to string format time

from datetime import datetime
t = datetime.now()
str_datetime = t.strftime("%Y-%m-%d %H:%M:%S")
print(f"字符串日期:{str_datetime},type:{type(str_datetime)}")

# From string format time to datetime
str_datetime = "2020-11-29 22:05:20"
t = datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
print(f"t:{t},type:{type(t)}")



# plus date
from datetime import datetime
import datetime as idatetime

t = datetime.now()
print(f"当前时间:{t}")
three_day = t + idatetime.timedelta(days=3)
print(f"三天后时间:{three_day}")

# Enhancement:   python-dateutil
from datetime import datetime
from dateutil.relativedelta import relativedelta

t = datetime.now()
print(f"当前时间:{t}")
three_time = t + relativedelta(months=3)
print(f"三个月后时间:{three_time}")
one_year = t+relativedelta(years=1)
print(f"一年后时间:{one_year}")
up_year = t+relativedelta(years=-1)
print(f"去年这个时间:{up_year}")
