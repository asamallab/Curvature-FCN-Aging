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

![network example](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/summary-figure.png)

# Repository Organization

The repository is organized into two folders, [CODE](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/CODE) and [DATA](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA). A description of the files contained in each folder is provided below.

## DATA

1. **List of included subjects:**
A list of the 225 subjects from the MPI-LEMON dataset included in our work is provided in the file [cohort_information.tsv](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/DATA/cohort_information.tsv). The file contains information on the ID, age, sex and cohort of the included subjects.

2. **Functional Connectivity (FC) Matrix:**
The preprocessed fMRI scan of each subject was parcellated into 200 regions of interest (ROIs) or nodes defined according to the [Schafer atlas](https://doi.org/10.1093/cercor/bhx179 "Local-Global Parcellation of the Human Cerebral Cortex from Intrinsic Functional Connectivity MRI"), and a 200 × 200 functional connectivity matrix was generated for each subject by computing the Pearson correlation coefficient between the time-series of all pairs of ROIs. The subfolder [FCM](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA/FCM) contains the FC matrix for each subject in weighted edgelist format. Each edgelist file can be uniquely identifed by subject ID.

3. **Functional Connectivity Network (FCN):**
Using the FC matrix of each subject, we generated FCNs using a two-step filtering approach comprising maximum spanning tree (MST) followed by sparsity-based thresholding. We constructed the 49 FCNs for each subject over a wide range of edge densities between 2 - 50% edges, with an increment of 1% edges.
The subfolder [FCN](https://github.com/asamallab/Curvature-FCN-Aging/tree/main/DATA/FCN) contains the FCNs for each subject in weighted edgelist format. Each edgelist file can be uniquely identified by subject ID and edge density.

4. **Supplementary Tables**
An Excel workbook, [ST_RicciAging.xlsx](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/DATA/ST_RicciAging.xlsx), containing all the Supplementary Tables S1-S7 for our paper is available for download.

## CODE

1. **[generate_fcn.py](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/generate_fcn.py):**
Python script to generate the FCN at the desired edge density.

2. **[FormanTriangleUndirected.cpp](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/FormanTriangleUndirected.cpp):** : C++ script to compute the FRC for all the edges and nodes in an undirected network. The edges of the network can be weighted or binary.

3. **[OR-UnDir.py](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/OR-UnDir.py):** Python script to compute the ORC for all the edges and nodes in an undirected network. The edges of the network can be weighted or binary.

4. **[example_fcm.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_fcm.txt):** An example FC matrix file which is the input to _generate_fcn.py_ .

5. **[example_fcn.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_fcn.txt):** An example FCN file which is the output to _generate_fcn.py_ . This file is also the input to _FormanTriangleUndirected.cpp_ and _OR-UnDir.py_ .

6. **[example_nodefile.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_nodefile.txt):** An example nodelist file which is the input to _FormanTriangleUndirected.cpp_ and _OR-UnDir.py_ .

7. **[example_frc_edge.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_frc_edge.txt):** An example edgelist file containing the values of FRC of the edges in the example FCN. This file is output to _FormanTriangleUndirected.cpp_ .

8. **[example_frc_node.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_frc_node.txt):** An example nodelist file containing the values of FRC of the nodes in the example FCN. This file is output to _FormanTriangleUndirected.cpp_ .

9. **[example_orc_edge.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_orc_edge.txt):** An example edgelist file containing the values of ORC of the edges in the example FCN. This file is output to _OR-UnDir.py_ .

10. **[example_orc_node.txt](https://github.com/asamallab/Curvature-FCN-Aging/blob/main/CODE/example_orc_node.txt):** An example nodelist file containing the values of ORC of the nodes in the example FCN. This file is output to _OR-UnDir.py_ .

An example of the commands that can be used to compute the disrete Ricci curvatures are provided below.

_**FormanTriangleUndirected.cpp**_: 

```
./FormanTriangleUndirected 0 example_nodefile.txt 0 example_fcn.txt example_frc_edge.txt example_frc_node.txt
```

_**OR-Undir.py**_: 

```
python3 OR-UnDir.py 0 example_fcn.txt example_orc_edge.txt example_orc_node.txt
```

**Requirements**
The Python packages required are _NetworkX_, _cvxpy_, _Numpy._

## References

Please cite the below papers if you use the codes in this repository for your work.

* Y. Yadav, P. Elumalai, N. Williams, J. Jost, A. Samal, Discrete Ricci curvatures capture age-related changes in human brain functional connectivity networks bioRxiv (2022)
* P. Elumalai, Y. Yadav, N. Williams, E. Saucan, J. Jost & A.Samal, [Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder](https://www.nature.com/articles/s41598-022-12171-y#citeas),  Scientific Reports 12: 8295 (2022)
* A. Samal, R.P. Sreejith, J. Gu, S. Liu, E. Saucan & J. Jost, [Comparative analysis of two discretizations of Ricci curvature for complex networks](https://www.nature.com/articles/s41598-018-27001-3), Scientific Reports 8: 8650 (2018).
* R.P. Sreejith, K. Mohanraj, J. Jost, E. Saucan & A. Samal, [Forman curvature for complex networks](https://iopscience.iop.org/article/10.1088/1742-5468/2016/06/063206), Journal of Statistical Mechanics: Theory and Experiment 063206 (2016).
