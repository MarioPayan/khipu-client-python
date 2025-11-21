#!/bin/bash

case "$1" in
  start)
    echo "Starting server..."
    ;;
  setup)
    echo "Setting up: reinstalling dependencies and initializing database..."
    uv sync --group dev
    echo "DONE"
    ;;
  lint)
    echo "Running linters..."
    uv run black .
    uv run flake8 .
    echo "Cleaning up __pycache__ and .pyc files..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete
    echo "DONE"
    ;;
  build)
    echo "Building package..."
    rm -rf dist/
    uv build
    echo "DONE"
    ;;
  deploy)
    echo "Deploying to PyPI..."
    if [ ! -f .env ]; then
      echo "Error: .env file not found"
      exit 1
    fi
    source .env
    if [ -z "$PYPI_TOKEN" ]; then
      echo "Error: PYPI_TOKEN not found in .env"
      exit 1
    fi
    export TWINE_USERNAME=__token__
    export TWINE_PASSWORD="$PYPI_TOKEN"
    uv run python -m twine upload dist/*
    echo "DONE"
    ;;
  test)
    echo "Running tests..."
    uv run python debug.py
    ;;
  *)
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  🚀 Khipu Backend Runner"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "  Usage: $0 [command]"
    echo ""
    echo "  Commands:"
    echo "    start      - Start the development server"
    echo "    setup      - Install dependencies"
    echo "    lint       - Run black and flake8 linters"
    echo "    build      - Build the package for distribution"
    echo "    deploy     - Deploy the package to PyPI (requires PYPI_TOKEN in .env)"
    echo "    test       - Run debug.py for testing"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    exit 1
    ;;
esac
