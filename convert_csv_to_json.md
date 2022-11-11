+ [Программа, которая конвертирует CSV файл в JSON файл](#csv-to-json-code)
+ [Метод чтения файла](#метод-чтения-файла)
+ [Метод форматирования вывода](#метод-форматирования-вывода)
+ [Метод определения типа значения и формат его записи](#методопределениятипазначенияиформатегозаписи)
+ [Метод записи](#методзаписи)
+ [Метод конвертации csv в json](#методконвертацииcsvвjson)
+ [Метод конвертации файлов](#методконвертациифайлов)

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


