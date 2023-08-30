# %% import
import vga
import gwfvis

# %% config
vis_config = gwfvis.create_config()
vga.set_view(vis_config, center=[51, -115], zoom=5)

# %% setup data provider
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.SQLITE_LOCAL_DATA_PROVIDER)
data_provider_plugin = vga.add_plugin(
    vis_config, name=gwfvis.PluginNames.GWFVISDB_DATA_PROVIDER)

# %% add U15 layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'
u15_layer = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.GEOJSON_LAYER)
vga.set_plugin_props(
    u15_layer,
    {
        'displayName': 'U15',
        'layerType': 'overlay',
        'active': True,
        'pointMode': 'pushpin'
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': ['gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'],
        'dataSourceDict': {'U15': 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'}
    }
)

# %% add metadata
metadata = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.METADATA, container='sidebar', container_props={'slot': 'top'})

# %% option1: print the config JSON
print(vis_config)

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %%
