# %% install
# ! pip install git+https://github.com/vga-team/python-helper.git
# ! pip install git+https://github.com/vga-team/gwf-vis-python-helper.git

# %% import
import vga
import gwfvis
import json

# %% config
vis_config = gwfvis.create_config()
vga.set_view(vis_config, center=[56.4, -123.2], zoom=6)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.SQLITE_LOCAL_DATA_PROVIDER)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.GWFVISDB_DATA_PROVIDER)

# %% add permafrost layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/permafrost_reduced_fill_null.gwfvisdb'
permafrost_layer = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.CONTOUR_LAYER)
vga.set_plugin_props(
    permafrost_layer,
    {
        'thresholds': 10,
        'displayName': 'Permafrost',
        'layerType': 'overlay',
        'active': True
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': [data_source],
        'dataSourceDict': {'Permafrost': data_source}
    }
)

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.METADATA, container='sidebar')

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LINE_CHART, container='sidebar', props={
        'dataFor': {
            'dimensionName': 'level',
            'dataSource': data_source
        }
    })


# %% add legend
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LEGEND, container='main', container_props={'width': '20rem'})

# %% option1: print the config JSON
print(json.dumps(vis_config))

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %%
