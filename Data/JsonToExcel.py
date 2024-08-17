import pandas as pd


class JsonToCsvExcel:

    def __init__(self, data):
        self.data = data

    def export_table_excel(self, filename):
        excel_filename = f"{filename}.xlsx"
        with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
            for key, value in self.data.items():
                if isinstance(value, list):
                    if all(isinstance(item, dict) for item in value):
                        df = pd.json_normalize(value)
                    else:
                        df = pd.DataFrame(value, columns=[key])
                elif isinstance(value, dict):
                    df = pd.json_normalize(value)
                else:
                    df = pd.DataFrame([value], columns=[key])
                if not df.empty:
                    df.to_excel(writer, sheet_name=key, index=False)
                else:
                    print(f"Aviso: A tabela '{key}' está vazia e não será salva.")

        print(f"Data saved to Excel file: {excel_filename}")

    def export_table_csv(self, filename):
        for key, value in self.data.items():
            csv_filename = f"{filename}_{key}.csv"
            if isinstance(value, list):
                if all(isinstance(item, dict) for item in value):
                    df = pd.json_normalize(value)
                else:
                    df = pd.DataFrame(value, columns=[key])
            elif isinstance(value, dict):
                df = pd.json_normalize(value)
            else:
                df = pd.DataFrame([value], columns=[key])
            if not df.empty:
                df.to_csv(csv_filename, index=False)
            else:
                print(f"Aviso: A tabela '{key}' está vazia e não será salva.")

        print(f"Data saved to CSV files with prefix: {filename}")
