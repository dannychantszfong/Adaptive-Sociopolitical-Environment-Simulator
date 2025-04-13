# Adaptive Sociopolitical Environment Simulator

A sophisticated simulation system that models and analyzes sociopolitical environments, focusing on policy impacts, population dynamics, and economic factors.

## Overview

This project simulates a sociopolitical environment with a focus on the United Kingdom, allowing for the analysis of various policies and their impacts on different population segments. The simulator incorporates complex interactions between policies, population demographics, and economic factors to provide insights into potential outcomes of policy decisions.

## Features

- **Population Simulation**: Generates and manages a detailed population model
- **Policy Analysis**: Evaluates the impact of various policies on different population segments
- **Economic Modeling**: Simulates economic factors and their interactions with policies
- **Data Extraction**: Processes and analyzes real-world data for simulation inputs
- **GUI Interface**: User-friendly interface for interacting with the simulation
- **Training System**: Machine learning components for policy optimization
- **Real-time Analysis**: Monitor policy impacts and population changes in real-time
- **Data Visualization**: Visual representations of simulation outcomes and trends

## Project Structure

- `config.py`: Core configuration settings and initialization
- `simulation.py`: Main simulation engine
- `policy.py`: Policy implementation and analysis
- `people_generation.py`: Population generation and management
- `data_extraction.py`: Data processing and analysis
- `training.py`: Machine learning components and model training
- `GUI.py`: User interface implementation
- `popularity.py`: Population sentiment and policy popularity tracking
- `data_dict.py`: Data structure definitions and mappings
- `policy_callout.py`: Policy event handling and triggers
- `simulation_config.py`: Simulation parameters and settings
- `training_data.py`: Training data management and processing

## Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 1GB free disk space

### Operating System-Specific Requirements

#### Windows
- Windows 10 or later
- Microsoft Visual C++ 14.0 or greater
```bash
# Install Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

#### macOS
- macOS 10.14 or later
- Xcode Command Line Tools
```bash
# Install Command Line Tools
xcode-select --install
```

#### Linux
- Any modern Linux distribution
- Required development packages:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-pip build-essential

# Fedora
sudo dnf install python3-devel python3-pip gcc
```

### Required Python Packages
See `requirements.txt` for specific version requirements:
```
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.2.0
tk>=8.6
python-dateutil>=2.8.2
hashlib>=20081119
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dannychantszfong/Adaptive-Sociopolitical-Environment-Simulator.git
cd Adaptive-Sociopolitical-Environment-Simulator
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Verify installation:
```bash
python -c "import numpy; import pandas; import sklearn"
```

## Usage

### GUI Interface
1. Launch the application:
```bash
python GUI.py
```

2. Configure simulation parameters:
   - Set population size and demographics
   - Define initial policy settings
   - Configure economic parameters
   - Set simulation duration

3. Run and monitor simulation:
   - Start the simulation
   - Monitor real-time updates
   - Analyze results through visualizations
   - Export data for further analysis

### Advanced Usage
- Custom policy creation through `policy.py`
- Population customization via `people_generation.py`
- Training model modifications in `training.py`

## Key Components

### Simulation Engine
The core simulation engine (`simulation.py`) handles the main simulation logic, including:
- Population dynamics
- Policy implementation
- Economic calculations
- Time progression
- Event handling
- State management

### Policy System
The policy system (`policy.py`) manages:
- Policy creation and modification
- Impact analysis
- Policy optimization
- Historical policy tracking
- Event triggers
- Policy interactions

### Population Management
The population system (`people_generation.py`) handles:
- Population generation
- Demographic distribution
- Individual characteristics
- Population evolution
- Sentiment tracking
- Behavioral modeling

## Development

### Setting Up Development Environment
1. Fork the repository
2. Create a new branch for your feature
3. Install development dependencies
4. Run tests before submitting PR

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owner of this repository before making a change.

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a Pull Request

## License

This project is licensed for personal and academic use only. Commercial use is not permitted. You are free to:
- Download and use the software
- Modify the code
- Share the software

Under the following conditions:
- You must give appropriate credit by including the original author's name (Danny Chan)
- You may not use this software for commercial purposes
- You must include this license notice in any copy or modification of the software

## Contact

- **Author**: Danny Chan
- **Email**: w1819419@my.westminster.ac.uk
- **LinkedIn**: [Tsz Fong Chan](https://www.linkedin.com/in/tsz-fong-chan-7201b7269/)
- **GitHub**: [@dannychantszfong](https://github.com/dannychantszfong)

## Acknowledgments

- University of Westminster
- This project was developed as part of a final year project
- Special thanks to all contributors and testers

## Future Development

### Planned Features
- Enhanced visualization capabilities
- Additional policy templates
- Advanced ML model integration
- API integration for real-world data
- Multi-region simulation support

### Known Issues
- Please check the Issues tab on GitHub for current known issues
- Report new issues through GitHub's issue tracker

## Citation

If you use this software in your research or project, please cite it as:

```
Chan, T.F. (2024). Adaptive Sociopolitical Environment Simulator. 
GitHub repository: https://github.com/dannychantszfong/Adaptive-Sociopolitical-Environment-Simulator
```

## Project Status

This project is actively maintained. For the latest updates and changes, please check the GitHub repository. 