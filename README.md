# bulletin_board_system
1. Установить зависимости `pip install -r requirements.txt`
2. migrate `python manage.py migrate` or `make migrate`
3. create superuser (admin)
`python manage.py createsuperuser --username admin --email admin@admin.com`
4. run app `make run`

## Git комманды
### сделать ветку и переключитья на неё
`git checkout -b <name>`

### изменения в локальном репозитории вносятся в удалённый репозиторий
`git push -u origin <name>`

### посмотреть удаленные (внешние) подлючения
`git remote -v `

### добавить удаленный репозиторий
`git remote add origin <remote name>`
