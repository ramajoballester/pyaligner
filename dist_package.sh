python -m build ./ --sdist
python -m build ./ --wheel
twine check ./dist/*
python -m twine upload ./dist/*