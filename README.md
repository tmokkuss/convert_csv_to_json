+ [Программа, которая конвертирует CSV файл в JSON файл](#csv-to-json-code)
+ [Unit тест для конвертере](#unit-тест-для-конвертере)
+ [Метод чтения файла](#метод-чтения-файла)
+ [Метод форматирования вывода](#метод-форматирования-вывода)
+ [Метод определения типа значения и формат его записи](#метод-определения-типа-значения-и-формат-его-записи)
+ [Метод записи](#метод-записи)
+ [Метод конвертации csv в json](#метод-конвертации-csv-в-json)
+ [Метод конвертации файлов](#метод-конвертации-файлов)

## Программа, которая конвертирует CSV файл в JSON файл

Полный код:

```python
def read_file(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    return content


def format_key_value(key, value):
    return 4 * ' ' + '"' + key + '"' + ': ' + value


def format_value_type(value):
    if value.isalpha():
        if value not in ['True', 'False']:
            return '"' + value + '"'
        return value.lower()
    else:
        return value


def write_data(file_name, content):
    f = open(file_name, "w")
    f.write(content)
    f.close()


def csv_content_to_json_content(csv_content):
    keys = csv_content[0].split(',')
    result = '[' + '\n'
    csv_content.pop(0)
    for row_index, row in enumerate(csv_content):
        result += 2 * ' ' + '{' + '\n'
        values = row.split(',')
        zipped_key_value = dict(zip(keys, values))
        len_dict = len(zipped_key_value)

        for key_index, key in enumerate(zipped_key_value):
            result += format_key_value(key, format_value_type(zipped_key_value[key]))
            if key_index + 1 != len_dict:
                result += ','
            result += '\n'

        result += 2 * ' ' + '}'
        if row_index + 1 != csv_content:
            result += ','
        result += '\n'
    result += ']'
    return result


def csv_file_to_json_file(input_file, output_file):
    csv_content = read_file(input_file)
    json_result = csv_content_to_json_content(csv_content)
    write_data(output_file, json_result)


csv_file_to_json_file('data.csv', 'data.json')


```


## Unit тест для конвертера



```python
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

```
## Метод чтения файла
Код метода:

```python
def read_file(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    return content
```

## Метод форматирования вывода

Код метода:

```python
def format_key_value(key, value):
    return 4 * ' ' + '"' + key + '"' + ': ' + value
```

## Метод определения типа значения и формат его записи

Код метода:

```python
def format_value_type(value):
    if value.isalpha():
        if value not in ['True', 'False']:
            return '"' + value + '"'
        return value.lower()
    else:
        return value
```

## Метод записи

Код метода:

```python
def write_data(file_name, content):
    f = open(file_name, "w")
    f.write(content)
    f.close()


```


## Метод конвертации csv в json

Код метода:

```python
def csv_content_to_json_content(csv_content):
    keys = csv_content[0].split(',')
    result = '[' + '\n'
    csv_content.pop(0)
    for row_index, row in enumerate(csv_content):
        result += 2 * ' ' + '{' + '\n'
        values = row.split(',')
        zipped_key_value = dict(zip(keys, values))
        len_dict = len(zipped_key_value)

        for key_index, key in enumerate(zipped_key_value):
            result += format_key_value(key, format_value_type(zipped_key_value[key]))
            if key_index + 1 != len_dict:
                result += ','
            result += '\n'

        result += 2 * ' ' + '}'
        if row_index + 1 != csv_content:
            result += ','
        result += '\n'
    result += ']'
    return result
```


## Метод конвертации файлов

Код метода:

```python
def csv_file_to_json_file(input_file, output_file):
    csv_content = read_file(input_file)
    json_result = csv_content_to_json_content(csv_content)
    write_data(output_file, json_result)
```
