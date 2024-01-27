from sdv.lite import SingleTablePreset
import pandas as pd
from sdv.datasets.demo import download_demo
from sdv.metadata import SingleTableMetadata
from sdv.datasets.local import load_csvs
from sdv.evaluation.single_table import get_column_plot

metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath="results/training_data_minority.csv")
real_data = pd.read_csv("results/training_data_minority.csv")


synthesizer = SingleTablePreset(
    metadata,
    name='FAST_ML'
)
synthesizer.fit(data=real_data)
synthetic_data = synthesizer.sample(num_rows=500)
synthetic_data.to_csv("results/synthetic_data.csv", index=False)