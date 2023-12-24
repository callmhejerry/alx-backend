#!/usr/bin/env python3

"""
Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ a method named get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        (start_index, end_index) = index_range(page=page, page_size=page_size)
        if (start_index > len(self.dataset()) or
                end_index > len(self.dataset())):
            return []
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs"""
        (start_index, end_index) = index_range(page=page, page_size=page_size)
        data = self.get_page(page=page, page_size=page_size)
        next_page = None
        prev_page = None

        if page > 1:
            prev_page = page - 1

        if end_index < len(self.dataset()):
            next_page = page + 1

        total_pages = None
        if len(self.dataset()) % page_size > 0:
            total_pages = len(self.dataset()) // page_size + 1
        else:
            total_pages = len(self.dataset()) // page_size

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int):
    """
    a function named index_range that takes two
    integer arguments page and page_size.
    The function should return a tuple of size two
    containing a start index and an
    end index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
