from evaluation.helpers.get_data_block import get_data_block
from visuals.plot_availability_matrix import plot_availability_matrix
import matplotlib.pyplot as plt
import numpy as np

df, _, _, _ = get_data_block(
    num_cells=5,
    num_perts=1000,
    cell_start=0,
    name='level2'
)


plt.clf()
plt.grid(False)
plot_availability_matrix(df)
plt.savefig('visuals/figures/availability_subset.png', dpi=500, transparent=True)

counts = df.groupby(['intervention', 'unit']).size()
sorted_perturbations = counts.groupby('intervention').size().sort_values(ascending=True)
sorted_celltypes = counts.groupby('unit').size().sort_values(ascending=False)
count_matrix = np.zeros((len(sorted_perturbations), len(sorted_celltypes)))


import seaborn as sns
sns.set()

plt.figure(figsize=(10, 10))
plt.scatter(list(range(len(sorted_celltypes))), list(sorted_celltypes.values))
plt.ylabel('Number of Perturbations')
plt.xlabel('Cell Type')
plt.xticks(list(range(len(sorted_celltypes))))
ax = plt.gca()
ax.tick_params(axis='x', bottom=False, top=False, labelsize='small')
ax.set_xticklabels(sorted_celltypes.index, ha='right', rotation=70)
plt.tight_layout()
plt.savefig('visuals/figures/sorted_celltypes_subset.png')

sns.set()
plt.figure(figsize=(10, 10))
plt.scatter(list(range(len(sorted_perturbations))), list(reversed(sorted_perturbations.values)))
plt.ylabel('Number of Cell Types')
plt.xlabel('Perturbation')
plt.tight_layout()
plt.savefig('visuals/figures/sorted_perturbations_subset.png')
