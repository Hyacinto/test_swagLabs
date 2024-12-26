def test_login(username, setup_teardown):
    _, login_page, _, password = setup_teardown

    expected_result = False
    if username == "locked_out_user":
        expected_result = True

    login_page.login(username, password)
    assert login_page.has_error_message() == expected_result