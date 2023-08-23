# %% import
from gwfvis import core as gwfvis_core, default as gwfvis_default

# %% config
vis_config = gwfvis_default.create_config()
gwfvis_core.set_view(vis_config, center=[51, -115], zoom=5)

# %% setup data provider
data_provider_plugin = gwfvis_core.add_plugin(
    vis_config, name='gwf-default.sqlite-local-data-provider')
data_provider_plugin = gwfvis_core.add_plugin(
    vis_config, name='gwf-default.gwfvisdb-data-provider')

# %% add U15 layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'
u15_layer = gwfvis_core.add_plugin(
    config=vis_config, name='gwf-default.geojson-layer')
gwfvis_core.set_plugin_props(
    u15_layer,
    {
        'displayName': 'U15',
        'layerType': 'overlay',
        'active': True,
        'pointMode': 'pushpin'
    }
)
# %% add data control
data_control = gwfvis_core.add_plugin(
    config=vis_config, name='gwf-default.data-control', container='main', props={
        'dataSources': ['gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'],
        'dataSourceDict': {'U15': 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/u15.gwfvisdb'}
    }
)

# %% add metadata
metadata = gwfvis_core.add_plugin(
    config=vis_config, name=gwfvis_default.PluginNames.METADATA, container='sidebar', container_props={'slot': 'top'})

# %% option1: print the config JSON
print(vis_config)

# %% option2: print the URL
print(gwfvis_core.generate_vis_url(vis_config))

# %%
