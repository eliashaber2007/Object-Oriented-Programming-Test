#!/usr/bin/env bash
# env_install.sh: sets up a Python + Jupyter development environment on macOS or Linux.
# Usage: ./env_install.sh

# Stop on errors, on unset variables, and on failed commands inside pipes,
# so a broken step never silently continues.
set -euo pipefail

# Colors make success, warnings and errors easy to spot in the output
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
RESET="\033[0m"

# Feature 1: pretty printing with blank lines around each message
pretty_print() {
    printf "\n%b\n\n" "$1"
}

success() { pretty_print "${GREEN}$1${RESET}"; }
warning() { pretty_print "${YELLOW}$1${RESET}"; }
error()   { pretty_print "${RED}$1${RESET}"; }

# Feature 2: detect the operating system so we use the right package manager
detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    else
        error "Unsupported operating system: $OSTYPE"
        exit 1
    fi
    success "Detected operating system: $OS"
}

# Feature 3: install python3 only if it is missing
check_python() {
    if command -v python3 > /dev/null 2>&1; then
        success "Python is installed: $(python3 --version)"
    else
        warning "Python 3 not found, installing it..."
        if [[ "$OS" == "macos" ]]; then
            brew install python
        else
            sudo apt-get update && sudo apt-get install -y python3 python3-pip
        fi
        success "Python installed: $(python3 --version)"
    fi
}

# Feature 4: pip is needed to install Python packages like Jupyter
check_pip() {
    if python3 -m pip --version > /dev/null 2>&1; then
        success "pip is available: $(python3 -m pip --version)"
    else
        error "pip is missing. Install it before continuing."
        exit 1
    fi
}

# Feature 5: install Jupyter Notebook (the command differs by OS)
install_jupyter() {
    pretty_print "Installing Jupyter Notebook..."
    if [[ "$OS" == "macos" ]]; then
        brew install jupyterlab
    else
        python3 -m pip install --user notebook
    fi
    success "Jupyter installed. Launch it with: jupyter notebook"
}

# Feature 6: on macOS, check that Homebrew itself is healthy
brew_health_check() {
    if [[ "$OS" == "macos" ]]; then
        pretty_print "Running brew doctor..."
        # brew doctor returns an error code for simple warnings, so don't stop the script here
        if brew doctor; then
            success "Homebrew is healthy"
        else
            warning "brew doctor reported warnings (see above)"
        fi
    fi
}

# Main logic
pretty_print "Starting environment setup"
detect_os
check_python
check_pip
install_jupyter
brew_health_check
success "Setup complete!"
