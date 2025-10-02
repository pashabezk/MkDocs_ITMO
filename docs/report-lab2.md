# Отчёт ЛР 2.2

**Отчёт о лабораторной работе «Кастомизация статического сайта»**

```sh
# создание виртуального окружения
python -m venv venv

# активация виртуального окружения
venv/Scripts/Activate.ps1

# установка темы
pip install mkdocs-bootswatch

# фиксация пакетов в файл
pip freeze > requirements.txt
```

Обновил файл mkdocs.yaml для подключения темы

```yml
theme:
    name: flatly
```

Добавим свои стили, чтоб прижать футер к низу страницы

Для этого был создан файл `/docs/styles/styles.css`

Обновил файл mkdocs.yaml для подключения css

```yml
extra_css:
  - styles/styles.css
```
