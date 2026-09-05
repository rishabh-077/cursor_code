-- # Write your MySQL query statement below
SELECT DISTINCT Products.product_id, IFNULL(latest_prices.new_price, 10) as price
FROM Products
LEFT JOIN

-- latest prices
(SELECT product_id, new_price FROM Products
WHERE (product_id, change_date) IN

-- # Latest Price changes
(SELECT product_id, MAX(change_date) AS change_date FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY product_id)) latest_prices

ON Products.product_id = latest_prices.product_id