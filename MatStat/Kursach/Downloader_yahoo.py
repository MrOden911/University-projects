import csv
from yahoo_finance import Share
from pprint import pprint


def get_data(tick):
    try:
        return Share(tick)
    except:
        print('Ошибка на сервере!')
        get_data(tick)


def download(tickers):
    error_tick = {}
    for tick in tickers:
        print('\nТикер: ', tick)
        yah = get_data(tick)
        try:
            yah.get_historical('2014-01-01', '2016-01-01')
        except Exception as e:
            print('Тикер {} пропущен.'.format(tick))
            print('Причина: ', e)
            error_tick.update({tick: e})
            continue
        with open('data/Yahoo/' + tick + '.csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            for position in yah:
                write.writerow([position['Adj_Close']])
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
