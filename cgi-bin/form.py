# -*- coding: utf-8 -*-
import cgi
from CreditPaymentsModule import CreditPayments
form = cgi.FieldStorage()
deal_id = int(form.getfirst("deal_id","none"))
pay_date = form.getfirst("pay_date","none")
pObject = CreditPayments()
calc_res = pObject.getRestOfCredit(deal_id, pay_date)
summ = pObject.getSummOfCredit(deal_id)
print("Content-type: text/html\n")
print ("""<!DOCTYPE HTML>
       <html>
       <head>
        <!--<meta charset="utf-8">-->
        <title>Обработка данных форм</title>
        </head>
        <body>""")
print ("<h1>Остаток кредита по договору №{} на дату {} cоставляет: </h1>".format(deal_id, pay_date))
print ("<h2>{} тыс. руб.</h2>".format(calc_res))
print ("<h2>Сумма кредита {} тыс.руб.".format(summ))
print ("""</body>
       </html>""")