from NewSignUp import signup

user2 = signup()
user2.already_registered_signup("berkgs96@hotmail.com", "ibo", "berk", "12345678", "12345678", "")
user2.password_is_empty_signup("berkgs96@hotmail.com", "ibo", "berk", " ", " ", " ")
user2.password_not_long_enough_signup("berkgs96@hotmail.com", "ibo", "berk", "1234567", "1234567", "")
user2.passwords_doesnt_match_signup("berkgs96@hotmail.com", "ibo", "berk", "12345678", "123456789", "")
user2.invalid_mail_signup("berkgs", "ibo", "berk", "12345678", "12345678", "")
user2.unselected_checkbox("berkgs96@hotmail.com", "ibo", "berk", "12345678", "12345678", "")
user2.teardown()