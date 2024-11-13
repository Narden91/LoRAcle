from pathlib import Path
import logging
from omegaconf import DictConfig
import boto3
from typing import Optional, Dict, Any

class DataModule:
    def __init__(self, cfg: DictConfig):
        self.cfg = cfg
        self.logger = logging.getLogger(__name__)
        
        # Initialize storage based on configuration
        storage_type = cfg.storage.type
        if storage_type == "s3":
            self.storage = S3Storage(cfg.storage.s3)
        elif storage_type == "local":
            self.storage = LocalStorage(cfg.storage.local)
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
        
        self.logger.info(f"Initialized DataModule with storage type: {storage_type}")
        
    def setup(self) -> Dict[str, Any]:
        """Load and prepare the dataset"""
        self.logger.info(f"Loading dataset: {self.cfg.dataset.name}")
        # Dummy dataset loading
        return {
            "train": ["dummy_data"],
            "validation": ["dummy_data"]
        }

class LocalStorage:
    def __init__(self, cfg: DictConfig):
        self.data_dir = Path(cfg.data_dir)
        self.cache_dir = Path(cfg.cache_dir)
        
        # Create directories if they don't exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def load_file(self, path: str) -> Optional[str]:
        full_path = self.data_dir / path
        return full_path.read_text() if full_path.exists() else None

class S3Storage:
    def __init__(self, cfg: DictConfig):
        self.cfg = cfg
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=cfg.access_key,
            aws_secret_access_key=cfg.secret_key,
            region_name=cfg.aws_region
        )
    
    def load_file(self, path: str) -> Optional[str]:
        try:
            response = self.s3_client.get_object(
                Bucket=self.cfg.bucket_name,
                Key=path
            )
            return response['Body'].read().decode('utf-8')
        except Exception as e:
            logging.error(f"Error loading from S3: {e}")
            return None