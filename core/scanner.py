
from concurrent.futures import ThreadPoolExecutor, as_completed

class EnterpriseScanner:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        
    def bulk_scan(self, urls):
        futures = {self.executor.submit(self.scan_url, url): url for url in urls}
        results = []
        
        for future in as_completed(futures):
            url = futures[future]
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Error scanning {url}: {str(e)}")
        return results
