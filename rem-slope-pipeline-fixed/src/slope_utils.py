import numpy as np
from scipy.signal import welch

def welch_psd(x, fs, nperseg=1024, noverlap=512, window='hann'):
    """Compute Welch PSD (power spectral density).
    Returns freqs (Hz) and PSD (power units).
    """
    f, pxx = welch(x, fs=fs, nperseg=nperseg, noverlap=noverlap, window=window, detrend='constant')
    return f, pxx

def synthetic_1overf(n, fs, beta=-2.0, rng=None):
    """Generate time series with 1/f^|beta| PSD using freq-domain shaping."""
    rng = np.random.default_rng(rng)
    white = rng.normal(size=n)
    X = np.fft.rfft(white)
    freqs = np.fft.rfftfreq(n, 1/fs)
    # avoid zero
    freqs[0] = freqs[1]
    X = X / (freqs**(abs(beta)/2.0))
    x = np.fft.irfft(X, n=n)
    return x / np.std(x)

def naive_aperiodic_slope(freqs, psd, fmin=1.0, fmax=40.0):
    """Estimate aperiodic slope via robust log-log linear regression.
    Returns slope (negative for 1/f^k) and intercept.
    """
    mask = (freqs >= fmin) & (freqs <= fmax)
    f = freqs[mask]
    p = psd[mask]
    x = np.log10(f)
    y = np.log10(p)
    # simple least squares; optionally add robust variants if needed
    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(slope), float(intercept)
