from devlog import sum_minutes

def test_sum_minutes():
    content = "2024-06-01 | Math | 30\n2024-06-02 | Science | 45\n"
    assert sum_minutes(content) == 75