from hook.commit_processor import process_commit, insert_prefix, get_prefix
import tempfile

insert_task_code_strategy = "insert_task_code"


def test_parse_task_id_takes_correct_id():
    task_id = '123'
    branch = f'pr/ivanov/{task_id}'
    assert get_prefix(insert_task_code_strategy, branch) == f"#{task_id}"


def test_parse_task_id_complex_message_takes_correct_id():
    task_id = '123'
    branch = f'pr/ivanov/{task_id}-task_description'
    assert get_prefix(insert_task_code_strategy, branch) == f"#{task_id}"


def test_parse_task_id_message_with_digits_takes_correct_id():
    task_id = '123'
    branch = f'pr/ivanov/{task_id}-task_description_kb5'
    assert get_prefix(insert_task_code_strategy, branch) == f"#{task_id}"


def test_insert_task_number_unicode_message():
    with tempfile.NamedTemporaryFile('r+') as tmp:
        # arrange
        original_message = 'Сообщение'
        task_number = 123
        tmp.write(original_message)
        tmp.seek(0, 0)

        # act
        insert_prefix(tmp, task_number)
        tmp.seek(0, 0)
        processed_message = tmp.read()

        # assert
        assert processed_message == f'{task_number} {original_message}'


def test_nothing_inserted_when_branch_name_hasnt_task_number():
    with tempfile.NamedTemporaryFile('r+') as tmp:
        # arrange
        original_message = 'Сообщение'
        tmp.write(original_message)
        tmp.seek(0, 0)

        # act
        process_commit("insert_task_code","pr/ivanov/fake", tmp)
        tmp.seek(0, 0)
        processed_message = tmp.read().strip()

        # assert
        assert processed_message == original_message



