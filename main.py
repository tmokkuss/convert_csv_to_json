import unittest
import convert


class TestConvert(unittest.TestCase):
    def test_format_key_value(self):
        data = '    "id": 1.0'
        result = convert.format_key_value('id', '1.0')
        self.assertEqual(result, data)

    def test_format_value_type_str(self):
        data = '"Alex"'
        result = convert.format_value_type('Alex')
        self.assertEqual(result, data)

    def test_format_value_type_bool(self):
        data = 'true'
        result = convert.format_value_type('True')
        self.assertEqual(result, data)

    def test_format_value_type_number(self):
        data = '1.0'
        result = convert.format_value_type('1.0')
        self.assertEqual(result, data)

    def test_csv_content_to_json_content(self):
        data = [{"id": 1.0, "name": "Alex", "salary": 150000, "department": True},
                {"id": 2.5, "name": "Joe", "salary": 200000, "department": False},
                {"id": 3.2, "name": "Frodo", "salary": 100000, "department": False}]
        content = convert.read_file('data.csv')
        result = [
                  {
                    "id": 1.0,
                    "name": "Alex",
                    "salary": 150000,
                    "department": True
                  },
                  {
                    "id": 2.5,
                    "name": "Joe",
                    "salary": 200000,
                    "department": False
                  },
                  {
                    "id": 3.2,
                    "name": "Frodo",
                    "salary": 100000,
                    "department": False
                  }
                ]
        self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()
