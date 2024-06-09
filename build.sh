module load StdEnv/2020
#module load gcc/9.3.0

source /home/fuaday/.venv/bin/activate

# Install requirements using the Python interpreter from the virtual environment
#python -m pip install -r /home/fuaday/github-repos/gwf-vis_examples_fy/requirements.txt
python -m pip install -r /home/fuaday/github-repos/gwf-vis_examples_fy/requirements.txt
python -m pip install jupytext nbconvert
rm -rf out
cd src
for f in *.py; do {
    python "$f"
    ipynb_path="../out/$(echo "${f%.*}").ipynb"
    jupytext "$f" -o "$ipynb_path"
    jupyter nbconvert "$ipynb_path" --to html
}; done
cp *.py ../out/