<?php

namespace Pager\Interfaces;


/**
 * Interface IActualPage
 * @package Pager\Interfaces
 * Info from inputs on which page we are
 */
interface IActualInput
{
    /**
     * Returns current page number
     * @return int
     */
    public function getActualPage(): int;
}
