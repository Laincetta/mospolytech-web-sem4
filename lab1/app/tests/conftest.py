import sys
import os
from datetime import datetime
import pytest
from flask import template_rendered
from contextlib import contextmanager

# Добавляем путь к папке с app.py в систему, чтобы Python его точно нашел
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Пробуем импортировать объект app из файла app.py
    from app import app as application
except ImportError:
    # Если запуск идет из корня lab1
    from app.app import app as application

@pytest.fixture
def app():
    application.config.update({
        "TESTING": True,
    })
    return application

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture
def posts_list():
    return [
        {
            'title': 'Заголовок поста',
            'text': 'Текст поста',
            'author': 'Иванов Иван Иванович',
            'date': datetime(2025, 3, 10),
            'image_id': '123.jpg',
            'comments': []
        }
    ]