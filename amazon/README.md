### System Design Questions

#### Q1 Customer-Database API Design
假设给一个数据库 怎么写一个给customer设计的接口来从数据库中检索客户信息?

(假设数据库已经提供了相应的方法来进行基本的CRUD操作)

> 定义主要Entity: Customer
>
> CustomerDAO类封装数据库的交互
>
> CustomerService 提供检索客户信息的接口

#### Q2 Search Engine Design