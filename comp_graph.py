from sdv.evaluation.single_table import get_column_plot
import pandas as pd
from sdv.metadata import SingleTableMetadata

real_data = pd.read_csv("results/base_data.csv")
synthetic_data = pd.read_csv("results/synthetic_data.csv")
#synthetic_data = synthetic_data.drop('Unnamed: 0.1', axis=1)

metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath="results/base_data.csv")

fig = get_column_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_name='amenities_fee',
    metadata=metadata
)

fig.show()