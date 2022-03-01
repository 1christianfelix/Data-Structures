import pytest

def test_circular_queue_class_exists():
    from circular_queue import CircularQueue


def test_circular_queue_constructor_has_required_size_argument_and_sets_property():
    from circular_queue import CircularQueue
    with pytest.raises(TypeError):
        CircularQueue()
    queue = CircularQueue(10)
    assert queue.size == 10


def test_new_queue_has_head_and_tail_set_to_zero():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    assert queue.head == 0
    assert queue.tail == 0
