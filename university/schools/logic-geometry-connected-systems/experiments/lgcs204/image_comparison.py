"""LGCS-204 local-only visual comparison; never writes to original files.

Requires Pillow and NumPy. Output is a measurement of two raster images,
not a proof of node locations, geometric symmetry, or physics.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from PIL import Image

REGIONS = {
    "upper_left_panel": [70,25,430,270],
    "upper_right_panel": [1000,20,1350,275],
    "lower_left_panel": [75,450,440,720],
    "lower_right_panel": [980,470,1350,720],
    "central_mandala": [380,5,1030,700],
    "outer_background": [0,0,100,120],
}

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
    return h.hexdigest()

def compare(before,after,heatmap=None):
    before=Path(before);after=Path(after)
    bh=sha256(before);ah=sha256(after)
    with Image.open(before) as img0, Image.open(after) as img1:
        dimensions=(img0.size,img1.size)
        rgb0=np.asarray(img0.convert('RGB'),dtype=np.int16)
        rgb1=np.asarray(img1.convert('RGB'),dtype=np.int16)
    if rgb0.shape!=rgb1.shape:
        raise ValueError('Images must have identical dimensions for pixelwise comparison')
    diff=np.abs(rgb0-rgb1)
    diff_px=diff.mean(axis=2)
    squared=(rgb0.astype(np.float64)-rgb1.astype(np.float64))**2
    rmse=np.sqrt(squared.mean())
    results={
        'before':{'sha256':bh,'bytes':before.stat().st_size,'dimensions':dimensions[0]},
        'after':{'sha256':ah,'bytes':after.stat().st_size,'dimensions':dimensions[1]},
        'same_original_bytes':bh==ah,
        'mean_abs_channel_difference':round(float(diff.mean()),6),
        'rmse_channels':round(float(rmse),6),
        'psnr_db':round(float(20*np.log10(255/rmse)),6) if rmse else None,
        'fraction_identical_rgb_pixels':round(float(np.all(rgb0==rgb1,axis=2).mean()),9),
        'fraction_pixels_mean_abs_difference_gt_24':round(float((diff_px>24).mean()),9),
        'regions':{},
        'interpretation_limit':'Pixel differences do not prove any particular graph, symmetry, physical law, or intent.'
    }
    for name,(x1,y1,x2,y2) in REGIONS.items():
        s=diff_px[y1:y2,x1:x2]
        results['regions'][name]={
            'rectangle_xyxy':[x1,y1,x2,y2],
            'mean_abs_channel_difference':round(float(s.mean()),6),
            'fraction_pixel_mean_difference_gt_24':round(float((s>24).mean()),9),
        }
    if heatmap:
        Image.fromarray(np.uint8(np.clip(diff_px*4,0,255)),mode='L').save(heatmap)
    return results

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--before',required=True)
    p.add_argument('--after',required=True)
    p.add_argument('--json-out',required=True)
    p.add_argument('--heatmap-out')
    a=p.parse_args()
    res=compare(a.before,a.after,a.heatmap_out)
    Path(a.json_out).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(res,indent=2))
