import datetime
import json

#from settings import PATH_WITH_FIXTURES


def get_all_operations(path: str) -> list[dict]:
    with open(path, 'r', encoding='UTF=8') as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    executed_operations = list()
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_newer_five_operations(executed_operations: list[dict]) -> list[dict]:
    sorted_operations = sorted(executed_operations, key=lambda operation: operation['date'], reverse=True)
    return list(sorted_operations)[:5]


def convert_date(date: str) -> str:
    date_convert = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.datetime.strftime(date_convert, '%d.%m.%Y')


def convert_payment_info(info: str) -> str:
    if info.startswith('Счет'):
        result = info.split(' ')[-1]
        return 2 * "*" + result[16:20]
    else:
        result_ = info.split(' ')[-1]
    return result_[:4] + " " + result_[4:6] + 2 * "*" + " " + 4 * "*" + " " + result_[12:16]


def validate_operation(operation: dict) -> str:
    date = convert_date(operation['date'])
    from_ = convert_payment_info(operation['from']) if operation.get('from') else ''
    to_ = convert_payment_info(operation['to'])
    return f'{date} {operation["description"]} ' \
           f'{from_} -> {to_} ' \
           f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}'


#operations_ = get_all_operations(PATH_WITH_FIXTURES)
#ex_operations = get_executed_operations(operations_)
#five_operations = get_newer_five_operations(ex_operations)
#print(json.dumps(five_operations, indent=2, ensure_ascii=False))
#for operation in five_operations:
#    if operation:
#        print(validate_operation(operation))
