# Curvature-FCN-Aging

This repository provides the datasets and codes associated with the following manuscript:<br>
<i>Discrete Ricci curvatures capture age-related changes in human brain functional connectivity networks,</i><br>
Yasharth Yadav, Pavithra Elumalai, Nitin Williams, Jürgen Jost, Areejit Samal*,<br>
(*Corresponding author)

# Summary of workflow and results

* We applied two notions of discrete Ricci curvature, namely Forman-Ricci curvature (FRC) and Ollivier-Ricci curvature (ORC), to study age-related changes in functional connectivity networks (FCNs) of 225 healthy human subjects in the MPI-LEMON dataset.
* Out of the 225 subjects in the MPI-LEMON dataset included in our study, 153 subjects belonged to the **healthy young** group and 72 subjects belonged to the **healthy elderly** group.
* We acquired raw resting state fMRI scans of the 225 subjects in the MPI-LEMON dataset, and preprocessed them using the MATLAB based CONN toolbox. 
* The preprocessing pipeline used in this study is identical to our [previous work on autism spectrum disorder](https://doi.org/10.1038/s41598-022-12171-y "Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder") , and we have published earlier a protocol video explaining this pipeline which is available at https://youtu.be/ch7-dOA-Vlo

![network example](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/summary_figure.png)

# Repository Organization

The repository is organized into two folders, [CODE](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/CODE) and [DATA](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA). A description of the files contained in each folder is provided below.

## DATA

1. **List of included subjects:**
A list of the 225 subjects from the MPI-LEMON dataset included in our work is provided in the file [cohort_information.tsv](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/DATA/cohort_information.tsv). The file contains information on the ID, age, sex and cohort of the included subjects.

2. **Functional Connectivity (FC) Matrix:**
The preprocessed fMRI scan of each subject was parcellated into 200 regions of interest (ROIs) or nodes defined according to the [Schafer atlas](https://doi.org/10.1093/cercor/bhx179 "Local-Global Parcellation of the Human Cerebral Cortex from Intrinsic Functional Connectivity MRI"), and a 200 × 200 functional connectivity matrix was generated for each subject by computing the Pearson correlation coefficient between the time-series of all pairs of ROIs. The subfolder [FCM](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA/FCM) contains the FC matrix for each subject in weighted edgelist format. Each edgelist file can be uniquely identifed by subject ID.

3. **Functional Connectivity Network (FCN):**
Using the FC matrix of each subject, we generated FCNs using a two-step filtering approach comprising maximum panning tree (MST) followed by sparsity-based thresholding. We constructed the 49 FCNs for each subject over a wide range of edge densities between 2 - 50% edges, with an increment 1% edges.
The subfolder [FCN](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA/FCN) contains the FCNs for each subject in weighted edgelist format. Each edgelist file can be uniquely identified by subject ID and edge density.
