# Homework 2 — Plug-and-Play Inverse Problems and Wavelet Processing

Notebook: `plug-and-play-inverse-problems.ipynb`

This practical notebook studies image reconstruction as an inverse problem and explores plug-and-play priors.

## Topics in the notebook

- Forward models, degradation operators, and inverse problems.
- Proximal maps and the plug-and-play idea.
- ADMM splitting and FFT-based solution of the image update.
- Classical denoisers, including Non-Local Means, BM3D, and total-variation denoising.
- A small DnCNN denoiser and patch-based training.
- The zero-curl condition.
- Composition of multiple denoising/contrast operators.
- MACE-style consensus equilibrium and fixed-point interpretation.
- The role of priors and the risk of hallucinated image details.

The archive also includes `hybrid_images_wavelet.py`, which:
- Aligns a near/far image pair with an affine transform.
- Performs a multilevel `db4` wavelet decomposition.
- Combines low-frequency content from one image with high-frequency details from the other.
- Writes a hybrid image and low-/high-frequency visualization outputs.

## Main libraries

NumPy, Matplotlib, SciPy, OpenCV, PyWavelets, scikit-image, BM3D, and PyTorch.

## External files and checkpoints

The notebook references `tiny_dncnn_demo.pth`. That checkpoint is not included in this public repository copy because its provenance and redistribution permission were not established.

The wavelet script expects `wavelet-near.png` and `wavelet-far.png` in its working directory. These image files and the generated hybrid result are not included because they contain face imagery. Add them only if you have permission and consent to publish them.

## Run

```bash
pip install -r ../../requirements/homework-02.txt
jupyter lab
```

The original notebook contains remaining TODO sections. Review and complete them as appropriate before treating the workflow as a fully reproducible implementation.
