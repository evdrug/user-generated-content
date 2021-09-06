# Описание структуры проекта

- architecture: здесь изложено описание архитектуры всего проекта
- research: результаты исследования для выбора между ClickHouse и Vertica
- etl: сервис перегрузки данных из Kafka в ClickHouse
- uga_api: сервис для сохранения пользовательской активности
- ugc_api: сервис для сохранения пользовательских оценок
- nginx: сервис с nginx, чтоб открыть ugc_api и uga_api во внешний мир

> **NOTE:** код этого модуля содержится в ugc_api, настроена работа CI и наряжена красивая ELK. 
> (Кто делал опишите)

# Запуск проекта

# Auth

Запуск сервиса авторизации:

```shell
git clone https://github.com/vctecc/Auth_sprint_2
cd Auth_sprint_2
```
Задаем **SECRET_KEY** и **JWT_SECRET_KEY**
```
docker compose up --build
```

# UGC
Запуск сервиса:

Задаем **JWT_SECRET_KEY**
```shell
docker compose up --build
```
> **NOTE:** Авторизация uga_api делается локально. Считаем эти данные не критичными, а обращений 
> к сервису планируется много. Для просто считаем что JWT_SECRET_KEY между сервисами передается безопасным
> способом. Данные в ugc_api считаем уловно важными, за проверкой каждый раз ходим
> в сервис авторизации для проверки токена в blacklist и возможности выхода из всех сессий. 
> Обработка токена в ugc_api сделана кое-как с большим дублированием кода, на это уже
> есть [бага](https://github.com/emiliskan/ugc_sprint_2/issues/9), работы по рефакторингу ведутся,
> виновные наказаны.
# Хранилища и всякое
ClickHouse, Kafka и MongoDB подняты в Yandex Cloud.
Параметры соединения к ним прописаны в env файле.

Результаты тестирования MongoDB и возможно актуальную структуру БД можно найти [тут](https://github.com/emiliskan/ugc_sprint_2/blob/main/research/mongo/README.md). 
