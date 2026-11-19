# Homework 3 data and checkpoints

The following inputs/checkpoints are referenced by the notebooks but are not included in this public-facing repository copy.

## Brain MRI registration
- BraTS 2020 training data with patient folders and modality files such as T1, T1ce, T2, and FLAIR NIfTI volumes.
- Follow the original dataset access terms and de-identification requirements.

## Optical–SAR registration
- OSdataset optical/SAR pairs, including the `opt*.png` and `sar*.png` files expected by the notebook.
- Update the original Kaggle-specific `DIR_PATH` to your local authorized dataset path.

## U-Net semantic segmentation
- Oxford-IIIT Pets is loaded through TensorFlow Datasets by the notebook; it is downloaded when the dataset-loading cell is run.

## SAM promptable segmentation
- `sam_vit_h_4b8939.pth` (SAM ViT-H checkpoint), which must be downloaded from the official Segment Anything release and stored at the path expected by the notebook.
- `dog.jpeg` for the prompt examples.
- Optional Roboflow MRI brain-tumor dataset and COCO annotations. The optional workflow may require a Roboflow API key. Store credentials in environment variables or a local secret manager; never commit them.

Before adding any dataset, verify its license, access restrictions, privacy status, and citation requirements.
