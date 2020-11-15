from typing import Union


categories = [
    (
        "tak",
        [
            "tak",
            "jak najbardziej",
            "no trudno powiedzieć ale myślę, że w zasadzie to tak",
            "czemu nie",
            "nie widzę przeszkód",
        ],
    ),
    ("nie", ["raczej nie", "w żadnym wypadku", "oczywiście, że nie"]),
    ("nie wiem", ["nie wiem", "skąd mam wiedzieć"]),
]


def sentence_classify(text: str) -> Union[str, None]:
    """Return classified sentence based on category"""
    for category, matches in categories:
        if any(match in text for match in matches):
            return category
    return None
