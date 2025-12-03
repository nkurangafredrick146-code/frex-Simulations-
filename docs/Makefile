.PHONY: test coverage docs package clean

test:
PYTHONPATH=. pytest -v

coverage:
PYTHONPATH=. pytest --cov=scene_env --cov=quantum_env --cov-report=term-missing

docs:
cd docs && make html

package:
python setup.py sdist bdist_wheel

clean:
rm -rf __pycache__ .pytest_cache dist build *.egg-info docs/build
