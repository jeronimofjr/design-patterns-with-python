import json
import xml.etree.ElementTree as etree

class JSONDataExtractor:

    def __init__(self, filepath) -> None:
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data
    
class XMLDataExtractor:
    def __init__(self, filepath) -> None:
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
    

def dataextraction_factory(filepath: str):
    if filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f"Cannot extract data from {filepath}")
    return extractor(filepath)

def extract_data_from(filepath):
    factory_obj = None

    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj



objeto = extract_data_from('data/movie.json')

print(objeto.parsed_data)