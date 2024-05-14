#!/usr/bin/env python3
"""3-hypermedia_del_pagination.py"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves data for a page specified by index with additional
        hypermedia information.

        Args:
            index (int): The start index of the page (0-indexed).
            Default is None.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            Dict: A dictionary containing hypermedia information.
        """
        assert index is None or (isinstance(index, int) and index >= 0 and index < len(self.indexed_dataset())), \
            "Index must be a non-negative integer within range."

        dataset = self.indexed_dataset()
        if index is None:
            index = 0

        next_index = index + page_size

        # Ensure that next_index does not exceed the dataset size
        if next_index >= len(dataset):
            next_index = None

        data = [dataset[i] for i in range(index, min(index + page_size, len(dataset)))]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
