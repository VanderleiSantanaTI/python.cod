from datetime import date

data_atual = date.today()
licence_time = date(2022, 9, 23)

if data_atual <= licence_time:
    print('Expirará na data {}'.format(licence_time))
else:
    print('Expirou')