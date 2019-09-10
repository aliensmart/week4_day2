from .tsla import tsla
import csv

def run():
    with open("TSLA.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # entry = tsla(Open=row["Open"], High=row["High"], Low=row["Low"],
            #             Adj_Close=row["Adj_Close"], Volume=row["Volume"])
            entry = tsla(**row)
            
            entry.save()
