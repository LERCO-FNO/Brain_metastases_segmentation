# Brain_metastases_segmentation

## Overview
Welcome to the repository for the paper **"Benchmarking Deep Segmentation Models for Brain Metastasis Detection and Delineation"**! This repository provides the code for the implementation of the networks for segmentation within the popular [nnUNet framework](https://github.com/MIC-DKFZ/nnUNet).

### Read the [paper](TO BE Updated): 

**Authors:** Michal Nohel<sup>1,2,*</sup>, Constantin Ulrich<sup>3,4</sup>, Yannick Kirchhoff<sup>3,5,6</sup>, Maximilian Rokuss<sup>3,5,6</sup>, Jiri Chmelik<sup>2</sup>, Stefan Reguli<sup>7</sup>, Lukas Knybel<sup>8</sup>

**Author Affiliations:**  
<sup>1</sup> Department of Deputy Director for Science and Research, University Hospital & Faculty of Medicine, Ostrava, Czech Republic  
<sup>2</sup> Department of Biomedical Engineering, Faculty of Electrical Engineering and Communication, Brno University of Technology, Brno, Czech Republic  
<sup>3</sup> German Cancer Research Center (DKFZ), Division of Medical Image Computing, Heidelberg, Germany  
<sup>4</sup> Medical Faculty Heidelberg, University of Heidelberg, Heidelberg, Germany  
<sup>5</sup> HIDSS4Health - Helmholtz Information and Data Science School for Health, Karlsruhe/Heidelberg, Germany  
<sup>6</sup> Faculty of Mathematics and Computer Science, Heidelberg University, Heidelberg, Germany  
<sup>7</sup> Department of Neurosurgery, University Hospital & Faculty of Medicine, Ostrava, Czech Republic  
<sup>8</sup> Department of Oncology, University Hospital & Faculty of Medicine, Ostrava, Czech Republic  
<sup>*</sup> Corresponding author: Michal Nohel (michal.nohel@fno.cz)

## Overview
This repository contains the code and pre-trained models accompanying the paper submitted to Computers in Biology and Medicine, titled **"Benchmarking Deep Segmentation Models for Brain Metastasis Detection and Delineation"**.  

This repository provides pretrained models, inference scripts, evaluation tools, and benchmark resources for automatic segmentation of brain metastases in contrast-enhanced T1-weighted MRI scans.

Our models are based on the [nnUNet framework](https://github.com/MIC-DKFZ/nnUNet).

---

## Trained Models / Zenodo

Pre-trained nnU-Net models for this project are available on Zenodo. These models were developed for automatic segmentation of brain metastases in contrast-enhanced T1-weighted MRI scans as part of the **BEAMSTER Benchmark** project.

- The models were trained and evaluated using the **BEAMSTER dataset**, a retrospective clinical MRI dataset comprising **140 patients** with **260 manually annotated brain metastases** acquired for stereotactic radiotherapy planning at University Hospital Ostrava.
- The dataset includes lesions of varying sizes, including a substantial proportion of **very small metastases**, allowing robust evaluation of lesion detection and segmentation performance.
- Multiple model architectures were trained within the **nnU-Net v2 framework**, including standard nnU-Net baselines, Residual Encoder U-Net variants, isotropic-resolution models, pretrained warm-start architectures, and a transformer-based hybrid segmentation model.
- All models operate on **contrast-enhanced T1-weighted MRI scans** in **NIfTI (.nii.gz)** format and are intended for **research and development purposes only**.
- The released package includes models trained using **five-fold cross-validation**, as well as selected models retrained on the full dataset when available.

**Links:**

- Zenodo repository with trained models: [BEAMSTER_nnUNet_models](ZENODO_MODEL_LINK)

A more detailed description of the trained models, preprocessing pipeline, inference usage, and benchmark results is provided in the accompanying Zenodo README file.


## Usage
### Installation

Check out the official [nnUNet installation instructions](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/installation_instructions.md)

nnU-Net needs to know where you intend to save raw data, preprocessed data and trained models. For this you need to set a few environment variables. Please follow the instructions [here](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/set_environment_variables.md)

Clone and install nnU-Net:

```bash
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .
```

After installation, the nnU-Net v2 commands (e.g., `nnUNetv2_predict_from_modelfolder`) will be available in your environment.

# Inference
For inference you can use the default [nnUNet inference functionalities](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/how_to_use_nnunet.md).

### Running Inference with Pre-trained Models

The pre-trained models are available on Zenodo (see the "Trained Models / Zenodo" section above). After downloading the models from Zenodo, you can run inference on your data using the following command:

```bash
nnUNetv2_predict_from_modelfolder -i INPUT_FOLDER -o OUTPUT_FOLDER -m MODEL_FOLDER
```

Where:
- `INPUT_FOLDER`: Path to the folder containing input NIfTI (.nii.gz) files (contrast-enhanced T1-weighted MRI scans)
- `OUTPUT_FOLDER`: Path to the folder where segmentation results will be saved
- `MODEL_FOLDER`: Path to the specific model folder (e.g., one of the fold directories or the full dataset model) from the downloaded Zenodo package


**Note:** Ensure that your input data is in NIfTI format and matches the preprocessing requirements of the models.

## Citation

If you use this work in your research, please cite:

[To be updated with the paper citation once published] 



















