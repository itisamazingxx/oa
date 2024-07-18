## Bank System

设计一个银行系统, 该系统需要支持创建新账户; 存钱; 取钱; 付款等操作

### Functionality

1. createAccount(timestamp, accountId);
2. deposit(timestamp, accountId, amount);
3. pay(timestamp, accountId, amount);
4. topActivity(timestamp, n);
5. transfer(timestamp, sourceAccountId, targetAccountId, amount);
6. acceptTransfer(timestamp, accountId, transferId);
