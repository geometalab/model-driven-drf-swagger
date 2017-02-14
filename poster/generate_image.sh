#!/bin/bash
set -e
python3 ../app/manage.py graph_models example -l dot -S > example_model_vizualized.dot
dot -Gdpi=1200 example_model_vizualized.dot -Tpng -o example_model_vizualized.png
rm example_model_vizualized.dot
