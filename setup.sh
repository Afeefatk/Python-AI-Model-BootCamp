
#!/bin/zsh
set -e

# Create an isolated environment
python3 -m venv .venv

# Install your commonly used libraries
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install numpy pandas matplotlib scikit-learn seaborn

echo "Project setup complete!"
echo "Select .venv/bin/python in VS Code."


## Activate the virtual environment
# source .venv/bin/activate

