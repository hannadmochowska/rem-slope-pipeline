import numpy as np, matplotlib.pyplot as plt
from src.slope_utils import synthetic_1overf, welch_psd, naive_aperiodic_slope
try:
    from src.fooof_wrap import fooof_aperiodic_slope
    FOOOF_OK = True
except Exception:
    FOOOF_OK = False

FS = 200
N_SEC = 60
USE_FOOOF = False  # set True if you installed fooof

def main():
    x = synthetic_1overf(N_SEC*FS, FS, beta=-2.0, rng=42)
    f, p = welch_psd(x, FS, nperseg=1024, noverlap=512)
    slope_lin, b = naive_aperiodic_slope(f, p, fmin=1, fmax=40)
    print(f"Naive slope (log-log fit): {slope_lin:.3f}")
    if USE_FOOOF and FOOOF_OK:
        slope_fooof, fm = fooof_aperiodic_slope(f, p, fmin=1, fmax=40)
        print(f"FOOOF aperiodic slope: {slope_fooof:.3f}")
    plt.loglog(f, p)
    plt.xlabel('Frequency (Hz)'); plt.ylabel('PSD (a.u.)'); plt.title('Welch PSD (synthetic 1/f)')
    plt.show()

if __name__ == '__main__':
    main()
