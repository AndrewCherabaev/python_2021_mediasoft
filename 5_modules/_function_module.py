from typing import List


def fib(n: int):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b
    print()


def get_string_array() -> List[str]:
    return ['te', 'ew']


def multiply_string(string: str, amount: int = 3) -> str:
    return string * amount


def cut_string(string: str) -> str:
    return string[1:-1]


def invert_string(string: str) -> str:
    return string[::-1]


if __name__ == '__main__':
    print('My name is {}'.format(__name__))
