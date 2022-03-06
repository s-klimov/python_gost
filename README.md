# Пример репозитория с "гостовским" питоном

Создание образа
```bash
docker build --file Dockerfile-local --tag komtek/python:3.7.10-openssl-gost .
```

Убедиться в наличии на хосте
* переменной среды DATABASE_URL
* переменной среды REDIS_URL
* переменной среды BROKER_URL
* переменной среды RABBITMQ_URL

## Прочие материалы
[Установка redis на Windows](https://skillbox.ru/media/base/kak_ustanovit_redis_v_os_windows_bez_ispolzovaniya_docker/)