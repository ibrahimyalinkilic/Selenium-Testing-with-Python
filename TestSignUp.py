from NewSignUp import signup

user2 = signup()
user2.already_registered_signup("a3@bitexen.com", "ibo", "berk", "12345678", "12345678", "")
user2.password_is_empty_signup("a3@bitexen.com", "ibo", "berk", " ", " ", " ")
user2.password_not_long_enough_signup("a3@bitexen.com", "ibo", "berk", "1234567", "1234567", "")
user2.passwords_doesnt_match_signup("a3@bitexen.com", "ibo", "berk", "12345678", "123456789", "")
user2.invalid_mail_signup("a3", "ibo", "berk", "12345678", "12345678", "")
user2.unselected_checkbox("a3@bitexen.com", "ibo", "berk", "12345678", "12345678", "")
user2.teardown()