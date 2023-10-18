# %%
# ! pip install git+https://github.com/vga-team/python-helper.git
# ! pip install git+https://github.com/vga-team/gwf-vis-python-helper.git

# %% import
import vga
from gwfvis import conf as gwfvisconf
import json
import os

# %% config
vis_config = gwfvisconf.create_config()
vga.set_view(vis_config, center=[51.3, -116], zoom=10)

# REQUEST LOCAL FILE ACCESS PERMISSION
vga.set_access_local_files(vis_config, True)

# NEED TO MAKE SURE THE PATH EXISTS WITHIN THE ROOT DIRECTORY THAT WOULD BE ASKED TO SELECT WHEN THE VIS LOADED
local_file_path = "test/mesh.gwfvisdb"

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.SQLITE_LOCAL_DATA_PROVIDER
)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.GWFVISDB_DATA_PROVIDER
)

# %% add MESH layer
data_source = f"gwfvisdb:file:{local_file_path}"
mesh_layer = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.GEOJSON_LAYER
)
vga.set_plugin_props(
    mesh_layer, {"displayName": "MESH", "layerType": "overlay", "active": True}
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.DATA_CONTROL,
    container="main",
    props={"dataSources": [data_source], "dataSourceDict": {"MESH": data_source}},
)

# %% add location pins
metadata = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.LOCATION_PIN,
    container="sidebar",
    container_props={"slot": "top"},
)

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.METADATA, container="sidebar"
)

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.LINE_CHART,
    container="sidebar",
    props={"dataFor": {"dimensionName": "time", "dataSource": data_source}},
)

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.LINE_CHART,
    container="sidebar",
    props={
        "dataFor": {
            "variableNames": [
                "STGW",
                "SNO",
            ],
            "dimensionName": "time",
            "dataSource": data_source,
        }
    },
)


# %% add legend
metadata = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.LEGEND,
    container="main",
    container_props={"width": "20rem"},
)

# %% option1: print the config JSON
print(json.dumps(vis_config))

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %% option3: save as a config file
config_directory = "../out"
config_file_name = "mesh_local_file.vgaconf"
if not os.path.exists(config_directory):
    os.makedirs(config_directory)
with open(f"{config_directory}/{config_file_name}", 'w') as file:
    file.write(json.dumps(vis_config))

# %%
