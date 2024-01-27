from sdv.evaluation.single_table import get_column_plot
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
from sdv.evaluation.single_table import run_diagnostic

real_data = pd.read_csv("results/training_data_minority.csv")
synthetic_data = pd.read_csv("results/synthetic_data.csv")
#synthetic_data = synthetic_data.drop('Unnamed: 0.1', axis=1)

metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath="results/base_data.csv")


diagnostic = run_diagnostic(
    real_data=real_data,
    synthetic_data=synthetic_data,
    metadata=metadata
)

quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
)

#print(quality_report.get_details('Column Shapes'))

'''
fig = get_column_plot(
    real_data=real_data,
    synthetic_data=synthetic_data,
    column_name='amenities_fee',
    metadata=metadata
)

fig.show()
'''