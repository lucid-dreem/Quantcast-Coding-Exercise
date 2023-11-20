from most_active_cookie import date_prev, on_date
# tests run using pytest

# date_prev tests

print (date_prev("2018-11-01"))

def test_date_prev_reg():
    assert date_prev("2018-12-09") == "2018-12-08"
    assert date_prev("2018-12-01") == "2018-11-30"
    assert date_prev("2018-11-01") == "2018-10-31"
    assert date_prev("2018-03-01") == "2018-02-28"
    assert date_prev("2016-03-01") == "2016-02-29"
    assert date_prev("2018-01-01") == "2017-12-31"

def test_on_date():
    assert on_date("2018-12-09T14:19:00+00:00", "2018-12-09") == True
    assert on_date("2018-12-08T14:19:00+00:00", "2018-12-09") == False
    assert on_date("2018-12-09T14:19:00+10:00", "2018-12-10") == True
    assert on_date("2018-12-09T14:19:30+09:41", "2018-12-10") == True