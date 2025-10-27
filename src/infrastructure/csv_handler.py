import csv
import os
from datetime import datetime
from pathlib import Path


class CSVHandler:
    
    def __init__(self, filename: str = None, output_dir: str = "output"):
        self.output_dir = output_dir
        self.filename = filename or self._generate_filename()
        self.filepath = self._create_filepath()
        
    def _generate_filename(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"scrapping_{timestamp}.csv"
    
    def _create_filepath(self) -> str:
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        return os.path.join(self.output_dir, self.filename)
    
    def write_csv(self, data: list, headers: list = None):
        if not data:
            print("Nenhum dado para escrever no CSV")
            return
        if not isinstance(data[0], dict):
            data = [self._object_to_dict(item) for item in data]
        if headers is None:
            headers = list(data[0].keys())
        
        try:
            with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            
            print(f"CSV criado com sucesso: {self.filepath}")
            print(f"Total de linhas: {len(data)}")
            
        except Exception as e:
            print(f"Erro ao escrever CSV: {e}")
    
    def append_csv(self, data: list, headers: list = None):
        if not data:
            print("Nenhum dado para adicionar ao CSV.")
            return
        if not isinstance(data[0], dict):
            data = [self._object_to_dict(item) for item in data]
        if headers is None:
            headers = list(data[0].keys())
        file_exists = os.path.isfile(self.filepath)
        
        try:
            with open(self.filepath, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                if not file_exists:
                    writer.writeheader()
                
                writer.writerows(data)
            
            print(f"Dados adicionados ao CSV: {self.filepath}")
            print(f"Linhas adicionadas: {len(data)}")
            
        except Exception as e:
            print(f"Erro ao adicionar ao CSV: {e}")
    
    def _object_to_dict(self, obj) -> dict:
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return {key: getattr(obj, key) for key in dir(obj) 
                    if not key.startswith('_') and not callable(getattr(obj, key))}
    
    def read_csv(self) -> list:
        if not os.path.isfile(self.filepath):
            print(f"Arquivo não encontrado: {self.filepath}")
            return []
        
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            
            print(f"CSV lido com sucesso: {self.filepath}")
            print(f"Total de linhas: {len(data)}")
            return data
            
        except Exception as e:
            print(f"Erro ao ler CSV: {e}")
            return []