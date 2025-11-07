# Import the relevant packages
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.io import loadmat

# Import functions from HW8Fun.py
from HW8Fun import produce_trun_mean_cov, plot_trunc_mean, plot_trunc_cov

# Create a new directory called K114 under my current working directory
cwd = Path.cwd()
new_dir = cwd / "K114"
new_dir.mkdir(exist_ok=True)

# Import data
eeg_trunc_obj = loadmat("/Users/madelyncarlson/Documents/GitHub/BIOS-584/data/K114_001_BCI_TRN_Truncated_Data_0.5_6.mat")
# print(eeg_trunc_obj.keys())

# Copying the global variables from HW7
bp_low = 0.5
bp_upp = 6
electrode_num = 16
electrode_name_ls = ['F3', 'Fz', 'F4', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP3', 'CP4', 'P3', 'Pz', 'P4', 'PO7', 'PO8', 'Oz']
time_index = np.linspace(0, 800, 25) # This is a hypothetic time range up to 800 ms after each stimulus.
subject_name = 'K114'
session_name = '001_BCI_TRN'
eeg_trunc_signal = eeg_trunc_obj['Signal']
eeg_trunc_type = eeg_trunc_obj['Type']
print("eeg_trunc_signal:", eeg_trunc_signal.shape)
eeg_trunc_type = np.squeeze(eeg_trunc_type, axis=1)
print("eeg_trunc_type shape (after squeeze):", eeg_trunc_type.shape)

signal_tar_mean, signal_notar_mean, signal_tar_cov, signal_notar_cov, signal_all_cov = produce_trun_mean_cov(
    input_signal=eeg_trunc_signal,
    input_type=eeg_trunc_type,
    E_val=electrode_num
)

# Mean function & save it to K114 folder
fig = plot_trunc_mean(signal_tar_mean, signal_notar_mean, subject_name, time_index, electrode_num, electrode_name_ls)
fig.savefig(new_dir / "Mean.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Covariance Target
fig_cov_target = plot_trunc_cov(
    eeg_cov=signal_tar_cov,
    cov_type="Target",
    time_index=time_index,
    subject_name=subject_name,
    E_val=electrode_num,
    electrode_name_ls=electrode_name_ls,
    fig_size=(14, 12)
)
fig_cov_target.savefig(new_dir / "Covariance_Target.png", dpi=300, bbox_inches="tight")
plt.close(fig_cov_target)

# Covariance Non-Target
fig_cov_nontarget = plot_trunc_cov(eeg_cov=signal_notar_cov, cov_type="Non-Target", time_index=time_index, subject_name=subject_name, E_val=electrode_num, electrode_name_ls=electrode_name_ls, fig_size=(14, 12))
fig_cov_nontarget.savefig(new_dir / "Covariance_Non-Target.png", dpi=300, bbox_inches="tight")
plt.close(fig_cov_nontarget)

# Covariance All
fig_cov_all = plot_trunc_cov(
    eeg_cov=signal_all_cov,
    cov_type="All",
    time_index=time_index,
    subject_name=subject_name,
    E_val=electrode_num,
    electrode_name_ls=electrode_name_ls,
    fig_size=(14, 12)
)
fig_cov_all.savefig(new_dir / "Covariance_All.png", dpi=300, bbox_inches="tight")
plt.close(fig_cov_all)