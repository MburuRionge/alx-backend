#!/usr/bin/env python3
"""the function  two integer arguments page and page_size."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size

    return(start, end)
