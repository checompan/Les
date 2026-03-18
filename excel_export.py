import pandas as pd

def export_registrations(data,filename):
    df = pd.DataFrame(data)
    df.to_excel(filename,index=False)