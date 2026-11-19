# Homework 1 — Image Degradation, Restoration, and Object Analysis

This homework contains three practical notebooks covering classical image-processing workflows.

## 1. Image degradation and restoration

Notebook: `01-image-degradation-restoration.ipynb`

- Implement and apply five noise models.
- Examine test patterns and noise histograms.
- Simulate motion blur and low contrast.
- Apply denoising filters.
- Perform Wiener deconvolution for motion blur.
- Apply histogram equalization and CLAHE-based contrast enhancement.
- Evaluate restoration quality using PSNR and SSIM.

## 2. Creating region objects in Python

Notebook: `02-region-object-segmentation.ipynb`

- Load and inspect a noisy image.
- Remove high-frequency noise.
- Estimate the background and perform flat-field correction.
- Apply global/Otsu thresholding.
- Extract connected components and region statistics.
- Filter regions and construct a segmented result.

## 3. Round-object recognition

Notebook: `03-round-object-recognition.ipynb`

- Load and preprocess an image.
- Apply Otsu thresholding and morphological cleanup.
- Extract object contours.
- Compute a roundness descriptor.
- Classify candidate round objects and estimate their diameters.

## Main libraries

NumPy, Pandas, Matplotlib, OpenCV, SciPy, scikit-image, and pydicom.

## Data requirements

The uploaded archive contains the notebooks and a scanned theory-work PDF, but not the image/DICOM datasets referenced by the notebooks. The theory PDF is not included in this public-facing repository copy. See the assignment-level `data/README.md` and root `DATASETS.md` for expected input names and notes.
