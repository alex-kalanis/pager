"""
Main classes and interfaces for using this kind of pager
"""


class IPager:
    """
     * Interface IPager
    """

    def set_max_results(self, max_results: int):
        """
         * Set maximum available results for paging
        """
        raise NotImplementedError('TBI')

    def get_max_results(self) -> int:
        """
         * Returns maximum available results for paging
        """
        raise NotImplementedError('TBI')

    def set_actual_page(self, page: int):
        """
         * Set current page number
        """
        raise NotImplementedError('TBI')

    def get_actual_page(self) -> int:
        """
         * Returns current page number
        """
        raise NotImplementedError('TBI')

    def set_limit(self, limit: int):
        """
         * Set limit of items on one page
        """
        raise NotImplementedError('TBI')

    def get_limit(self) -> int:
        """
         * Returns limit of items on one page
        """
        raise NotImplementedError('TBI')

    def get_offset(self) -> int:
        """
         * Returns calculated offset
        """
        raise NotImplementedError('TBI')

    def get_pages_count(self) -> int:
        """
         * Returns number of available pages
        """
        raise NotImplementedError('TBI')

    def page_exists(self, page: int) -> bool:
        """
         * Have we that page?
        """
        raise NotImplementedError('TBI')


class IRenderEngine:
    """
     * Interface IRenderEngine
     * How to display
    """

    def set_display_inputs_count(self, number: int):
        """
         * If rendering area has this option - how many page inputs will show themselves
        """
        raise NotImplementedError('TBI')

    def set_pager(self, pager: IPager = None):
        """
         * Set used pager
        """
        raise NotImplementedError('TBI')

    def get_pager(self):
        """
         * Get pager known to object
        """
        raise NotImplementedError('TBI')

    def render(self) -> str:
        """
         * Render content to output (cli or html)
        """
        raise NotImplementedError('TBI')


class BasicPager(IPager):

    def __init__(self):
        self._max_results = 0
        self._actual_page = 0
        self._limit_per_page = 0

    def set_max_results(self, max_results: int):
        self._max_results = max_results
        return self

    def get_max_results(self) -> int:
        return self._max_results

    def set_actual_page(self, page: int):
        self._actual_page = page
        return self

    def get_actual_page(self) -> int:
        return self._actual_page

    def set_limit(self, limit: int):
        self._limit_per_page = limit
        return self

    def get_limit(self) -> int:
        return self._limit_per_page

    def get_offset(self) -> int:
        page = int(self._actual_page - 1)
        if self.page_exists(page):
            return int(page * self._limit_per_page)
        else:
            return 0

    def get_pages_count(self) -> int:
        last_page_items = self._max_results % self._limit_per_page
        page = int(self._max_results / self._limit_per_page)
        return page + 1 if last_page_items > 0 else page

    def page_exists(self, page: int) -> bool:
        return (0 < page) and (page <= self.get_pages_count())
