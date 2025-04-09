
import json
import csv
from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate(results, format='json'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == 'json':
            filename = f"report_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
                
        elif format == 'csv':
            filename = f"report_{timestamp}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['URL', 'Card Type', 'BIN', 'Full Number'])
                for result in results:
                    writer.writerow([
                        result['url'],
                        result['type'],
                        result['bin'],
                        result['card_number']
                    ])
        return filename
