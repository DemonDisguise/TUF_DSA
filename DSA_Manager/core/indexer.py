import json
import os
import time


from core.models import Problem


CACHE_FILE = os.path.join(
    "cache",
    ".problem_index.json"
)


class Indexer:

    @staticmethod
    def save(problems: list[Problem]):

        os.makedirs("cache", exist_ok=True)

        data = {
            "version": "1.0",
            "last_scan": time.time(),
            "count": len(problems),
            "problems": [
                p.to_dict()
                for p in problems
            ]
        }

        with open(
            CACHE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load() -> list[Problem] | None:

        if not os.path.exists(CACHE_FILE):

            return None

        try:

            with open(
                CACHE_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            return [
                Problem.from_dict(item)
                for item in data.get("problems", [])
            ]

        except Exception:

            return None