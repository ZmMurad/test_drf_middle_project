# Сервис доставки грузов
Сервис разработа на Django Rest Framework с Celery/Redis

## Установка и запуск


1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Создать файл .env заполнить в нем поля 
```
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DJANGO_SETTINGS_MODULE=freight.settings
DATABASE_URL=
```
4. Запустить контейнеры
```
sudo docker-compose up -d
```
5. Остановка работы контейнеров
```
sudo docker-compose stop
```
***
```http://0.0.0.0:8000/showcars/``` - увидеть все доступные машины post для добавления новой

```http://0.0.0.0:8000/showcars/{id}/``` -  отправить put запрос для обновления данных машины

```http://0.0.0.0:8000/showcargoes/``` - увидеть все грузы, post для добавления новой

```http://0.0.0.0:8000/showcargoes/{id}/``` - get конкретный груз, put изменить груз, delete удалить

```http://0.0.0.0:8000/showlocations/``` - get получить все локации

```http://0.0.0.0:8000/getlat/``` - post принимает индекс, возвращает широту и долготу.
