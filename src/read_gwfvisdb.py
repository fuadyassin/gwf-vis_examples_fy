# %%
# ! pip install git+https://github.com/vga-team/python-helper.git
# ! pip install git+https://github.com/vga-team/gwf-vis-python-helper.git

# %% import
from gwfvis import db as gwfvisdb
import json
import urllib.request

# %% download the gwfvisdb file
gwfvisdb_url = (
    "https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/mesh.new.gwfvisdb"
)
gwfvisdb_path = "_.gwfvisdb"
urllib.request.urlretrieve(gwfvisdb_url, gwfvisdb_path)

# %% read the db file
options = gwfvisdb.read_gwfvis_db(gwfvisdb_path)

# %% info
options.info

# %% locations
options.locations

# %% dimensions
options.dimensions

# %% variables
options.variables

# %% values
options.values

# %%
