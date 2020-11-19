print('Üdvözöljük ez egy valuta váltó program!')
jo = 0
lista = {
    'HUF-EUR': 0.00277269
    , 'HUF-GBP': 0.00247522
    , 'HUF-USD': 0.00328165
    , 'HUF-CHF': 0.00299376
    , 'HUF-PLN': 0.0123946
    , 'HUF-JPY': 0.340882
    , 'HUF-CZK': 0.0730353
    , 'HUF-RON': 0.0135146
    , 'HUF-SEK': 0.0283141
    ,
        'EUR-HUF': 360.66
    , 'EUR-GBP': 0.8928
    , 'EUR-USD': 1.1833
    , 'EUR-CHF': 1.07955
    , 'EUR-PLN': 4.4778
    , 'EUR-JPY': 123.115
    , 'EUR-CZK': 26.342
    , 'EUR-RON': 4.87355
    , 'EUR-SEK': 10.2129
    ,
        'GBP-HUF': 404.005
    , 'GBP-EUR': 1.12007
    , 'GBP-USD': 1.3252
    , 'GBP-CHF': 1.2087
    , 'GBP-PLN': 5.01293
    , 'GBP-JPY': 137.843
    , 'GBP-CZK': 29.5223
    , 'GBP-RON': 5.45959
    , 'GBP-SEK': 10.2129
    ,
        'USD-HUF': 304.725
    , 'USD-EUR': 0.84505
    , 'USD-GBP': 0.754603
    , 'USD-CHF': 0.9125
    , 'USD-PLN': 3.7846
    , 'USD-JPY': 104.095
    , 'USD-CZK': 22.2912
    , 'USD-RON': 4.11818
    , 'USD-SEK': 8.62651
    ,
        'CHF-HUF': 333.988
    , 'CHF-EUR': 0.926312
    , 'CHF-GBP': 0.827335
    , 'CHF-USD': 1.09589
    , 'CHF-PLN': 4.14595
    , 'CHF-JPY': 113.989
    , 'CHF-CZK': 24.4297
    , 'CHF-RON': 4.51419
    , 'CHF-SEK': 9.46163
    ,
        'PLN-HUF': 80.68
    , 'PLN-EUR': 0.223324
    , 'PLN-GBP': 0.199484
    , 'PLN-USD': 0.264197
    , 'PLN-CHF': 0.241199
    , 'PLN-JPY': 27.4912
    , 'PLN-CZK': 5.89472
    , 'PLN-RON': 1.09046
    , 'PLN-SEK': 2.28625
    ,
        'JPY-HUF': 2.93337
    , 'JPY-EUR': 0.00812249
    , 'JPY-GBP': 0.00725465
    , 'JPY-USD': 0.00960661
    , 'JPY-CHF': 0.00877281
    , 'JPY-PLN': 0.0363656
    , 'JPY-CZK': 0.214289
    , 'JPY-RON': 0.0395937
    , 'JPY-SEK': 0.0830201
    ,
        'CZK-HUF': 13.6901
    , 'CZK-EUR': 0.0379018
    , 'CZK-GBP': 0.0338671
    , 'CZK-USD': 0.044812
    , 'CZK-CHF': 0.0409212
    , 'CZK-PLN': 0.169686
    , 'CZK-JPY': 4.66268
    , 'CZK-RON': 0.184581
    , 'CZK-SEK': 0.387218
    ,
        'RON-HUF': 74.1113
    , 'RON-EUR': 0.205172
    , 'RON-GBP': 0.183342
    , 'RON-USD': 0.242692
    , 'RON-CHF': 0.221574
    , 'RON-PLN': 0.918717
    , 'RON-JPY': 25.2506
    , 'RON-CZK': 5.41682
    , 'RON-SEK': 2.09683
    ,
        'SEK-HUF': 35.3345
    , 'SEK-EUR': 0.09799159
    , 'SEK-GBP': 0.08874418
    , 'SEK-USD': 0.115764
    , 'SEK-CHF': 0.105657
    , 'SEK-PLN': 0.438019
    , 'SEK-JPY': 12.0493
    , 'SEK-CZK': 2.58217
    , 'SEK-RON': 0.476767
}
valutak = ['HUF', 'EUR', 'GBP', 'USD', 'CHF', 'PLN', 'JPY', 'CZK', 'RON', 'SEK']
van = 0
while van < 1:
    valuta1 = input('Kérem Adja meg mit szeretne váltani!' + str(valutak)).upper()
    if valuta1 in valutak:
        van = 1
        valutak.remove(valuta1)
    else:
        print('El írta a valutát. kérem probálja újra!\n')
        van = 0

valuta2 = ''
while jo < 1:
    valuta2 = input('Kérem Adja meg mire szeretne váltani!' + str(valutak)).upper()
    if valuta2 in valutak:
        jo = 1
        valutak.remove(valuta2)
    else:
        jo = 0
        print('El írta a valutát. kérem probálja újra!\n')

valuta = valuta1 + '-' + valuta2
mennyiseg = int(input('Adja meg mennyit szeretne át váltani: '))
osszeg = lista.get(valuta) * mennyiseg
print('Az osszeg:', osszeg, ' ', valuta2)
