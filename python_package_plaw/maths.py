import fire
from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> int:
    return int(a + b)


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> int:
    return int(a - b)


def multiply_numbers(a, b):
    return a * b


def main():
    fire.Fire(
        {
            "add": add_numbers,
            "subtract": subtract_numbers,
        }
    )


if __name__ == "__main__":
    main()
