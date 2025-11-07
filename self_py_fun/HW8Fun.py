# import the relevant packages
import numpy as np
import matplotlib.pyplot as plt

# produce_trun_mean_cov
def produce_trun_mean_cov(input_signal, input_type, E_val):
    r"""
    args:
    -----
        input_signal: 2d-array, (sample_size_len, feature_len)
        input_type: 1d-array, (sample_size_len,)
        E_val: integer, (number of electrodes)
    return:
    -----
        A list of 5 arrays including
            signal_tar_mean, (E_val, length_per_electrode)
            signal_ntar_mean, (E_val, length_per_electrode)
            signal_tar_cov, (E_val, length_per_electrode, length_per_electrode)
            signal_ntar_cov, (E_val, length_per_electrode, length_per_electrode)
            signal_all_cov, (E_val, length_per_electrode, length_per_electrode)
    note:
    -----
        descriptive mean and sample covariance statistics from real data
        In this case, E_val=16, length_per_electrode=25.
        But you should pass them as arguments or calculate them inside the function.
    """
    N, F = input_signal.shape # F = total features
    length_per_electrode = F // E_val
    x3 = input_signal.reshape(N, E_val, length_per_electrode)
    mask_tar = (input_type== 1)
    mask_notar = (input_type== -1)
    signal_tar_mean = x3[mask_tar].mean(axis=0)
    signal_notar_mean = x3[mask_notar].mean(axis=0)
    signal_tar_cov = []
    signal_notar_cov = []
    signal_all_cov = []
    for e in range(E_val):
        xe_tar = x3[mask_tar, e, :]
        xe_notar = x3[mask_notar, e, :]
        xe_all = x3[:, e, :]
        signal_tar_cov.append(np.cov(xe_tar, rowvar=False))
        signal_notar_cov.append(np.cov(xe_notar, rowvar=False))
        signal_all_cov.append(np.cov(xe_all, rowvar=False))
        print(signal_tar_mean.shape, signal_notar_mean.shape,
        len(signal_tar_cov), len(signal_notar_cov), len(signal_all_cov))
    return [signal_tar_mean, signal_notar_mean, signal_tar_cov, signal_notar_cov,signal_all_cov]

#p lot_trunc_mean
def plot_trunc_mean(
        eeg_tar_mean, eeg_ntar_mean, subject_name, time_index, E_val, electrode_name_ls,
        y_limit=np.array([-5, 8]), fig_size=(12, 12)
):
    r"""
    :param eeg_tar_mean:
    :param eeg_ntar_mean:
    :param subject_name:
    :param time_index:
    :param E_val:
    :param electrode_name_ls:
    :param y_limit: optional parameter, a list or an array of two numbers
    :param fig_size: optional parameter, a tuple of two numbers
    :return:
    """
    fig, axes = plt.subplots(4,4, figsize=fig_size)
    for i in range(len(electrode_name_ls)):
        plt.subplot(4,4,i+1)
        plt.plot(time_index, eeg_tar_mean[i], color="red", label = "Target")
        plt.plot(time_index, eeg_ntar_mean[i], color="blue", label = "Non-Target")
        plt.title(electrode_name_ls[i])
        plt.xlabel("Time (ms)")
        plt.ylabel("Amplitude (uV")
        plt.ylim(y_limit)
        plt.legend(loc="upper right", fontsize=8)
        plt.suptitle(f"Subject: {subject_name} - Target and Non-Target Sample Means", fontsize=14, fontweight="bold")
    return fig

# plot_trunc_cov
def plot_trunc_cov(
        eeg_cov, cov_type, time_index, subject_name, E_val, electrode_name_ls, fig_size=(14,12)
):
    """
    Parameters:
    eeg_cov : Covariance matrices for each electrode (shape: E_val × [n_timepoints × n_timepoints]).
    cov_type : str. Type of covariance ('Target', 'Non-Target', or 'All').
    time_index : Time values (in ms) for x and y axes.
    subject_name : str. Subject identifier for the figure title.
    E_val : int. Number of electrodes.
    electrode_name_ls : list of str. Names of electrodes.
    fig_size : tuple, optional. Figure size in inches, default (14, 12).
    """
    X, Y = np.meshgrid(time_index, time_index)
    fig, axes = plt.subplots(4, 4, figsize=fig_size)
    axes = axes.flatten()
    for i in range(E_val):
        plt.subplot(4,4,i+1)
        cs=plt.contourf(X, Y, eeg_cov[i], levels=50, cmap='RdBu_r')
        plt.title(electrode_name_ls[i])
        plt.xlabel("Time (ms)")
        plt.ylabel("Time (ms)")
        plt.gca().invert_yaxis()  # for time to increase top to bottom
    for j in range(E_val, len(axes)):
        plt.sca(axes[j])
        plt.axis("off")
    plt.suptitle(
        f"Subject: {subject_name} - {cov_type} Sample Covariance", y=1.02, fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig