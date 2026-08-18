-- Write your MySQL query statement below
WITH first_orders AS (
    SELECT customer_id, min(order_date) AS order_date
    FROm Delivery
    GROUP BY customer_id
)
SELECT ROUND(AVG(Delivery.order_date = customer_pref_delivery_date)*100, 2) AS immediate_percentage
FROM Delivery 
JOIN first_orders ON Delivery.customer_id = first_orders.customer_id
AND Delivery.order_date = first_orders.order_date

--  Write your MySQL query statement below
WITH first_orders AS (
    SELECT customer_id, min(order_date) AS order_date
    FROm Delivery
    GROUP BY customer_id
)
SELECT ROUND(AVG(order_date = customer_pref_delivery_date)*100, 2) AS immediate_percentage
FROM Delivery 
WHERE (customer_id, order_date) in (SELECT * FROM first_orders)