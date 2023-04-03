# **API социальной сети "Yatube"**

## **Описание проекта**

В данном проекте реализован API для интеграции новых приложений
с социальной сетью "Yatube"

## **Технологии**

| Библиотека                  | Версия |
|-----------------------------|--------|
|Django                      | 3.2.16 |
|djangorestframework          | 3.12.4 |
|djangorestframework-simplejwt| 4.7.2  |
|Pillow                       | 9.3.0  |
|PyJWT                        | 2.1.0  |
|requests                     | 2.26.0 |

## Запуск

1. Установите python версии 3.9 и выше.
1. Клонируйте репозиторий и перейдите в него в командной строке:

    ```bash
    git clone https://github.com/LizaKoch/api_final_yatube.git && \
    cd api_final_yatube
    ```

1. Создайте вертуальное окружение и установите зависимости (пример команд на linux/mac):

    ```bash
    python3 -m venv venv && \ 
        source venv/bin/activate && \
        python3 -m pip install --upgrade pip && \
        pip install -r requirements.txt
    ```

1. Выполните миграции:

    ```bash
    python3 yatube_api/manage.py migrate
    ```

1. Создайте superuser:

    ```bash
    python3 manage.py createsuperuser
    ```

1. Запустите проект:

    ```bash
    python3 manage.py runserver
    ```

## **Примеры запросов API**

Полная документация доступна по ссылке <http://127.0.0.1:8000/doc/> после запуска проекта.
