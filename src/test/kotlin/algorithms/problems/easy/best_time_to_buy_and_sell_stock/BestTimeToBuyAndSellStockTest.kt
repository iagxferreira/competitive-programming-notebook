package algorithms.problems.easy.best_time_to_buy_and_sell_stock

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class BestTimeToBuyAndSellStockTest {
    @Test
    fun `returns the best profit for the classic example`() {
        assertEquals(5, maxProfit(intArrayOf(7, 1, 5, 3, 6, 4)))
    }

    @Test
    fun `returns zero when prices only go down`() {
        assertEquals(0, maxProfit(intArrayOf(7, 6, 4, 3, 1)))
    }

    @Test
    fun `returns the best profit even when it appears in the middle`() {
        assertEquals(2, maxProfit(intArrayOf(2, 4, 1)))
    }

    @Test
    fun `returns zero for a flat sequence`() {
        assertEquals(0, maxProfit(intArrayOf(5, 5, 5, 5)))
    }
}
