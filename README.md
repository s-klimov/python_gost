# Пример репозитория с "гостовским" питоном

### Вариант использования Dockerfile
1. Создание образа
```bash
docker build --file Dockerfile-local --tag komtek/python:3.7.10-openssl-gost .
```
2. Выбрать в PyCharm Pro интерпретатор Docker, имя образа komtek/python:3.7.10-openssl-gost
3. Ответить на вопрос брандмаура Windows

### Вариант использования docker-compose
1. Создание образа
```bash
docker-compose build
```
2. Выбрать в PyCharm Pro интерпретатор docker-compose, имя контейнера - имя основного приложения
3. Ответить на вопрос брандмаура Windows

## Прочие материалы
[Установка redis на Windows](https://skillbox.ru/media/base/kak_ustanovit_redis_v_os_windows_bez_ispolzovaniya_docker/)
