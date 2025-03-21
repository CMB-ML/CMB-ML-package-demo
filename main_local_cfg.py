import logging
import hydra
from omegaconf import OmegaConf


logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="cfg", config_name="config")
def run_it(cfg):
    logger.debug(f"Running {__name__} in {__file__}")

    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    run_it()
