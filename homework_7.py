import datetime

def systeam_date(now = str(datetime.datetime.now())):
    current_time = now[11:-7]
    current_date = now[:10]
    split_date = current_date.split('-')
    return current_time, split_date

current_time, split_date = systeam_date()
current_sec = int(current_time[-2:])

dot = '.'

date_eng = split_date[1] + dot + split_date[2] + dot + split_date[0]
date_eu = split_date[2] + dot + split_date[1] + dot + split_date[0]

print('Date in Europe format:   %s %s\n \n'
      'Date in American format: %s %s' % (date_eu, current_time, date_eng, current_time))
