#import json

from settings import PATH_WITH_FIXTURES
from src.utils import get_all_operations, get_executed_operations, get_newer_five_operations, validate_operation


def main():
    operations_ = get_all_operations(PATH_WITH_FIXTURES)
    ex_operations = get_executed_operations(operations_)
    five_operations = get_newer_five_operations(ex_operations)
#    print(json.dumps(five_operations, indent=2, ensure_ascii=False))
    for operation in five_operations:
        if operation:
            print(validate_operation(operation))


if __name__ == '__main__':
    main()