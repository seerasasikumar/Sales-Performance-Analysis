create database project;
use project;
select * from orders;

select count(*) as Total_Records from orders;
select count(distinct Customer_Name) as Total_Customers from orders;
select count(distinct Product_Name) as Total_Products from orders;
select sum(Sales) as Total_Sales from orders;
select sum(Profit) as Total_Sales from orders;
select avg(Sales) as Avg_Order_Val from orders;

select Category, sum(Sales) as Total_Sales from orders 
group by Category order by Total_Sales desc;

select Category, sum(Profit) as Total_Profit from orders
group by Category order by Total_Profit desc;

select Region, Sum(Sales) as Revenue from orders
group by Region order by Revenue desc;

select Product_Name, sum(Sales) as Revenue from orders
group by Product_Name order by Revenue desc limit 10;

select Customer_Name, sum(Sales) as Revenue from orders
group by Customer_Name order by Revenue desc limit 5;

select Product_Name, sum(Quantity) as Total_Units from orders
group by Product_Name order by Total_Units desc limit 5;

select Product_Name, sum(Profit) as Total_Profit from orders
group by Product_Name having Total_Profit < 0 
order by Total_Profit;

select Customer_Name, count(Order_ID) as Total_Orders from orders
group by Customer_Name having Total_Orders > 1
order by Total_Orders;

select Region,Customer_Name, sum(Sales) as Revenue from orders
group by Region,Customer_Name order by Revenue desc limit 5;

select Category, round(sum(Profit)/sum(Sales)*100,2) as Profit_Margin from orders
group by Category;
