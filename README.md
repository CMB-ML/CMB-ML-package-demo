# CMB-ML as a Package

This repo serves as a testbed for the CBM-ML repository installed as a package. Of particular concern was the use of hydra configurations without conflict.

Note that nothing in this repository tells Hydra where to find configurations. All of that is set up when CMB-ML is installed with pip.

# Installation

To use CMB-ML in that way:
- Download the CMB-ML repository
    - `git clone git@github.com:CMB-ML/cmb-ml.git`
    - `cd cmb-ml`
    - `git switch whatever`
- Create the conda environment 
    - still required due to either namaster or torch... this could be fixed soon, possibly
    - `conda env create -f env.yaml`
    - To change the name of the environment, edit the file or use a different command.
- Activate the conda environment
    - `conda activate cmb-ml`
- Install CMB-ML
    - `which pip` (ensure that the response is within the conda environment)
    - `pip install .`

Then, for the test cases here:
- Download this to a separate location (don't mix it with the main CMB-ML repository)
- Run main_cmbml_cfg.py
    - Note that this is the same config as is used by CMB-ML's `main_sim.py`
- Run main_local_cfg.py
    - Take a look at the `cfg/config.yaml` being read from this repo
    - The `new_dir`: `test` line shows that new subfolders of the config dir work
    - The `local_system`: `generic_lab` line shows that config directories not found will be loaded from CMB-ML
    - The `splits`: `"1-1"` line shows that config YAMLs not found will be loaded from CMB-ML
    - The `file_system`: `common_fs` line shows that yaml files are preferentially loaded from here (this version is shorter)
    - The `a` and `b` parameters show that parameters themselves are loaded (trivially)
    - Note that no errors occur (hopefully!)