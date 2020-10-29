#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
from typing import List, Tuple, Dict


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
        """Get a page from the dataset
        """
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict:
        """Return a page with some metadata
        """
        page_data = self.get_page(page, page_size)
        dataset_size = len(self.dataset())
        r_pages = dataset_size // page_size
        n_pages = r_pages if dataset_size % page_size == 0 else r_pages + 1
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < n_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": n_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    start = (page - 1) * page_size
    return (start, start + page_size)
