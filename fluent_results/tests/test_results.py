"""
Author kaypee90
"""
import pytest

from results.result import Result
from results.custom_exceptions import (
    MessageNotStringError,
    MessageNotEmptyError,
    BulkMessagesTypeError,
)


def test_result_ok_with_valid_data():
    Result.ok("Successful One")
    result = Result.ok({"data": "sample data"}, "Tested successfully")

    assert len(result.successes) == 1
    assert len(result.errors) == 0
    assert len(result.reasons) == 0
    assert result.successes[0] == "Tested successfully"
    assert result.value == {"data": "sample data"}
    assert result.is_success
    assert not result.is_failed


def test_result_ok_with_invalid_data():
    with pytest.raises(MessageNotStringError):
        Result.ok(["Somthing"], 99.8)


def test_result_fail_with_valid_data():
    Result.fail("Failure")
    result = Result.fail("Process failed")

    assert len(result.successes) == 0
    assert len(result.errors) == 1
    assert len(result.reasons) == 0
    assert result.errors[0] == "Process failed"
    assert not result.value
    assert not result.is_success
    assert result.is_failed


def test_result_base_with_error_using_empty_data_should_throw_an_error():
    with pytest.raises(MessageNotEmptyError):
        result = Result.fail("Valid Data One")
        result.with_error("")


def test_result_base_with_error_using_valid_data_should_succeed():
    result = Result.fail("Error occured with Data 1")
    result.with_error("The Process failed")
    output = result.with_error("The Process failed again")

    assert len(result.successes) == 0
    assert len(result.errors) == 3
    assert len(result.reasons) == 0
    assert result.is_failed
    assert isinstance(output, Result)


def test_result_base_with_error_using_empty_message_should_throw_an_error():
    with pytest.raises(MessageNotEmptyError):
        result = Result.fail("Valid Data One")
        result.with_error("")


def test_result_base_with_success_using_invalid_data_should_throw_an_error():
    with pytest.raises(MessageNotEmptyError):
        result = Result.ok("Valid Data Two")
        result.with_success("")


def test_result_base_with_success_using_valid_data_should_succeed():
    result = Result.ok({"data": "sample test data"}, "Process occured with Data Two")
    result.with_success("The Process succeeded")
    result.with_success("The Process succeeded again")
    output = result.with_success("The Process succeeded again and again")
    assert len(result.successes) == 4
    assert len(result.errors) == 0
    assert len(result.reasons) == 0
    assert result.is_success
    assert isinstance(output, Result)


def test_result_base_with_reason_using_invalid_data_should_throw_an_error():
    with pytest.raises(MessageNotEmptyError):
        result = Result.ok("Valid Data Three")
        result.with_reason("")


def test_result_base_with_reason_using_valid_data_should_succeed():
    result = Result.ok({"data": "sample test data 1"}, "Process occured with Data 3")
    result.with_reason("With reason one")
    result.with_reason("With reason two")
    output = result.with_reason("With reason three")

    assert len(result.successes) == 1
    assert len(result.errors) == 0
    assert len(result.reasons) == 3
    assert result.is_success
    assert isinstance(output, Result)


def test_string_representation_of_result_with_no_reasons_should_retun_empty_string():
    result = Result.ok(
        {"data": "sample test data one"}, "Process occured with Data THREE"
    )

    assert len(result.reasons) == 0
    assert str(result) == ""


def test_string_representation_of_result_with_reasons_should_retun_valid_string_format():
    result = Result.ok(
        {"data": "sample test data one"}, "Process occured with Data THREE"
    )
    result.with_reason("With reason one")
    result.with_reason("With reason two")

    assert len(result.reasons) == 2
    assert (
        str(result)
        == "Result: IsSuccess='True', Reasons='With reason one; With reason two'"
    )


def test_convert_to_dict_should_return_a_valid_dictionary():
    result = Result.ok(
        {"data": "sample test data six"}, "Process occured with Data five"
    )
    result.with_reason("With reason eight")

    output = result.convert_to_dict()

    assert output == {
        "is_success": True,
        "value": {"data": "sample test data six"},
        "successes": ["Process occured with Data five"],
        "errors": [],
        "reasons": ["With reason eight"],
    }


def test_with_reasons_with_valid_reasons_should_update_result_reasons_list():
    reasons = ["Second reason", "Third reason"]
    result = Result.fail("Error occured with Data One")
    result.with_reason("First reason")

    result.with_reasons(reasons)

    assert result.errors == ["Error occured with Data One"]
    assert not result.successes
    assert result.reasons == ["First reason", "Second reason", "Third reason"]


def test_with_reasons_with_invalid_reasons_list_should_throw_an_exception():
    reasons = [8, 9]
    result = Result.fail("Error occured. Try Again")
    result.with_reason("Initial reason")

    with pytest.raises(BulkMessagesTypeError):
        result.with_reasons(reasons)


def test_with_successes_with_valid_messages_should_update_result_success_list():
    messages = ["Success reason two", "Success reason three"]
    result = Result.ok(
        {"data": "sample test data Five"}, "Process finished with Data Seven"
    )
    result.with_success("Success reason one")

    result.with_successes(messages)

    assert not result.errors
    assert not result.reasons
    assert result.successes == [
        "Process finished with Data Seven",
        "Success reason one",
        "Success reason two",
        "Success reason three",
    ]

def test_with_sucesses_with_invalid_messages_list_should_throw_an_exception():
    reasons = [2, True]
    result = Result.ok({"data": "sample"}, "Executed successfully")
    result.with_success("Initial reason")

    with pytest.raises(BulkMessagesTypeError):
        result.with_successes(reasons)


def test_with_errors_with_valid_messages_should_update_result_error_list():
    messages = ["Error reason two", "Error reason three"]
    result = Result.fail("Process couldn't finish!")
    result.with_error("Error reason one")

    result.with_errors(messages)

    assert not result.successes
    assert not result.reasons
    assert result.errors == [
        "Process couldn't finish!",
        "Error reason one",
        "Error reason two",
        "Error reason three",
    ]


def test_with_errors_with_invalid_messages_list_should_throw_an_exception():
    reasons = [False, True]
    result = Result.fail("Error occured. Contact Admin")
    result.with_error("First Error Message")

    with pytest.raises(BulkMessagesTypeError):
        result.with_errors(reasons)


def test_with_errors_with_empty_messages_list_should_not_update_errors_list():
    reasons = []
    result = Result.fail("Process failed. Kindly Contact Admin")
    result.with_error("Emtpy List Error Message")
    
    result.with_errors(reasons)

    assert result.errors == [
        "Process failed. Kindly Contact Admin",
        "Emtpy List Error Message",
    ]
