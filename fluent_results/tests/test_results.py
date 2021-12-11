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


