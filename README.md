# fast_api_stepic

## Как запускать локально

Обратите внимание, что на структуру проекта:

project_name/<br>
+-- app/<br>
| +-- \_\_init\_\_.py<br>
| +-- main.py<br>
+-- venv/<br>

В файле main.py в самом низу прописаны параметры запуска

if \_\_name\_\_ == "\_\_main\_\_":
uvicorn.run("main:app", host= "localhost", port=8000, reload=True)
\# запуск через "python app/main.py"

Соответственно, активируем виртуальное окружение, устанавливаем зависимости из файла requirements.txt.
А весь проект запускаем как обычный питоновский файл из консоли bash командой python app/main.py
