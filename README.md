# Medical Image Analysis and Processing

A curated collection of coursework notebooks and practical implementations for **Medical Image Analysis and Processing**.

The repository covers image degradation and restoration, segmentation and object recognition, inverse problems, plug-and-play (PnP) reconstruction, wavelet-based image processing, multimodal registration, and deep-learning-based segmentation.

The material is organized by the three uploaded homework sets. Some assignments use general computer-vision benchmarks (for example, Oxford-IIIT Pets and optical/SAR imagery) to study methods that are also relevant to medical imaging.

## Coursework overview

| Homework | Main focus | Topics and methods |
|---|---|---|
| [01 — Image Degradation & Restoration](assignments/01-image-degradation-and-restoration/) | Classical image processing and object analysis | Noise models, blur, denoising, Wiener deconvolution, contrast enhancement, region properties, connected components, Otsu thresholding, morphology, roundness descriptors |
| [02 — Inverse Problems, PnP & Wavelets](assignments/02-inverse-problems-pnp-and-wavelets/) | Image reconstruction with classical and learned priors | Forward models, inverse problems, ADMM, plug-and-play denoisers, BM3D, NLM, TV denoising, DnCNN, zero-curl condition, MACE/consensus equilibrium, wavelet decomposition and hybrid images |
| [03 — Registration & Segmentation](assignments/03-registration-and-segmentation/) | Registration and semantic/promptable segmentation | 3D multimodal brain-MRI registration (BraTS 2020), optical–SAR registration, mutual information, ORB + RANSAC, U-Net with MobileNetV2, Oxford-IIIT Pets, Segment Anything Model (SAM), IoU |

## Detailed contents

### Homework 1 — Image degradation, restoration, and object analysis

Three notebooks:

1. **Image degradation and restoration**
   - Five noise models and noise histograms.
   - Motion blur and low-contrast degradation.
   - Denoising filters and Wiener deconvolution.
   - Contrast enhancement and quantitative evaluation with PSNR/SSIM.

2. **Creating region objects in Python**
   - Noise reduction and background estimation.
   - Flat-field correction.
   - Otsu thresholding and connected components.
   - Region statistics, filtering, and segmented output visualization.

3. **Round-object recognition**
   - Image thresholding and morphological cleanup.
   - Contour extraction.
   - Roundness descriptors and per-object diameter estimation.

### Homework 2 — Plug-and-Play inverse problems and wavelet processing

- Forward models and inverse problems.
- Proximal maps and plug-and-play priors.
- ADMM splitting and FFT-based updates.
- Classical and learned denoisers, including Non-Local Means, BM3D, and a small DnCNN example.
- Training a denoiser on patches.
- Zero-curl condition and stacked operators.
- MACE / consensus equilibrium and fixed-point interpretation.
- Wavelet-domain image decomposition and hybrid-image construction.

The archive also contains `hybrid_images_wavelet.py`, a script that aligns two images and combines low-frequency information from one with high-frequency detail from the other using a level-4 `db4` wavelet decomposition.

### Homework 3 — Registration and segmentation

Four notebooks:

1. **Multimodal 3D brain-MRI registration (BraTS 2020)**
   - NIfTI volume loading and visualization.
   - SimpleITK registration.
   - Resampling, checkerboard visualization, and mutual-information evaluation.
   - Batch registration and PNG export.

2. **Multimodal 2D optical–SAR registration**
   - Affine transforms and synthetic misalignment.
   - Mutual-information-based registration.
   - ORB feature matching with RANSAC.
   - Checkerboard and corner-error evaluation.

3. **Semantic segmentation with U-Net (Oxford-IIIT Pets)**
   - TensorFlow Datasets input pipeline.
   - Image/mask preprocessing and augmentation.
   - MobileNetV2 encoder and U-Net-style decoder.
   - Training and mean-IoU evaluation.

4. **Promptable segmentation with Segment Anything Model (SAM)**
   - Automatic mask generation.
   - Box- and point-prompted segmentation.
   - Mask filtering and visualization.
   - IoU evaluation against labeled masks, including an optional Roboflow brain-tumor dataset workflow.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── requirements/
│   ├── base.txt
│   ├── homework-01.txt
│   ├── homework-02.txt
│   ├── hw3-brain-mri-registration.txt
│   ├── hw3-optical-sar-registration.txt
│   ├── hw3-unet.txt
│   └── hw3-sam.txt
├── .gitignore
├── DATASETS.md
├── SHARING_AND_ACADEMIC_INTEGRITY.md
├── PACKAGING_NOTES.md
└── assignments/
    ├── 01-image-degradation-and-restoration/
    ├── 02-inverse-problems-pnp-and-wavelets/
    └── 03-registration-and-segmentation/
```
