# Optional FOOOF wrapper (safe import). If FOOOF is not installed, functions raise a clear error.
def _import_fooof():
    try:
        from fooof import FOOOF
        return FOOOF
    except Exception as e:
        raise ImportError("FOOOF not installed. Run `pip install fooof` or set USE_FOOOF=False.") from e

def fooof_aperiodic_slope(freqs, psd, fmin=1.0, fmax=40.0, peak_width_limits=(1, 8), max_n_peaks=6, aperiodic_mode='fixed'):
    FOOOF = _import_fooof()
    fm = FOOOF(peak_width_limits=peak_width_limits, max_n_peaks=max_n_peaks, aperiodic_mode=aperiodic_mode, verbose=False)
    # FOOOF expects linear freqs & linear power; it works internally in log space
    mask = (freqs >= fmin) & (freqs <= fmax)
    fm.fit(freqs[mask], psd[mask])
    # aperiodic_params_ = [offset, slope] or [offset, knee, slope] if 'knee'
    params = fm.aperiodic_params_
    slope = float(params[-1])
    return slope, fm
