import csv
from yahoo_finance import Share


def get_data(tick):
    try:
        return Share(tick)
    except:
        print('Ошибка на сервере!')
        get_data(tick)

tickers = []
TickFile = open('data/tickers.txt', 'r')
for line in TickFile:
    tickers.append(line.replace('\n', ''))
TickFile.close()


for tick in tickers:
    print('\nТикер: ', tick)
    yah = get_data(tick)
    try:
        yah.get_historical('2014-01-01', '2016-01-01')
    except Exception as e:
        print('Тикер {} пропущен.'.format(tick))
        print('Причина: ', e)
        continue
    with open('data/' + tick + '.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        for position in yah:
            write.writerow([position['Adj_Close']])
    csvfile.close()
    print('Тикер {} загружен.'.format(tick))

print('Завершено')