from datetime import datetime,timedelta

now = datetime.now()

print(now)  # 2018-08-11 22:30:04.448334
print(now.strftime('%y%m%d %H%M%S')) #180811 223251
print(now.strftime('%Y%m%d %H%M%S')) #20180811 223400

tomorrow = now + timedelta(days=1) # 2018-08-12 08:36:57.240462
print(tomorrow)

after_5_hours = now + timedelta(hours=5)
print(after_5_hours)

dt = datetime(2018,8,11,22,0,10)
print(dt)

dt = datetime.strptime('2018/8/11 22:10:10', '%Y/%m/%d %H:%M:%S')
print(dt)

timestamp = 1429417200
begin_time = datetime.fromtimestamp(timestamp)
print(begin_time)

