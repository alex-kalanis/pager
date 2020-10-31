<?php

namespace Pager;


class BasicPager implements IPager
{
    /** @var int */
    protected $maxResults = 0;
    /** @var int */
    protected $actualPage = 0;
    /** @var int */
    protected $limitPerPage = 0;

    public function setMaxResults(int $maxResults): IPager
    {
        $this->maxResults = $maxResults;
        return $this;
    }

    public function getMaxResults(): int
    {
        return $this->maxResults;
    }

    public function setActualPage(int $page): IPager
    {
        $this->actualPage = $page;
        return $this;
    }

    public function getActualPage(): int
    {
        return $this->actualPage;
    }

    public function setLimit(int $limit): IPager
    {
        $this->limitPerPage = $limit;
        return $this;
    }

    public function getLimit(): int
    {
        return $this->limitPerPage;
    }

    public function getOffset(): int
    {
        $page = intval($this->actualPage - 1);
        if ($this->pageExists($page)) {
            return intval($page * $this->limitPerPage);
        } else {
            return 0;
        }
    }

    public function getPagesCount(): int
    {
        $lastPageItems = $this->maxResults % $this->limitPerPage;
        $page = intval(floor($this->maxResults / $this->limitPerPage));
        return ($lastPageItems > 0) ? $page + 1 : $page ;
    }

    public function pageExists(int $i): bool
    {
        return (0 < $i) && ($i <= $this->getPagesCount());
    }
}
