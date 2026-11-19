# Homework 3 — Registration and Segmentation

This homework contains four notebooks exploring medical-image registration and deep-learning-based segmentation, along with general computer-vision benchmarks used to study the same methods.

## 1. Multimodal 3D brain-MRI registration (BraTS 2020)

Notebook: `01-multimodal-3d-brain-mri-registration.ipynb`

- Explore a multimodal brain-MRI dataset.
- Load and visualize 3D NIfTI volumes.
- Implement an intensity-based registration function with SimpleITK.
- Apply known perturbations and resample moving images.
- Inspect alignment with checkerboard visualizations.
- Evaluate registration with a similarity metric and translation error.
- Batch-register selected patients and export registered volumes/slices.

**Main libraries:** SimpleITK, NiBabel, NumPy, Matplotlib.

## 2. Multimodal 2D optical–SAR registration

Notebook: `02-optical-sar-image-registration.ipynb`

- Explore paired optical and SAR images.
- Implement affine transforms.
- Generate synthetically misaligned SAR variants.
- Register images with mutual information.
- Implement feature-based registration using ORB and RANSAC.
- Compare results with checkerboards and corner error.

**Main libraries:** SimpleITK, OpenCV, Pillow, NumPy, Matplotlib.

## 3. Semantic segmentation with U-Net (Oxford-IIIT Pets)

Notebook: `03-unet-semantic-segmentation.ipynb`

- Load the Oxford-IIIT Pets dataset using TensorFlow Datasets.
- Build preprocessing and augmentation pipelines.
- Use a pretrained MobileNetV2 encoder.
- Connect a U-Net-style decoder with skip connections.
- Train a three-class segmentation model.
- Evaluate with pixel accuracy and mean IoU.

This is a general segmentation benchmark rather than a medical dataset.

**Main libraries:** TensorFlow, TensorFlow Datasets, TensorFlow Examples, NumPy, Matplotlib.

## 4. Promptable segmentation with Segment Anything Model

Notebook: `04-promptable-segmentation-sam.ipynb`

- Load the SAM ViT-H checkpoint.
- Generate masks automatically.
- Filter and visualize predicted masks.
- Perform box-prompted and point-prompted segmentation.
- Evaluate masks against ground-truth annotations using IoU.
- Includes an optional Roboflow brain-tumor dataset workflow.

The notebook also uses a dog image for introductory promptable-segmentation exercises; the optional tumor-dataset workflow is closer to the medical-imaging application.

**Main libraries:** PyTorch, Segment Anything, OpenCV, Pillow, SciPy, Supervision, Roboflow, and dataclasses-json.

## Data and model checkpoints

The uploaded archive contains the notebooks and a scanned theory-work PDF. The PDF is not included in this public-facing repository copy. Raw datasets, SAM weights, and local image files are not included. See `data/README.md` and the root `DATASETS.md`.

## Reproducibility status

The notebooks contain remaining TODO placeholders in multiple sections. The notebooks have not been re-executed as part of repository packaging. Install the correct environment, provide authorized data/checkpoints, and complete or verify the TODO cells before relying on the results.
