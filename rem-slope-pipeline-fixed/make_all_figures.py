import subprocess, sys
subprocess.check_call([sys.executable, 'scripts/example_psd.py'])
subprocess.check_call([sys.executable, 'scripts/param_sweeps.py'])
print('All figures/scripts done.')
