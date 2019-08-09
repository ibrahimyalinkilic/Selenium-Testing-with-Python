from Trade import Trade

user = Trade()
user.success_login("a3@bitexen.com","123123123")
user.buy_select_first()
user.buy_select_second()
user.buy_select_all()
user.sell_select_first()
user.sell_select_second()
user.sell_select_all()
user.teardown()