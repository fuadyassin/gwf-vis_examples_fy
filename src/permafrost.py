# %% install
# ! pip install git+https://github.com/vga-team/py-lib.git
# ! pip install git+https://github.com/vga-team/gwf-vis_lib.git

# %% import
import vga
from gwfvis import conf as gwfvisconf
import json
import os

# %% config
vis_config = gwfvisconf.create_config()
vga.set_view(vis_config, center=[56.4, -123.2], zoom=6)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.SQLITE_LOCAL_DATA_PROVIDER
)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvisconf.PluginNames.GWFVISDB_DATA_PROVIDER
)

# %% add permafrost layer
data_source = "gwfvisdb:https://gwf-vis.usask.ca/assets/datasets/permafrost_reduced_fill_null.gwfvisdb"
permafrost_layer = vga.add_plugin(
    config=vis_config, name=gwfvisconf.PluginNames.CONTOUR_LAYER
)
vga.set_plugin_props(
    permafrost_layer,
    {
        "thresholds": 10,
        "displayName": "Permafrost",
        "layerType": "overlay",
        "active": True,
    },
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config,
    name=gwfvisconf.PluginNames.DATA_CONTROL,
    container="main",
    props={"dataSources": [data_source], "dataSourceDict": {"Permafrost": data_source}},
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
    props={"dataFor": {"dimensionName": "level", "dataSource": data_source}},
)


# %% add legend
legend = vga.add_plugin(
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
config_file_name = "permafrost.vgaconf"
if not os.path.exists(config_directory):
    os.makedirs(config_directory)
with open(f"{config_directory}/{config_file_name}", 'w') as file:
    file.write(json.dumps(vis_config))

# %%
