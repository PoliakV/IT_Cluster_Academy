from decimal import *

pryb = input("Введіть суму нарахованої заробної плати: ")

pdokh = Decimal(pryb) * Decimal(0.18)

viisk_zbir = Decimal(pryb) * Decimal(0.015)

print('Податок на доходи фізичних осіб складає: ', Decimal(pdokh).quantize(Decimal('.01')))

print('Військовий збір складає: ', Decimal(viisk_zbir).quantize(Decimal('.01')))

print('Сумарно необхідно сплатити до бюджету податків на суму: ', Decimal(pdokh + viisk_zbir).quantize(Decimal('.01')))
