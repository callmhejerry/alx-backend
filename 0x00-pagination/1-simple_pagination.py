#!/usr/bin/env python3


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
        return self.dataset()[start_index: end_index]


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
