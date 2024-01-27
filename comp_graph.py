from sdv.evaluation.single_table import get_column_plot
import pandas as pd
from sdv.metadata import SingleTableMetadata

real_data = pd.read_csv("results/training_data_minority.csv")
synthetic_data = pd.read_csv("results/synthetic_data.csv")
metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath="results/base_data.csv")

fig = get_column_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_name='Class',
    metadata=metadata
)

fig.show()