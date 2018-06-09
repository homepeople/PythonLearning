#coding=utf-8
#Exercise5.1
import time
# from types import AsyncGeneratorType
timer=time.time()
def howmany(unit,second,rtype):
    if rtype =='times':
        times=second // unit
        return times
    else:
        remain=second % unit
        return remain
    
def counttime(second,rinfo):
    years=howmany(60*60*24*365, second, 'times')
    remainsecond=howmany(60*60*24*365, second, 'remain')
    days=howmany(60*60*24, remainsecond, 'times')
    remainsecond=howmany(60*60*24, remainsecond, 'remain')
    months=howmany(30, days, 'times')
    hours=howmany(60*60, remainsecond, 'times')
    remainsecond=howmany(60*60, remainsecond, 'remain')
    minutes=howmany(60, remainsecond, 'times')
    remainsecond=howmany(60, remainsecond, 'remain')

#     result=str(int(years))+':'+str(int(months))+':'+str(int(days))+':'+str(int(hours))+':'+str(int(minutes))+':'+str(int(remainsecond))
    result=eval(rinfo)
    return result

t=counttime(timer,'days')
days=howmany(60*60*24, timer, 'times')
hours=howmany(60*60, timer, 'times')
minutes=howmany(60, timer, 'times')
months=howmany(30, days, 'times')
print(days)
print(months)