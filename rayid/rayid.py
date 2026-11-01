import secrets
from typing import Literal

IDType = Literal["digit", "lower", "upper", "all"]

VALUES: dict[str, str] = {
    "digit": "0123456789",
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
}

VALUES["all"] = "".join(VALUES.values())


class RayID:
    def __init__(self, type: IDType) -> None:
        if type not in VALUES:
            raise ValueError(
                f"Invalid ID type: {type!r}. " f"Expected one of: {', '.join(VALUES)}"
            )

        self.type: IDType = type

    def characters(self) -> str:
        return VALUES[self.type]

    def engine(self, length: int) -> str:
        if not isinstance(length, int) or isinstance(length, bool):
            raise TypeError("Length must be an integer.")

        if length <= 0:
            raise ValueError("Length must be greater than zero.")

        characters = self.characters()

        return "".join(secrets.choice(characters) for _ in range(length))

    def gen(self, length: int) -> str:
        if not isinstance(length, int) or isinstance(length, bool):
            raise TypeError("Length must be an integer.")

        if length <= 0:
            raise ValueError("Length must be greater than zero.")

        characters = self.characters()
        first_characters = characters.replace("0", "")

        first = secrets.choice(first_characters)
        remaining = "".join(secrets.choice(characters) for _ in range(length - 1))

        return first + remaining
