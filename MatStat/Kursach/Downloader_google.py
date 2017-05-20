import csv
from datetime import datetime
from pprint import pprint

import pandas_datareader as pan


def download(tickers):
    error_tick = {}
    for tick in tickers:
        print('\nТикер: ', tick)
        try:
            data = pan.get_data_google(symbols=tick, start=datetime(2014, 1, 1), end=datetime(2014, 1, 4))
        except Exception as e:
            print('Тикер {} пропущен.'.format(tick))
            print('Причина: ', e)
            error_tick.update({tick: e})
            continue
        with open('data/Google/' + tick + '.csv', 'w', newline='') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(['Close'])
            for position in data['Close']:
                write.writerow([position])
        csvfile.close()
        print('Тикер {} загружен.'.format(tick))
    return error_tick


tickers = []
TickFile = open('data/tickers.txt', 'r')
for line in TickFile:
    tickers.append(line.replace('\n', ''))
TickFile.close()

while True:
    error_tick = download(tickers)
    if len(error_tick) == 0:
        break
    print('\nОшибочные тикеры:')
    pprint(error_tick)
    quest = input('Повторить скачивание ошибочных тикеров? (+/-) ')
    if quest != '+':
        break
    tickers = list(set(tickers) & set(error_tick))

print('\nЗавершено')