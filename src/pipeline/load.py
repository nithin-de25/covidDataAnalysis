import pandas as pd
import os
import json
from datetime import datetime


def to_csv(data, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.DataFrame([data])
    filename = f"{output_dir}/weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    return filename
