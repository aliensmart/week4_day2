from .orm import ORM

class tsla(ORM):
    dbpath = ""
    tablename = "tsla"
    fields = ["Open", "High", "Low", "Close", 
              "Adj_Close", "Volume"]
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.Open = kwargs.get("Open")
        self.High = kwargs.get("High")
        self.Low = kwargs.get("Low")
        self.Close = kwargs.get("Close")
        self.Adj_Close = kwargs.get("Adj_Close")
        self.Volume = kwargs.get("Volume")

