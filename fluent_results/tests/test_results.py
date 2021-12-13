import pytest
"""
Test case for results.py
"""
from results.result import Result

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
    with pytest.raises(TypeError):
        Result.ok(["Somthing"], 99.8)

def test_result_fail_with_valid_data():
    Result.fail("Failure")
    result = Result.fail("Process failed")

    assert len(result.successes) == 0
    assert len(result.errors) == 1
    assert len(result.reasons) == 0
    assert result.errors[0] == "Process failed"
    assert result.value == None
    assert not result.is_success
    assert result.is_failed

def test_result_base_with_error_using_invalid_data_should_thow_an_error():
    with pytest.raises(TypeError):
        result = Result.ok("Valid Data One")
        result.with_error("")

def test_result_base_with_error_using_valid_data_should_succeed():
    result = Result.fail("Error occured with Data One")
    output = result.with_error("The Process failed")
    
    assert len(result.successes) == 0
    assert len(result.errors) == 2
    assert len(result.reasons) == 0
    assert result.is_failed
    assert isinstance(output, Result)