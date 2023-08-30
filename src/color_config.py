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

# %% define color scheme
color_scheme = {
    '': {  # '' is for default (any variables that is not defined here)
        # here we use a quantize scale for custom array of colors
        'type': 'quantize',
        'scheme': ['blue', 'green', 'yellow', 'red']
    },
    'scalarCanopyWat': {  # color definition for scalarCanopyWat only
        # here we use a quantile scale for custom array of colors
        'type': 'quantile',
        'scheme': ['blue', 'green', 'yellow', 'red']
    },
    'scalarSWE': {  # color definition for scalarSWE only
        # here we use a sequential scale for custom array of colors
        'type': 'sequential',
        'scheme': ['blue', 'green', 'yellow', 'red']
    },
    'scalarTotalIET': {  # color definition for scalarTotalIET only
        # here we use a quantize scale for builtin color scheme, the builtin scheme names can be found at https://github.com/d3/d3-scale-chromatic
        'type': 'quantize',
        # use a single string instead of an array means to use the built in scheme
        'scheme': 'schemeOranges[5]'
    },
    'scalarTotalRunoff': {  # color definition for scalarTotalRunoff only
        # here we use a sequential scale for builtin color scheme, the builtin scheme names can be found at https://github.com/d3/d3-scale-chromatic
        'type': 'sequential',
        # use a single string instead of an array means to use the built in scheme, note that for sequntial, you have to use interpolate colors
        'scheme': 'interpolateOranges'
    }
}

# %% add SUMMA layer
data_source = 'gwfvisdb:https://gwf-vis.usask.ca/v1/api/file/fetch/public/datasets/catchment.gwfvisdb'
summa_layer = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.GEOJSON_LAYER)
vga.set_plugin_props(
    summa_layer,
    {
        'displayName': 'SUMMA',
        'layerType': 'overlay',
        'active': True,
        'colorScheme': color_scheme
    }
)
# %% add data control
data_control = vga.add_plugin(
    config=vis_config, name=gwfvis.PluginNames.DATA_CONTROL, container='main', props={
        'dataSources': [data_source],
        'dataSourceDict': {'SUMMA': data_source}
    }
)

# %% add legend
metadata = vga.add_plugin(
    config=vis_config,
    name=gwfvis.PluginNames.LEGEND,
    container='main',
    props={'colorScheme': color_scheme},
    container_props={'width': '20rem'}
)

# %% option1: print the config JSON
print(json.dumps(vis_config))

# %% option2: print the URL
print(vga.generate_vis_url(vis_config))

# %%
