import sys
import hydra
from omegaconf import DictConfig, OmegaConf
import logging
from pathlib import Path
from typing import Optional

from src.training.trainer import Trainer
from src.data.data_module import DataModule
from src.models.model_loader import ModelLoader

sys.dont_write_bytecode = True

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig) -> Optional[float]:
    """Main entry point
    Args:
        cfg: Hydra configuration
    """
    # print("\nLoaded Configuration:")
    # print(OmegaConf.to_yaml(cfg))

    logging.basicConfig(level=logging.INFO)
    
    # Initialize components
    data_module = DataModule(cfg.data)
    model = ModelLoader(cfg.model)
    trainer = Trainer(cfg.training, model, data_module)
   
    # Train/evaluate based on mode
    if cfg.mode == "train":
        return trainer.train()
    elif cfg.mode == "eval":
        return trainer.evaluate()
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")

if __name__ == "__main__":
    main()