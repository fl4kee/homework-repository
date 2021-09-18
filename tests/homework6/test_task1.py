from homework6.task1 import instances_counter


def test_instances_counter():
    @instances_counter
    class User:
        pass
    assert User.get_created_instances() == 0
    _, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
