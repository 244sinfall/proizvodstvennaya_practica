# Производственная практика
Автор: студент 3 курса ЗКИ21-16Б СФУ Филин Дмитрий Алексеевич


Реализован проект для запуска голсоований.
Реализован алгоритм голосования: Нечёткое голосование относительным большинством. (Вариант 8)

# Запуск проекта

## Вручную

1. Зависимости описаны в pyporject.toml
2. ```python ./app.py -p "PATH" -q "QUERY"```

где PATH - путь до SQLite файла,
QUERY - запрос для получения данных.

## Poetry

1. ```poetry install```
2. ```python ./app.py -p "PATH" -q "QUERY"```

где PATH - путь до SQLite файла,
QUERY - запрос для получения данных.

## Docker

1. ```docker build . -t vote_alg_runner```
2.  Скопируйте .db файл в папку data проекта
2. ```sudo  docker run --rm -it -v ./data:/data vote-alg-runner python app.py -q "QUERY" -p "PATH"```

где PATH - /data/(имя файла)
QUERY - запрос для получения данных.