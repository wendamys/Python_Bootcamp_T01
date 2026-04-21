import pytest


class TestPerimeter:

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "number, expected_result, expected_stdout", [
        (1, 1.000, "Perimeter: 1.000\n"),
        (0, 0.000, "Perimeter: 0.000\n"),
        (None, None, "It's not a triangle\n")
    ])
    def test_print_result_calc_the_perimeter(self, perimeter, capsys, number, expected_result, expected_stdout):
        test_data = perimeter.print_result_calc_the_perimeter(number)
        assert test_data == expected_result
        captured = capsys.readouterr()
        assert captured.out == expected_stdout

    @pytest.mark.smoke
    @pytest.mark.parametrize("numbers, expected_result", [
        (["3#", 10, "fsd", 20, 10, 20, 5, 5], [10.0, 20.0, 10.0, 20.0, 5.0, 5.0]),
        (["abc", 5, 5, 5, 5, 5, 5], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]),
        ([0, 0, 0, 0, 0, 0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
    ])
    def test_user_input(self, monkeypatch, perimeter, numbers, expected_result):
        answers = iter(map(str, numbers))
        monkeypatch.setattr("builtins.input", lambda _=None: next(answers))
        result = perimeter.user_input()
        assert result == expected_result

    @pytest.mark.parametrize("numbers, expected_result", [
        ([1.0, 2.0, 2.0, 1.0, 5.0, 5.0], 11.414),
        ([2.0, 1.0, 2.0, 1.0, 2.0, 1.0], None),
        ([2.0, 1.0, 2.0, 1.0, 3.0, 1.0], None)
    ])
    @pytest.mark.smoke
    def test_calc_the_perimeter_of_triangle(self, perimeter, numbers, expected_result):
        result = perimeter.calc_the_perimeter_of_triangle(*numbers)
        if isinstance(result, float):
            result = round(result, 3)
        assert result == expected_result


    @pytest.mark.smoke
    @pytest.mark.parametrize("numbers, expected_result", [
        ([1.0, 2.0, 2.0, 1.0, 5.0, 5.0], 11.414),
        ([2.0, 1.0, 2.0, 1.0, 2.0, 1.0], None),
        ([2.0, 1.0, 2.0, 1.0, 3.0, 1.0], None)
    ])
    def test_integration_user_input_and_calc_perimeter(self, perimeter, capsys, numbers, expected_result, monkeypatch):
        answers = iter(map(str, numbers))
        monkeypatch.setattr("builtins.input", lambda _=None: next(answers))
        user_input = perimeter.user_input()
        calc_the_perimetr = perimeter.calc_the_perimeter_of_triangle(*user_input)
        if isinstance(calc_the_perimetr, float):
            calc_the_perimetr = round(calc_the_perimetr, 3)
        assert calc_the_perimetr == expected_result


    @pytest.mark.smoke
    @pytest.mark.parametrize("numbers, expected_result", [
        ([1.0, 2.0, 2.0, 1.0, 5.0, 5.0], "Perimeter: 11.414\n"),
        ([2.0, 1.0, 2.0, 1.0, 2.0, 1.0], "It's not a triangle\n"),
        ([2.0, 1.0, 2.0, 1.0, 3.0, 1.0], "It's not a triangle\n")
    ])
    def test_e2e_perimeter(self, perimeter, numbers, expected_result, monkeypatch,
                                                                         capsys):
        answers = iter(map(str, numbers))
        monkeypatch.setattr("builtins.input", lambda _=None: next(answers))
        user_input = perimeter.user_input()
        calc_the_perimetr = perimeter.calc_the_perimeter_of_triangle(*user_input)
        if isinstance(calc_the_perimetr, float):
            calc_the_perimetr = round(calc_the_perimetr, 3)
        perimeter.print_result_calc_the_perimeter(calc_the_perimetr)
        captured = capsys.readouterr()
        assert captured.out == expected_result





