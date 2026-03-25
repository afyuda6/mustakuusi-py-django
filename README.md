# mustakuusi-java-springboot
for learning purposes

## Start Server
```bash
python manage.py runserver 3006
```

## Get Games
```text
curl -X 'GET' \
  'http://localhost:3006/games' \
  -H 'accept: */*'
```

## Get Characters
```text
curl -X 'GET' \
  'http://localhost:3006/characters' \
  -H 'accept: */*'
```
