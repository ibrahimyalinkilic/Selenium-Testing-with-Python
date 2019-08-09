from NewSignIn import login

user = login()
user.password_is_empty_login("a3@bitexen.com", "")
user.wrong_mail_login("a3@hotmail.com", "12345678")
user.wrong_password_login("a3@bitexen.com", "12345678")
user.invalid_login("a3", "1234567")
user.success_login("a3@bitexen.com","123123123")
user.teardown()

