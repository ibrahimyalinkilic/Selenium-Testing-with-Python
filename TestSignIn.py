from NewSignIn import login

user = login()
user.password_is_empty_login("berkgs96@hotmail.com", "")
user.wrong_mail_login("berkgs966@hotmail.com", "12345678")
user.wrong_password_login("berkgs96@hotmail.com", "1234567")
user.invalid_login("berkgs96", "1234567")
user.success_login("a3@bitexen.com","123123123")
user.teardown()

