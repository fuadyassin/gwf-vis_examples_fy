# %%
# ! pip install git+https://github.com/vga-team/python-helper.git
# ! pip install git+https://github.com/vga-team/gwf-vis-python-helper.git

# %% import
import vga
import gwfvis
import json

# %% config
vis_config = gwfvis.create_config()
vga.set_view(vis_config, center=[0, 0], zoom=2)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.SQLITE_LOCAL_DATA_PROVIDER)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.GWFVISDB_DATA_PROVIDER)

# %% add GDP layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/gdp.gwfvisdb'
gdp_layer = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.GEOJSON_LAYER)
vga.set_plugin_props(
    gdp_layer,
    {
        'displayName': 'GDP',
        'layerType': 'overlay',
        'active': True
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': [data_source],
        'dataSourceDict': {'GDP': data_source}
    }
)

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.METADATA, container='sidebar', container_props={'slot': 'top'})

# %% add line chart
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.LINE_CHART, container='sidebar', props={
        'dataFor': {
            'dimensionName': 'time',
            'dataSource': data_source,
            'locationLabelKey': 'ADMIN',
        }
    })

# %% option1: print the config JSON
print(json.dumps(vis_config))

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %%
