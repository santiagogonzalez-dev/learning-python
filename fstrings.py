import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str


def main():
    number = 800
    print(f"The number is {number:06}")
    print(f"{100.23459786:.2f}")


if __name__ == "__main__":
    main()
