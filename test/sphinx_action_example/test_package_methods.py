from sphinx_action_example import package_methods


def test_example_function1():
    assert package_methods.example_function1(1, 5.1) == 6.1
