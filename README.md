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

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/medical-image-analysis-and-processing.git
cd medical-image-analysis-and-processing
```

Replace `<YOUR_GITHUB_USERNAME>` with your GitHub username.

### 2. Create a Python environment

Python 3.10 or 3.11 is a practical starting point, but deep-learning packages may require version adjustments depending on your operating system and GPU.

**Windows**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies for the assignment you want to run

Start with the common tools:

```bash
python -m pip install --upgrade pip
pip install -r requirements/base.txt
```

Then install the relevant assignment requirements. For example:

```bash
pip install -r requirements/homework-01.txt
```

For Homework 3, choose the requirements file matching the notebook. TensorFlow and PyTorch/SAM have different installation constraints, so separate environments may be easier than installing every dependency together.

### 4. Open the notebook

```bash
jupyter lab
```

Read the README in the relevant assignment folder and `DATASETS.md` before running cells. Several original datasets and model checkpoints are not included.

## Important reproducibility notes

- The notebooks are preserved as coursework, but their code-cell outputs and execution counts have been cleared in this public-facing copy.
- The supplied notebooks contain remaining `TODO` placeholders in multiple sections. This repository documents the uploaded state; it does not imply that every exercise is fully implemented or that all notebooks have been rerun.
- Input datasets, DICOM/NIfTI files, external checkpoints, and face-image assets have not been bundled. See `DATASETS.md`.
- The SAM notebook requires a separate checkpoint and may require Roboflow credentials for the optional dataset workflow. Never commit API keys or access tokens.
- GPU acceleration may be helpful for DnCNN, U-Net, and SAM workflows.

## Academic integrity and licensing

This is a personal coursework portfolio, not an official course repository. Course handouts, assignment prompts, starter code, datasets, and pretrained weights may have separate sharing and licensing restrictions. Check the course policy and original terms before publishing or adding excluded files. See [SHARING_AND_ACADEMIC_INTEGRITY.md](SHARING_AND_ACADEMIC_INTEGRITY.md).

---

**Topics:** Medical Image Processing · Image Restoration · Inverse Problems · Plug-and-Play Priors · Wavelets · Medical Image Registration · Image Segmentation · Deep Learning
