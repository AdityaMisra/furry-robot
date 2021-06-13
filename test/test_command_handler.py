import pytest

from input_reader import input_parser


class TestCommandHandlerInterface:

    def test_invalid_command(self):
        assert input_parser("INVALID COMMAND") == "Invalid Command"

    def test_success_user_registration(self):
        assert input_parser("REGISTER user1") == "Success"

    def test_failure_user_registration(self):
        assert input_parser("REGISTER user1") == "Error - user already existing"

    def test_invalid_params(self):
        with pytest.raises(Exception):
            input_parser("REGISTER user1 user2")

    def test_listing_creation_1(self):
        assert input_parser(
            "CREATE_LISTING user1 'Phone model 8' 'Black color, brand new' 1000 'Electronics'") == str(100001)

    def test_listing_creation_2(self):
        assert input_parser(
            "CREATE_LISTING user1 'Phone model 8' 'Black color, brand new' 2000 'Electronics'") == str(100002)

    def test_listing_creation_3(self):
        assert input_parser(
            "CREATE_LISTING user1 'Black shoes' 'Training shoes' 100 'Sports'") == str(100003)

    def test_failure_listing_creation(self):
        assert input_parser(
            "CREATE_LISTING user2 'Phone model 8' 'Black color, brand new' 1000 'Electronics'") == "Error - unknown user"

    def test_success_get_top_category(self):
        assert input_parser("GET_TOP_CATEGORY user1") == "Electronics"

    def test_failure_get_top_category(self):
        assert input_parser("GET_TOP_CATEGORY user2") == "Error - unknown user"

    def test_get_category_sort_price_asc_ordering(self):
        assert input_parser(
            "GET_CATEGORY user1 'Electronics' sort_price asc").startswith("Phone model 8|Black color, brand new|1000|")

    def test_get_category_sort_price_dsc_ordering(self):
        assert input_parser(
            "GET_CATEGORY user1 'Electronics' sort_price dsc").startswith("Phone model 8|Black color, brand new|2000|")

    def test_get_category_sort_time_dsc_ordering(self):
        assert input_parser(
            "GET_CATEGORY user1 'Electronics' sort_time dsc").startswith("Phone model 8|Black color, brand new|2000|")

    def test_failure_get_category(self):
        assert input_parser("GET_CATEGORY user1 'Fashion' sort_time asc") == "Error - category not found"

    def test_failure_user_not_present_get_category(self):
        assert input_parser("GET_CATEGORY user14 'Fashion' sort_time asc") == "Error - unknown user"

    def test_get_listing(self):
        assert str(input_parser("GET_LISTING user1 100001")).startswith("Phone model 8|Black color, brand new|1000|")

    def test_failure_unknown_user_get_listing(self):
        assert input_parser("GET_LISTING user10 100001") == "Error - unknown user"

    def test_failure_not_found_get_listing(self):
        assert input_parser("GET_LISTING user1 10000112") == "Error - not found"

    def test_delete_listing(self):
        assert input_parser("DELETE_LISTING user1 100002") == "Success"

    def test_failure_owner_mismatch_delete_listing(self):
        assert input_parser("DELETE_LISTING user10 100001") == "Error - listing owner mismatch"

    def test_failure_listing_does_not_exist_delete_listing(self):
        assert input_parser("DELETE_LISTING user1 10000122") == "Error - listing does not exist"

    def test_delete_listing_same_count_category(self):
        assert input_parser("DELETE_LISTING user1 100001") == "Success"

    def test_top_category(self):
        assert input_parser("GET_TOP_CATEGORY user1") == "Sports"

    def test_delete_listing_clearing_out_the_category(self):
        assert input_parser("DELETE_LISTING user1 100003") == "Success"
