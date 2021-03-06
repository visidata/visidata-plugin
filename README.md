# VisiData plugin cookiecutter template

Documentation:

* [VisiData plugins](https://www.visidata.org/docs/api/plugins)
* [configurable options](https://www.visidata.org/docs/api/options)
* [creating new commands](https://www.visidata.org/docs/api/commands)
* [writing a new data loader](https://www.visidata.org/docs/api/loaders)
* [writing a new data saver](https://www.visidata.org/docs/api/savers)

You can use this template with [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html), or create a new repository based on the template and modify by hand.

## Requirements

* Python 3.7
* [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html)

## Usage

Run `cookiecutter gh:visidata/visidata-plugin` and then answer the prompts. This will help set the fundamentals for your plugin structure.

If you are not using cookiecutter, rename {{cookiecutter.plugin_name}}.py to the name of your plugin, and add the plugin code to it.

## Publishing your plugin

To publish a plugin:

1. Make public Github repo with your `.py` file.
2. Fork `[visidata:dlc](https://github.com/visidata/dlc)`
3. Add a row to `visidata-plugins.jsonl' with all of the necessary information. (If using cookiecutter, it will create a template for your row in [plugins-sample.jsonl](https://github.com/visidata/visidata-plugin/blob/stable/plugins-sample.jsonl).)

* `name`: short name of the plugin (like `vfake`). Less than 20 characters.
* `description`: a one-line searchable description of the core features. Less than 1000 characters.
* `maintainer`: like `Your Name <name@example.com>`.
* `latest_release`: date of most recent release, ISO formatted like `2020-02-02`.
* `latest_ver`: version of most recent release, like `v1.4`.
* `url`: link to the primary page (which may be the raw .py file itself, if it describes itself effectively).
* `visidata_ver`: version of VisiData required, like `v2.0`.
* `pydeps`: space-separated list of PyPI dependencies (like in requirements.txt).
* `vdplugindeps`: space-separated list of vd plugin dependencies.
* `sha256`: SHA256 hash of plugin .py of most recent release. A script for obtaining this has can be found in [vdhash.py](https://raw.githubusercontent.com/visidata/visidata-plugin/stable/vdhash.py).

4. Submit a PR to the `visidata/dlc` repo.
5. We will do basic review and then merge the PR.
6. VisiData users will be able to see the plugin using `plugins-sheet` within 24 hours.
