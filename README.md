# ДЗ 3 Асинхронность в Python

FastAPI приложение, считает квадраты чисел асинхронно с задержками

## Запуск

```
pip install -r requirements.txt
uvicorn main:app --reload
```

Потом открыть http://127.0.0.1:8000/docs

## Пример запроса

POST /calculate/

```
{
  "numbers": [5, 3, 10],
  "delays": [1, 2, 0.5]
}
```

Ответ:

```
{
  "results": [
    {"number": 5, "square": 25, "delay": 1, "time": 1.0},
    {"number": 3, "square": 9, "delay": 2, "time": 2.0},
    {"number": 10, "square": 100, "delay": 0.5, "time": 0.5}
  ],
  "total_time": 2.0,
  "parallel_faster_than_sequential": true
}
```
