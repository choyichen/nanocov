# PCs vs covariates

## Folder Structure

* `data/`:    Metadata
* `ipynb/`:   IPython notebooks
* `plots/`:   Output figures
* `reports/`: Output tables

## Workflow

1. Expression data preprocessing (`ipynb/01_Data_preprocessing.ipynb`)

To preprocess the multi-tissue RNA-seq gene expression data from GTEx v6.

Output: `data/GTEx.samples_to_use.tsv`, `data/GTEx.genes_to_use.tsv`.

2. Association between covariates and PCs using mutual information (MI) (`ipynb/02_PCs_vs_covariates.ipynb`)

To associate covariates with gene expression variation (principal components).

Output:
  * `reports/Global_MI_btw_covariates.unnormalized.tsv`
  * `reports/Global_MI_btw_covariates.tsv`
  * `reports/Tissue-specific_MI_between_PCs_and_covariates.xlsx`
  * `reports/Tissue-specific_PCA_explained_variance_ratios.tsv`

3. Global cluster structure of covariates (`ipynb/03_Global_clusters_of_variables.ipynb`)

Variables are often redundant or dependent. Here we used hierarchial clustering to identify clusters of variables based on MI distance.

Output:
  * A series of clustermap plots at `plots/Global_MI_btw_covariates.[average/complete/single].pdf` & `.labels`.
  * Also, `plots/Global_MI_btw_covariates.unnormalized.pdf`, which was based on unnormalized MI.

4. Global MI matrix to edge lists (`ipynb/04_Global_MI_matrix_to_edgelist.ipynb`)

MI matrix can be seen as a weighted adjacency matrix. Here we transformed the MI matrix to edge list, using different levels of MI cutoffs.

Output: `data/Global_MI_btw_covariates.edgelist`
