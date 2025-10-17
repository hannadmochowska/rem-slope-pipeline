import numpy as np, matplotlib.pyplot as plt, os
from src.slope_utils import synthetic_1overf, welch_psd, naive_aperiodic_slope

FS = 200; SEC = 60
os.makedirs('outputs', exist_ok=True)

x = synthetic_1overf(SEC*FS, FS, beta=-2.0, rng=0)

# Sweep nperseg
segs = [256, 512, 1024, 2048]
vals = []
for nseg in segs:
    f, p = welch_psd(x, FS, nperseg=nseg, noverlap=nseg//2)
    sl, _ = naive_aperiodic_slope(f, p, 1, 40)
    vals.append(sl)
plt.figure()
plt.plot(segs, vals, marker='o')
plt.xlabel('nperseg'); plt.ylabel('Estimated slope'); plt.title('Slope vs nperseg')
plt.savefig('outputs/slope_vs_nperseg.png', dpi=200)

# Sweep frequency range
ranges = [(1,30),(1,40),(2,40),(5,40)]
vals = []
for fr in ranges:
    f, p = welch_psd(x, FS, nperseg=1024, noverlap=512)
    sl, _ = naive_aperiodic_slope(f, p, fr[0], fr[1])
    vals.append(sl)
plt.figure()
plt.plot([str(r) for r in ranges], vals, marker='o')
plt.xlabel('F-range (Hz)'); plt.ylabel('Estimated slope'); plt.title('Slope vs fit range')
plt.savefig('outputs/slope_vs_frange.png', dpi=200)

print('Saved figures in outputs/')
