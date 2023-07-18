# Простое API для тестирования Redis
Возвращает температуру в городе, обращаясь к WeatherAPI.com

### Три ручки:
- http://127.0.0.1:5001/api/?city=London - сразу вызывает WeatherAPI
- http://127.0.0.1:5001/api/cache/?city=London - с использованием кэш Redis
- http://127.0.0.1:5001/api/postgres/?city=Moscow - с использованием Postgres в качестве кэша
