from graphs.course_schedule import CourseSchedule


def test_can_finish_true():
    assert CourseSchedule().canFinish(2, [[1, 0]]) is True


def test_can_finish_false_cycle():
    assert CourseSchedule().canFinish(2, [[1, 0], [0, 1]]) is False


def test_no_prerequisites():
    assert CourseSchedule().canFinish(3, []) is True


def test_complex_graph():
    assert CourseSchedule().canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True