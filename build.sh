python -m pip install -r requirements.txt
python -m pip install jupytext nbconvert
rm -rf out
cd src
for f in *.py; do {
    python "$f"
    ipynb_path="../out/$(echo "${f%.*}" | cut -d'_' -f1).ipynb"
    jupytext "$f" -o "$ipynb_path"
    jupyter nbconvert "$ipynb_path" --to html
}; done
cd ../out