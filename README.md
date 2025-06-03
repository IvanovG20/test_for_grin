## Запуск проекта локально
Склонируйте репозиторий
```
git clone git@github.com:IvanovG20/test_for_grin.git
```
Перейдите в директорию проекта
```
cd test_for_grin/
```

Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Создать файл .env:
```
touch .env
```

Заполнить файл .env в соотвествии с примером:
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432
```
Запустить контейнеры локально следующей командой:
```
docker-compose up -d
```
С этого момента проект будет доступен по адресу:
```
http://localhost:8000/
```
