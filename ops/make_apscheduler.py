# https://mp.weixin.qq.com/s/pSSI2LxF0hSfLNA1nlOeeA


from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()

# main.py
from datetime import datetime

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler

# 任务持久化 使用 SQLite
jobstores = {
    'default': SQLAlchemyJobStore(url = 'sqlite:///jobs.db')
}
# 执行器配置
executors = {
    'default': ThreadPoolExecutor(20),
}
# 关于 Job 的相关配置，见官方文档 API
job_defaults = {
    'coalesce': False,
    'next_run_time': datetime.now()
}
scheduler = BlockingScheduler(
    jobstores = jobstores,
    executors = executors,
    job_defaults = job_defaults,
    timezone = 'Asia/Shanghai'
)

from datetime import datetime

# v1 
# def now(trigger):
#     print(f"trigger:{trigger} -> {datetime.now()}")
    

# if __name__ == '__main__':
#     scheduler.add_job(now, trigger = "interval", args = ("interval",), seconds = 5)
#     scheduler.start()

@scheduler.scheduled_job(trigger = "interval", args = ("interval",), seconds = 5)
def now(trigger):
    print(f"trigger:{trigger} -> {datetime.now()}")

if __name__ == '__main__':
    scheduler.start()