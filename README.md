# fast_api_stepic

## Как запускать локально

1. Активируем виртуальное окружение,
2. Устанавливаем зависимости из файла requirements.txt.
3. Запускаем командой python run.py из главного каталога, где лежит run.py

Если хотите запускать и тестироварть проект в режиме дебаггера, то обратите внимание на структуру проекта:

project_name/<br>
├──.vscode<br>
│ └── launch.json<br>
├── app/<br>
│ └── main.py<br>
├── venv/<br>
└── run.py<br>

В файле launch.json должно быть такое содержимое (это опараметры запуска дебагера)

{
"version": "0.2.0",
"configurations": [
{
"name": "Python: FastAPI Debug",
"type": "debugpy",
"request": "launch",
"program": "${workspaceFolder}/run.py",
"console": "integratedTerminal",
"justMyCode": true,
"env": {
"PYTHONPATH": "${workspaceFolder}"
}
}
]
}
