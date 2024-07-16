# Производственная практика
Автор: студент 3 курса ЗКИ21-16Б СФУ Филин Дмитрий Алексеевич


Реализован проект для запуска голсоований.
Реализован алгоритм голосования: Нечёткое голосование относительным большинством. (Вариант 8)

# Запуск проекта

## Вручную

1. Установить зависимости. Зависимости описаны в pyporject.toml
2. ```python ./app.py -p "PATH" -q "QUERY"```

где PATH - путь до SQLite файла,
QUERY - запрос для получения данных.

## Poetry (Quick Start)

1. ```poetry install```
2. ```poetry shell```
3. ```python ./src/app.py -p "PATH" -q "QUERY"```

где PATH - путь до SQLite файла,
QUERY - запрос для получения данных. (SELECT * FROM experiment_data)

Example:
```python ./src/app.py -p "/home/dmitryfilin/Downloads/experiment_edu.db" -q "SELECT * FROM experiment_data"```

## Docker

1. ```docker build . -t vote_alg_runner```
2.  Скопируйте .db файл в папку data проекта
2. ```docker run --rm -it -v ./data:/data vote_alg_runner python app.py -q "QUERY" -p "PATH"```

где PATH - /data/(имя файла)
QUERY - запрос для получения данных.

Example:
```docker run --rm -it -v ./data:/data vote_alg_runner python app.py -q "SELECT * FROM experiment_data" -p "/data/experiment_edu.db"```
