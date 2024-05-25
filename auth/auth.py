class Session():
    def __init__(self, api_key: str, panel_url):
        self.api_key = api_key
        self.panel_url = panel_url
    
    def abandon(self):
        self.api_key = ""
        
