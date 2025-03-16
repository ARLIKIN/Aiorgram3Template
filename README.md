# Aiogram Template
Это шаблон для telegram-ботов от angiogram 3.X 
с использованием локализации fluentogram


## **How to use🤔**
1. [**Setup environment variables**](https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm)
   - [TOKEN](https://telegram.me/BotFather)
   - DEBUG = True если хотите использовать SQLite
2. [**Setup handlers**](bot/handlers)
   - [Admin](bot/handlers/admin/main.py)
   - [User](bot/handlers/user/main.py)
3. [**Localization**](bot/service/i18n.py)
   - [settings](bot/service/i18n.py)
4. Run [run.py](run.py)


## Миграции

1. Что бы создать выполните команду 
```sh
shalembic revision --autogenerate -m «name_migrate»
```

2. При запуске бота автоматически применяется последняя миграция
