# LoRAcle 🚀

A flexible and efficient implementation for fine-tuning Small Language Models using LoRA/QLoRA techniques.

## Project Structure 📁
```
LoRAcle/
├── configs/                    # Hydra configuration files
│   ├── config.yaml            # Main config
│   ├── data/                  # Dataset configs
│   │   └── default.yaml
│   ├── model/                 # Model configs
│   │   └── default.yaml
│   └── training/              # Training configs
│       └── default.yaml
├── src/
│   ├── data/                  # Data loading
│   │   └── data_module.py
│   ├── models/                # Model definitions
│   │   └── model_loader.py
│   └── training/              # Training logic
│       └── trainer.py
├── main.py                    # Entry point
└── README.md
```

## Quick Start 🚀

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/LoRAcle.git
cd LoRAcle

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```bash
# Run training with default configuration
python main.py

# Run evaluation
python main.py mode=eval
```

### Tests 
```bash
pytest tests/test_x.py
```


### Parameter Override Examples 🔧

Hydra allows flexible parameter override from command line. Here are some examples:

1. Modify training parameters:
```bash
python main.py \
    training.training.num_epochs=5 \
    training.optimizer.lr=1e-4 \
    training.training.gradient_accumulation_steps=4
```

2. Change model and hardware setup:
```bash
python main.py \
    model.base_model.name=TinyLlama-1.1B-Chat-v1.0 \
    model.base_model.device=cuda \
    model.quantization.bits=4
```

## Configuration ⚙️

The project uses Hydra for configuration management. Key configuration files:

- `configs/config.yaml`: Main configuration
- `configs/model/default.yaml`: Model settings
- `configs/data/default.yaml`: Dataset settings
- `configs/training/default.yaml`: Training parameters

Check the individual config files for all available options.

## License 📄
MIT

## Citation 📚
If you use this code in your research, please cite:
```bibtex
@software{loracle2024,
  author = {},
  title = {LoRAcle: },
  year = {2024},
  url = {}
}
```