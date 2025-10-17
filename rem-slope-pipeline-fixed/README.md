# Aperiodic Spectral Slope Pipeline (REM) — Fixed Starter

A clean, reproducible pipeline for estimating the aperiodic (1/f) slope in REM sleep.
It provides:
- Welch PSD computation
- Aperiodic slope via robust log–log linear fit (no external deps)
- Optional FOOOF integration (if installed) to separate periodic peaks
- Synthetic 1/f validation + parameter sweeps
- One-command figure reproduction

## Quick start (synthetic demo)
```bash
python scripts/example_psd.py              # shows PSD and prints slope
python scripts/param_sweeps.py             # produces sweep plots in outputs/
python make_all_figures.py                 # runs all demos
```

## Optional: FOOOF support
Install `fooof` (`pip install fooof`) and set `USE_FOOOF=True` in `scripts/example_psd.py` to get the aperiodic slope from FOOOF.
The pipeline will fall back to the robust linear estimator if FOOOF is not available.

## Project layout
```
src/
  slope_utils.py        # Welch PSD, synthetic 1/f, naive slope estimate
  fooof_wrap.py         # Optional FOOOF helpers (safe import)
scripts/
  example_psd.py        # single-run PSD + slope
  param_sweeps.py       # vary nperseg, f-range; save figures
notebooks/
  01_demo_placeholder.ipynb  # your future analysis notebook (placeholder)
outputs/                # created at runtime for figures
data/                   # put small EEG/LFP samples here (optional)
make_all_figures.py     # runs all scripts and saves outputs
requirements.txt
README.md
```

## Notes
- For real EEG/LFP, pre-clean segments (artifact removal) before slope estimation.
- Always report parameters used (fs, nperseg, overlap, fmin/fmax).
