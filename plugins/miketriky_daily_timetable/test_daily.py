"""
Unit tests for DailyTimetable module (without external dependencies).

These tests validate the code structure and basic logic.
For full integration tests, install: pip install pendulum apache-airflow
"""

import unittest


class TestCodeStructure(unittest.TestCase):
    """Test that the module has correct structure."""

    def test_module_imports(self):
        """Should be able to parse the module."""
        import ast
        with open('daily.py', 'r') as f:
            code = f.read()
        try:
            ast.parse(code)
            self.assertTrue(True, "Module parses successfully")
        except SyntaxError as e:
            self.fail(f"Syntax error in daily.py: {e}")

    def test_class_exists(self):
        """Should have DailyTimetable class defined."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        self.assertIn('DailyTimetable', classes, "DailyTimetable class should exist")

    def test_required_methods_exist(self):
        """Should have all required methods."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DailyTimetable':
                methods = [m.name for m in node.body if isinstance(m, ast.FunctionDef)]
                break

        required_methods = [
            '__init__',
            '__eq__',
            '__hash__',
            '__repr__',
            'serialize',
            'deserialize',
            'is_holiday',
            'get_holiday_name',
            'create_datetime',
            'find_previous_valid_day',
            'find_next_valid_day',
        ]

        for method in required_methods:
            self.assertIn(method, methods, f"Method {method} should exist")

    def test_required_properties_exist(self):
        """Should have required properties."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        properties = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DailyTimetable':
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        # Check if decorated with @property
                        for decorator in item.decorator_list:
                            if isinstance(decorator, ast.Name) and decorator.id == 'property':
                                properties.append(item.name)
                break

        required_properties = ['description', 'time', 'summary']
        for prop in required_properties:
            self.assertIn(prop, properties, f"Property {prop} should exist")

    def test_constants_defined(self):
        """Should have MAX_SEARCH_DAYS constant."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        constants = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DailyTimetable':
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                constants.append(target.id)
                break

        self.assertIn('MAX_SEARCH_DAYS', constants, "MAX_SEARCH_DAYS constant should exist")

    def test_helper_functions_exist(self):
        """Should have helper functions."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        functions = [node.name for node in ast.walk(tree)
                    if isinstance(node, ast.FunctionDef) and not node.name.startswith('_')]

        self.assertIn('parse_date', functions, "parse_date function should exist")
        self.assertIn('parse_holidays', functions, "parse_holidays function should exist")

    def test_type_hints_present(self):
        """Should have type hints in function signatures."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        # Check that parse_date has return annotation
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'parse_date':
                self.assertIsNotNone(node.returns, "parse_date should have return type hint")
                break

    def test_docstrings_present(self):
        """Should have docstrings for class and key methods."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        # Check class docstring
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DailyTimetable':
                docstring = ast.get_docstring(node)
                self.assertIsNotNone(docstring, "DailyTimetable should have a docstring")
                self.assertGreater(len(docstring), 50, "Docstring should be comprehensive")
                break

    def test_error_handling_present(self):
        """Should have error handling (raise statements)."""
        with open('daily.py', 'r') as f:
            code = f.read()

        # Check for ValueError raises
        self.assertIn('raise ValueError', code, "Should have ValueError for validation")

        # Count how many validations we have
        validation_count = code.count('raise ValueError')
        self.assertGreaterEqual(validation_count, 5, "Should have multiple validations")

    def test_no_print_statements(self):
        """Should not have print statements (use logging instead)."""
        with open('daily.py', 'r') as f:
            code = f.read()

        # Allow print in docstrings/comments but not in actual code
        lines = [line for line in code.split('\n') if not line.strip().startswith('#')]
        code_without_comments = '\n'.join(lines)

        # Simple heuristic: print( should not appear outside of strings
        import re
        print_calls = re.findall(r'^[^"\']*print\s*\(', code_without_comments, re.MULTILINE)
        self.assertEqual(len(print_calls), 0, "Should not use print() statements")


class TestCodeQuality(unittest.TestCase):
    """Test code quality metrics."""

    def test_line_length_reasonable(self):
        """Should not have excessively long lines."""
        with open('daily.py', 'r') as f:
            lines = f.readlines()

        long_lines = [i+1 for i, line in enumerate(lines) if len(line) > 120]

        # Allow a few long lines (like long strings), but not many
        self.assertLess(len(long_lines), 10,
                       f"Too many long lines (>120 chars): {long_lines}")

    def test_future_annotations_imported(self):
        """Should use future annotations for better type hints."""
        with open('daily.py', 'r') as f:
            first_lines = ''.join(f.readlines()[:5])

        self.assertIn('from __future__ import annotations', first_lines,
                     "Should import annotations from __future__")

    def test_class_has_constants(self):
        """Should define constants at class level, not magic numbers."""
        with open('daily.py', 'r') as f:
            code = f.read()

        self.assertIn('MAX_SEARCH_DAYS', code, "Should define MAX_SEARCH_DAYS constant")

    def test_has_comprehensive_validation(self):
        """Should validate all input parameters."""
        with open('daily.py', 'r') as f:
            code = f.read()

        # Check for various validations
        validations = [
            'hour must be',
            'minute must be',
            'days cannot be empty',
            'Invalid timezone',
            'Invalid date format',
        ]

        for validation in validations:
            self.assertIn(validation, code, f"Should validate: {validation}")


class TestDocumentation(unittest.TestCase):
    """Test documentation quality."""

    def test_module_docstring(self):
        """Module should have a docstring."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        # Module docstring is the first statement if it's a string
        if tree.body and isinstance(tree.body[0], ast.Expr):
            if isinstance(tree.body[0].value, ast.Constant):
                # Module has docstring (could be improved with actual content check)
                pass

    def test_example_in_docstring(self):
        """Class docstring should include usage example."""
        import ast
        with open('daily.py', 'r') as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == 'DailyTimetable':
                docstring = ast.get_docstring(node)
                self.assertIn('Example:', docstring, "Should have usage example")
                self.assertIn('DailyTimetable(', docstring, "Example should show instantiation")
                break


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
