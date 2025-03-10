import time
from contextlib import contextmanager

from typing import Any, Generator


@contextmanager
def timed(title: str) -> None | Generator[None, Any, None]:
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        print(f"{title} took {(end_time - start_time):.6f} seconds")


