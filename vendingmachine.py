# 自販機のお釣りシステム

coin = 799
coin500 = 500
coin500_number = coin//coin500
coin -= coin500

coin100 = 100
coin100_number = coin//coin100
coin -= coin100*coin100_number

coin10 = 10
coin10_number = coin//coin10
coin -= coin10*coin10_number

coin1 = 1
coin1_number = coin//coin1
coin -= coin1*coin1_number

print('799円に必要なお金は500円',coin500_number,'枚、100円',coin100_number,'枚、10円',coin10_number,'枚、1円',coin1_number,'枚。',sep='')