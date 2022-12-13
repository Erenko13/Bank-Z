# Bank-Z
BankZ reposu
to do:
- readme'de responseları gösterilecek
- transfer kısmı için ayrı app'e geçiş yapılacak

## Auth API

### POST auth/token/
#### JSON
- username
- password

### POST auth/token/refresh/
#### JSON
- refresh(token)

### POST auth/register/
#### JSON
- username
- password
- password2
- email
- first_name
- last_name

### GET getInfo/
#### Authorization
- Bearer token

### POST trasfer/
#### Authorization
- Bearer token
#### JSON
- trasfer_id
- balance

## Binance Public API (güncellenecek!!!)

GET binance/public/ping/

GET binance/public/exchangeInfo/{symbol}
