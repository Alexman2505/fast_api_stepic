# fast_api_stepic

## Локальный запуск, в т.ч. в режиме дебаггера.

1. Создаем и активируем виртуальное окружение venv,
2. Устанавливаем зависимости из файла requirements.txt в это виртуальное окружение.
3. Запускаем приложение командой python run.py из главного каталога, где лежит run.py

Если хотите запускать и тестировать проект в режиме дебаггера, то обратите внимание на структуру проекта:

````project_name/
```├──.vscode
```│ └── launch.json
```├── app/
```│ └── main.py
```├── venv/
```└── run.py
````

Проект разрабатывается в IDE vscode, поэтому содержимое launch.json из папки .vscode для удобного запуска дебаггера через кнопку f5 должно быть таким.

{<br>
"version": "0.2.0",<br>
"configurations": [<br>
{<br>
"name": "Python: FastAPI Debug",<br>
"type": "debugpy",<br>
"request": "launch",<br>
"program": "${workspaceFolder}/run.py",<br>
"console": "integratedTerminal",<br>
"justMyCode": true,<br>
"env": {<br>
"PYTHONPATH": "${workspaceFolder}"<br>
}<br>
}<br>
]<br>
}<br>
