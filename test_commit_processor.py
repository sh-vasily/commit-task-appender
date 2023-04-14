from hook.commit_processor import parse_task_id


def test_parse_task_id_takes_correct_id():
    task_id = '123'
    commit_message = f'pr/ivanov/{task_id}'
    assert parse_task_id(commit_message) == task_id


def test_parse_task_id_complex_message_takes_correct_id():
    task_id = '123'
    commit_message = f'pr/ivanov/{task_id}-task_description'
    assert parse_task_id(commit_message) == task_id


def test_parse_task_id_message_with_digits_takes_correct_id():
    task_id = '123'
    commit_message = f'pr/ivanov/{task_id}-task_description_kb5'
    assert parse_task_id(commit_message) == task_id
