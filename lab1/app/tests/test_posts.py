import pytest

def test_posts_index(client):
    response = client.get("/posts")
    assert response.status_code == 200
    assert "Последние посты" in response.text

def test_posts_index_template(client, captured_templates, mocker, posts_list):
    with captured_templates as templates:
        mocker.patch(
            "app.posts_list",
            return_value=posts_list,
            autospec=True
        )
        
        _ = client.get('/posts')
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'posts.html'
        assert context['title'] == 'Посты'
        assert len(context['posts']) == 1

# 1. Тесты на базовые страницы (Маршруты)
def test_index_status(client):
    assert client.get('/').status_code == 200

def test_about_status(client):
    assert client.get('/about').status_code == 200

# 2. Тесты на страницу конкретного поста (Детализация)
def test_post_detail_status(client):
    # Проверяем первый пост (индекс 0)
    response = client.get('/posts/0')
    assert response.status_code == 200

# 3. Тест на 404 (Несуществующий пост)
def test_post_not_found(client):
    # У нас всего 5 постов, индекс 99 должен вернуть 404
    # Примечание: проверь в app.py, чтобы там была обработка ошибки индекса!
    response = client.get('/posts/99')
    assert response.status_code == 404

# 4. Проверка наличия ВСЕХ данных поста (Заголовок, Автор, Текст, Дата, Картинка)
def test_post_content_data(client):
    response = client.get('/posts/0')
    html = response.text
    assert "Заголовок поста" in html  # Заголовок
    assert "Автор:" in html           # Имя автора
    assert ".jpg" in html             # Изображение
    assert "<p>" in html              # Текст поста (в тегах абзаца)

# 5. Проверка формата даты (ДД.ММ.ГГГГ)
def test_post_date_format(client):
    response = client.get('/posts/0')
    import re
    # Регулярка для поиска даты вида 22.08.2026
    date_pattern = r'\d{2}\.\d{2}\.\d{4}'
    assert re.search(date_pattern, response.text)

# 6. Проверка формы комментариев
def test_post_has_comment_form(client):
    response = client.get('/posts/0')
    assert '<form' in response.text
    assert '<textarea' in response.text
    assert 'Отправить' in response.text

# 7. Проверка наличия комментариев
def test_post_has_comments_list(client):
    response = client.get('/posts/0')
    assert 'Комментарии' in response.text

# 8. Проверка футера (ФИО и Группа)
def test_footer_info_present(client):
    response = client.get('/')
    assert "Выполнил:" in response.text
    assert "Группа:" in response.text

# 9. Проверка использования правильного шаблона для поста
def test_post_template_used(client, captured_templates):
    with captured_templates as templates:
        client.get('/posts/0')
        assert templates[0][0].name == 'post.html'

# 10. Проверка передачи данных в шаблон поста
def test_post_context_data(client, captured_templates):
    with captured_templates as templates:
        client.get('/posts/0')
        context = templates[0][1]
        assert 'post' in context
        assert 'title' in context

@pytest.mark.parametrize("index", [0, 1, 2, 3, 4])
def test_all_posts_load_correctly(client, index):
    # Этот код создаст СРАЗУ 5 ТЕСТОВ (по одному на каждый индекс)
    response = client.get(f'/posts/{index}')
    assert response.status_code == 200