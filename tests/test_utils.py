import pytest

from settings import PATH_WITH_FIXTURES
from src.utils import get_all_operations, get_executed_operations, get_newer_five_operations, convert_date, \
    convert_payment_info


@pytest.fixture
def valid_date():
    return [
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
                "amount": "81150.87",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]


@pytest.fixture
def last_operation():
    return [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869"
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381"
        }
    ]


@pytest.fixture
def card_convert():
    result = 'Счет 77613226829885488381'
    return 2 * "*" + result[15:-1]


def test_get_all_operations(valid_date):
    assert isinstance(get_all_operations(PATH_WITH_FIXTURES), list)


def test_get_executed_operations(valid_date):
    assert len(get_executed_operations(valid_date)) == 8


def test_get_newer_five_operations(last_operation):
    assert get_newer_five_operations(last_operation)[-1] == {"id": 801684332,
                                                             "state": "EXECUTED",
                                                             "date": "2019-11-05T12:04:13.781725",
                                                             "operationAmount": {
                                                                 "amount": "21344.35",
                                                                 "currency": {
                                                                     "name": "руб.",
                                                                     "code": "RUB"
                                                                 }
                                                             },
                                                             "description": "Открытие вклада",
                                                             "to": "Счет 77613226829885488381"}


def test_convert_date():
    assert convert_date("2019-12-08T22:46:21.935582") == '08.12.2019'


def test_convert_payment_info():
    assert convert_payment_info("Счет 38611439522855669794") == '**9794'
    assert convert_payment_info("Maestro 7810846596785568") == '7810 84** **** 5568'
