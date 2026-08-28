package algorithms.problems.easy.best_time_to_buy_and_sell_stock

fun maxProfit(prices: IntArray): Int {
    var minBuy = Int.MAX_VALUE
    var maxSell = Int.MIN_VALUE
    var maxProfit = 0

    for (price in prices) {
        when {
            price < minBuy -> {
                minBuy = price
                maxSell = price
            }

            price > maxSell -> {
                maxSell = price
                maxProfit = maxOf(maxProfit, maxSell - minBuy)
            }
        }
    }

    return maxProfit
}
