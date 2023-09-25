import sender_stand_request
import data

def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

def prepare_body_post_new_client_kit(name_kits):
    current_kits = data.kit_body.copy()
    current_kits["name"] = name_kits
    return current_kits

def positive_assert(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert resp_kit.status_code == 201
    assert resp_kit.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert resp_kit.status_code == 400

def negative_assert_no_name(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    assert resp_kit.status_code == 400

# Тест 1:
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit("a")
    positive_assert(kit_body)
# Тест 2:
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit("a" * 511)
    positive_assert(kit_body)
# Тест 3:
def test_create_kit_empty_name_get_error_response():
    kit_body = prepare_body_post_new_client_kit("")
    negative_assert(kit_body)
# Тест 4:
def test_create_kit_512_letter_in_name_get_error_response():
     kit_body = prepare_body_post_new_client_kit("а" * 512)
     negative_assert(kit_body)
# Тест 5:
def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit("QWErty")
    positive_assert(kit_body)
# Тест 6:
def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit("Мария")
    positive_assert(kit_body)
# Тест 7:
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit('"№%@",')
    positive_assert(kit_body)
# Тест 8:
def test_create_kit_has_space_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit(" Человек и КО ")
    positive_assert(kit_body)
# Тест 9:
def test_create_kit_has_number_in_name_get_success_response():
    kit_body = prepare_body_post_new_client_kit("123")
    positive_assert(kit_body)
# Тест 10:
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)
# Тест 11:
def test_create_kit_number_type_in_name_get_error_response():
    kit_body = prepare_body_post_new_client_kit(123)
    negative_assert(kit_body)