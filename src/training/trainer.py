import sys
sys.dont_write_bytecode = True

import logging
from omegaconf import DictConfig
from pathlib import Path
from typing import Optional, Dict, Any

class Trainer:
    def __init__(self, cfg: DictConfig, model: Any, data_module: Any):
        """Initialize the trainer
        
        Args:
            cfg: Training configuration
            model: Model instance
            data_module: Data module instance
        """
        self.cfg = cfg
        self.model = model
        self.data_module = data_module
        self.logger = logging.getLogger(__name__)
        
        # Create output directory for checkpoints
        self.output_dir = Path("outputs") / "checkpoints"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Log training configuration
        self.logger.info("Trainer initialization:")
        self.logger.info(f"Number of epochs: {self.cfg.training.num_epochs}")
        self.logger.info(f"Learning rate: {self.cfg.optimizer.lr}")
        self.logger.info(f"Batch size: {self.data_module.cfg.preprocessing.batch_size}")
        self.logger.info(f"Gradient accumulation steps: {self.cfg.training.gradient_accumulation_steps}")
    
    __str__ = lambda self: f"Trainer for {self.model.__class__.__name__}"
    
    def print_config(self):
        """Print the configuration of the trainer"""
        self.logger.info(f"Trainer configuration: {self.cfg.optimizer}")
    
    def train(self) -> float:
        """Training loop
        
        Returns:
            float: Final evaluation metric
        """
        try:
            self.logger.info("Starting training...")
            
            # Training loop
            for epoch in range(self.cfg.training.num_epochs):
                self.logger.info(f"Epoch {epoch+1}/{self.cfg.training.num_epochs}")
                
                # Dummy training step
                if epoch % self.cfg.training.eval_steps == 0:
                    self.logger.info(f"Running evaluation at epoch {epoch+1}")
                
                if epoch % self.cfg.training.save_steps == 0:
                    self.logger.info(f"Saving checkpoint at epoch {epoch+1}")
                    
            return 0.85  # Dummy metric
            
        except Exception as e:
            self.logger.error(f"Error during training: {str(e)}")
            self.logger.error(f"Configuration used: {self.cfg}")
            raise
            
    def evaluate(self) -> float:
        """Evaluation loop
        
        Returns:
            float: Evaluation metric
        """
        try:
            self.logger.info("Running evaluation...")
            return 0.83  # Dummy metric
            
        except Exception as e:
            self.logger.error(f"Error during evaluation: {str(e)}")
            raise

    def _log_metrics(self, metrics: Dict[str, float], step: int):
        """Log metrics during training
        
        Args:
            metrics: Dictionary of metric names and values
            step: Current training step
        """
        for name, value in metrics.items():
            self.logger.info(f"Step {step} - {name}: {value:.4f}")