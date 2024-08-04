# fast_api_stepic

## Локальный запуск, в т.ч. в режиме дебаггера.

1. Активируем виртуальное окружение,
2. Устанавливаем зависимости из файла requirements.txt.
3. Запускаем командой python run.py из главного каталога, где лежит run.py

Если хотите запускать и тестироварть проект в режиме дебаггера, то обратите внимание на структуру проекта:

````project_name/<br>
```├──.vscode<br>
```│ └── launch.json<br>
```├── app/<br>
```│ └── main.py<br>
```├── venv/<br>
```└── run.py<br>

Содержимое launch.json для удобного запуска дебаггера через f5.

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






````
