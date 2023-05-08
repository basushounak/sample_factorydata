import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

csv_file = 'millingmachinedata1.csv'
encoding = detect_encoding(csv_file)
print("File Encoding:" , encoding)

