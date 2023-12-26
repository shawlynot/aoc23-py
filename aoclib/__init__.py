import requests
import os

class AocClient:

    def __init__(self, puzzle: int) -> None:
        self.session_cookie = os.getenv("SESSION")
        self.puzzle = puzzle

    def get_input(self) -> str:
        response = requests.get(f"https://adventofcode.com/2023/day/{self.puzzle}/input", cookies={"session": self.session_cookie})
        return response.text

    def get_bonus_input(self) -> str:
        pass