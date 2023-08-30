# %%
# ! pip install git+https://github.com/gwf-vis/vga-python-lib.git
# ! pip install git+https://github.com/gwf-vis/gwf-vis-python-lib.git

# %% import
import vga
import gwfvis
import json

# %% config
vis_config = gwfvis.create_config()
vga.set_view(vis_config, center=[51.3, -116], zoom=10)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.SQLITE_LOCAL_DATA_PROVIDER)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.GWFVISDB_DATA_PROVIDER)

# %% add MESH layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/mesh.new.gwfvisdb'
mesh_layer = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.GEOJSON_LAYER)
vga.set_plugin_props(
    mesh_layer,
    {
        'displayName': 'MESH',
        'layerType': 'overlay',
        'active': True
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': [data_source],
        'dataSourceDict': {'MESH': data_source}
    }
)

# %% add location pins
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LOCATION_PIN, container='sidebar', container_props={'slot': 'top'})

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.METADATA, container='sidebar')

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LINE_CHART, container='sidebar', props={
        'dataFor': {
            'dimensionName': 'time',
            'dataSource': data_source
        }
    })

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LINE_CHART, container='sidebar', props={
        'dataFor': {
            'variableNames': [
                'STGW',
                'SNO',
            ],
            'dimensionName': 'time',
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
