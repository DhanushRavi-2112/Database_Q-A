few_shots=[
    {
        "Question" : "How many t-shirts do we  have left for nike in extra small size and white color?",
        "SQLQuery" : "SELECT stock_quantity FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS';",
        "SQLResult" : "Result of the SQL Query",
        "Answer"   : "69"},
    {
        "Question" : "How much price in the inventory for all small size t-shirts?",
        "SQLQuery" : "SELECT SUM(PRICE*STOCK_QUANTITY) FROM t_shirts WHERE SIZE='S'",
        "SQLResult" : "Result of the SQL Query",
        "Answer" : "24137"},
    {
        "Question" : "if we have sell all Levi's t-shirts today with discounts applied.How much revenue our store will generate (post discounts)?",
        "SQLQuery" : """SELECT sum(a.total_amount*((100-coalesce(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand='Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id=discounts.t_shirt_id;""",
"SQLResult" : "Result of the SQL Query",
        "Answer" : "884"},
    {
        "Question" : "How many white color levi's t-shirts are available?",
        "SQLQuery" : "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand='Levi' AND color='White';",
        "SQLResult" : "Result of the SQL Query",
        "Answer" : "10"},
    {
        "Question" : "if we have sell all Levi's t-shirts.How much revenue our store will generate (post discounts)?",
        "SQLQuery" : "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        "SQLResult" : "Result of the SQL Query",
        "Answer" : "33893"}
]