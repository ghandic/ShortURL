import string
from itertools import product
from typing import Optional


class ShortURL(object):
    def __init__(self, chars: str = string.ascii_lowercase, max_length: int = 4) -> None:
        self.chars = chars
        self.max_length = max_length
        self.cur = 1
        self.db = {}  # Short -> Long
        self.r_db = {}  # Long -> Short

        self.max_supported = sum(len(self.chars) ** i for i in range(1, self.max_length + 1))
        self.set_short_urls()

    def __repr__(self) -> str:
        return str(self.db)

    def set_short_urls(self):
        if self.cur > self.max_length:
            raise Exception("Ran out of short urls")
        self.short = product(string.ascii_lowercase, repeat=self.cur)

    def add(self, long_url: str) -> str:
        if self.r_db.get(long_url) is not None:
            return self.r_db[long_url]

        try:
            short_url = "".join(next(self.short))
            self.db[short_url] = long_url
            self.r_db[long_url] = short_url
            return short_url
        except StopIteration:
            self.cur += 1
            self.set_short_urls()
            return self.add(long_url)

    def get(self, short_url: str) -> Optional[str]:
        return self.db.get(short_url)

