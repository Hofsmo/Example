"""Module containing an example function."""
import scipy.signal as sig


def preprocess_data(signal, factor=5, detrend=True):
    """Function that preproccesses some data.

    This functions preproccesses a signal by detrending it
    and then applying a moving average filter.

    Args:
        signal: Input signal
        factor: Decimation factor
        detrend: Whether or not to detrend the signal

    Output:
        processed: The preprocessed signal
    """
    # Detrend the signal
    if detrend:
        signal = sig.detrend

    return sig.decimate(signal, factor)
