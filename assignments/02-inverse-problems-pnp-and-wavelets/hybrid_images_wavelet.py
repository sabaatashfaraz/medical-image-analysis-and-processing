import cv2
import numpy as np
import pywt

def align_images(near_img, far_img, pts_near, pts_far):
    matrix = cv2.getAffineTransform(pts_far, pts_near)
    rows, cols = near_img.shape[:2]
    
    aligned_far_img = cv2.warpAffine(
        far_img, 
        matrix, 
        (cols, rows), 
        borderMode=cv2.BORDER_CONSTANT, 
        borderValue=(255, 255, 255)
    )
    
    return aligned_far_img

def process_channel_dwt(near_ch, far_ch, wavelet='db4', level=4):
    # Decomposing down to Level 4 to strip out sharp structural outlines
    coeffs_near = pywt.wavedec2(near_ch, wavelet, level=level)
    coeffs_far = pywt.wavedec2(far_ch, wavelet, level=level)
    
    LL_near, details_near = coeffs_near[0], coeffs_near[1:]
    LL_far, details_far = coeffs_far[0], coeffs_far[1:]
    
    # Far's Low Frequencies (LL) + Near's High Frequencies (details)
    hybrid_coeffs = [LL_far] + details_near
    hybrid_ch = pywt.waverec2(hybrid_coeffs, wavelet)
    
    # High-Pass 
    zero_LL = np.zeros_like(LL_near)
    near_dwt_ch = pywt.waverec2([zero_LL] + details_near, wavelet)
    
    # Low-Pass
    zero_details = [tuple(np.zeros_like(d) for d in level_details) for level_details in details_far]
    far_dwt_ch = pywt.waverec2([LL_far] + zero_details, wavelet)
    
    return hybrid_ch, near_dwt_ch, far_dwt_ch

def create_hybrid():

    near_img = cv2.imread('wavelet-near.png')
    far_img = cv2.imread('wavelet-far.png')
    
    pts_near = np.float32([
        [353, 502], #left eye
        [571, 502], #right eye
        [459, 757], #mouth
    ])
    
    pts_far = np.float32([
        [342, 499], #left eye
        [560, 490], #right eye
        [467, 746], #mouth
    ])
    
    aligned_far = align_images(near_img, far_img, pts_near, pts_far)
    
    near_channels = cv2.split(near_img)
    far_channels = cv2.split(aligned_far)
    
    hybrid_channels = []
    near_dwt_channels = []
    far_dwt_channels = []
    
    for nc, fc in zip(near_channels, far_channels):
        h_ch, n_dwt_ch, f_dwt_ch = process_channel_dwt(
            nc, fc, 
            wavelet='db4', 
            level=4
        )
        
        hybrid_channels.append(h_ch)
        near_dwt_channels.append(n_dwt_ch)
        far_dwt_channels.append(f_dwt_ch)
        
    hybrid_img = cv2.merge(hybrid_channels)
    near_dwt_img = cv2.merge(near_dwt_channels)
    far_dwt_img = cv2.merge(far_dwt_channels)
    
    def normalize_img(img):
        return np.clip(img, 0, 255).astype(np.uint8)

    hybrid_result = normalize_img(hybrid_img)
    far_dwt_result = normalize_img(far_dwt_img)
    near_dwt_result = normalize_img(near_dwt_img + 128) 
    
    cv2.imwrite('wavelet-near-dwt.jpg', near_dwt_result)
    cv2.imwrite('wavelet-far-dwt.jpg', far_dwt_result)
    cv2.imwrite('hybrid-result.jpg', hybrid_result)
    
if __name__ == "__main__":
    create_hybrid()