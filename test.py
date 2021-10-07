# from unittest.mock import Mock
# import datetime

# tuesday = datetime.datetime(year=2019,month=1,day=1)
# saturday = datetime.datetime(year=2019,month=1,day=5)

# datetime = Mock()

# def is_weekday():

#     today = datetime.datetime.today()
#     print(today.weekday())
#     return (0 <= today.weekday() < 5)


# print(datetime.datetime.today())

# datetime.datetime.today.return_value = tuesday

# assert is_weekday()

import pytest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    print("kkkk")
    if r.status_code == 200:
        print("WORJING")
        return r.json()
    return None

def test_get_hoildays_timeout():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'test':'working','second':'second_working'}
    requests.get.side_effect = [Timeout,mock_response]

    # print('didnt')
    with pytest.raises(Timeout):
        get_holidays()

    assert get_holidays()['test'] == 'working'
    # assert get_holidays()['second'] == 'second_working'
    assert requests.get.call_count == 2
        
