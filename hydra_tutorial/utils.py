from __future__ import annotations
import json
from hydra.core.hydra_config import HydraConfig
from pathlib import Path




def dump_logs(log_data: dict, filename: str):
    """Dump log dict in jsonl format

    This appends one json dict line to the filename.

    Parameters
    ----------
    log_data : dict
        Data to log, must be json serializable.
    filename : str
        Filename without path. The path will be either the
        current working directory or if it is called during
        a hydra session, the hydra run dir will be the log 
        dir.
    """
    log_data_str = json.dumps(log_data) + "\n"

    try:
        # Check if we are in a hydra context
        hydra_cfg = HydraConfig.instance().get()
        directory = hydra_cfg.run.dir
    except:
        directory = "."
    filename = Path(directory) / filename
    with open(filename, mode="a") as file:
        file.writelines([log_data_str])