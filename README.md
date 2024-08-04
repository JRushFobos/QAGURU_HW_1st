# Домашнее задание №1 QA.GURU | Python Advanced | Автоматизация
## Домашнее задание №1

1. Разработать несколько API-автотестов на https://reqres.in (если обучались на основном курсе python - можно взять код автотестов из домашнего задания) Можно также за основу взять https://github.com/qa-guru/qa_guru_python_9_19

2. Вместо https://reqres.in разработать свой микросервис в стеке Python + FastAPI (допускается также Flask, Django).
Пример - https://github.com/qa-guru/python-advanced-intro
    - Автотесты должны также успешно проходить.
    - В коде микросервиса не должно быть хардкода. Например, не должно быть эндпоинтов типа /api/users/2 -  правильнее /api/users/{user_id}
3. Данные для ответа пока что можно хранить в текстовом файле, в следующих занятиях мы перенесем их в базу данных
4. Оформить README.md - https://school.qa.guru/teach/control/stream/view/id/465999013 в тренинге есть несколько занятий по оформлению красивой документации.

## Домашнее задание №2
1. Расширить тестовое покрытие smoke тестами на доступность микросервиса.
2. Добавить сервисный эндпоинт /status для проверки доступности микросервиса.
3. Использовать библиотеку fastapi-pagination для базовой пагинации в эндпоинтах, которые возвращают список объектов.
4. Добавить тесты на пагинацию. Тестовых данных должно быть достаточно для проверки пагинации (не менее 10).
5. Проверяем:
   - ожидаемое количество объектов в ответе;
   - правильное количество страниц при разных значениях size;
   - возвращаются разные данные при разных значениях page;

## Домашнее задание №3
1. Запустить postgresql в докере.
   Запустить проект локально (в докере будем запускать в следующем занятии).
2. Расширить тестовое покрытие:
- Тест на post: создание. Предусловия: подготовленные тестовые данные
- Тест на delete: удаление. Предусловия: созданный пользователь
- Тест на patch: изменение. Предусловия: созданный пользователь
По желанию:
- Get после создания, изменения
- Тест на 405 ошибку: Предусловия: ничего не нужно
- 404 422 ошибки на delete patch
- 404 на удаленного пользователя
- user flow: создаем, читаем, обновляем, удаляем
- валидность тестовых данных (емейл, урл)
- отправить модель без поля на создание

## Технологии
1. Микросервис: Python + FastAPI
2. Тесты: Python + Pytest + Requests

## Микросервис примеры запросов
#### POST запрос /api/users с JSON-body
```{
    "first_name": "Rachel",
    "last_name": "Howell",
    "email": "rachel.howell@reqres.in",
    "avatar": "https://reqres.in/img/faces/1-image.jpg"
}
```
#### PUT/PATCH запросы /api/users/{id} с JSON-body
```{
    "first_name": "Rachel",
    "last_name": "Howell",
    "email": "rachel.howell@reqres.in",
    "avatar": "https://reqres.in/img/faces/1-image.jpg"
}
```
#### GET запрос /api/users/{id}
#### GET запрос /api/users/
#### DELETE запрос /api/users/{id}

## Запуск проекта (локально)
1. python -m venv venv
2. source venv/Scripts/activate
3. pip install -r requirements.txt
4. uvicorn main:app —reload
5. pytest

## Автор 
Мокрушин Евгений

