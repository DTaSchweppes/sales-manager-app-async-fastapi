# sales-manager-app-async-fastapi
Приложение для менеджеров по продажам в компании торгующей оптом
Приложение содержит следующие эндпоинты:
![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/4055f778-2043-4cb6-b9fc-92fd2e8cbfa1)
Среди которых CRUD эндпоинты для товара (создание, просмотр, удаление, обновление)

А так же эндпоинты для создания необходимых для товара сущностей: "Поставщик", "Бренд" и небольшая двухуровневая иерархия категорий:
![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/be8b4910-2b1a-414c-9a6d-1eddb07afb28)

![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/760bcec4-bda4-4973-837c-39ea4b03f9f8)
Все операции асинхронны
![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/160d19c1-d5cb-4131-92d8-f2b2485c2330)

![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/6c45251f-60e7-491f-9a1b-c3d16078f396)
используется asyncpg

Так же для всех эндпоинтов написаны тесты:
![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/363de68b-0494-4aaa-8d77-3e5ff91c3cbc)


Созданы и запущены контейнеры приложения и БД:
![image](https://github.com/DTaSchweppes/sales-manager-app-async-fastapi/assets/45369246/1293128e-dcdc-417f-80a7-937ed5b50c7a)
