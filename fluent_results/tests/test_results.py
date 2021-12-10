"""
Test case for results.py
"""
from results.result import Result

def test_result_ok_with_valid_data():
    result = Result.Ok("Tested successfully")

    assert len(result.Successes) == 1
    assert result.data == None
