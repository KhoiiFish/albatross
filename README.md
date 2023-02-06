# Albatross
Albatross, an interactive itinerary planning application.

## Pre-commit
Pre-commit is a multi-language package manager for pre-commit hooks. Run

```
pre-commit install
```

This installs the versions in .pre-commit-config.yaml and sets it up as a pre-commit hook (it only takes a long time the
first time as it's installing). Currently, this will run the following pre-commit hooks:

* isort
* black (version must be kept consistent between .yaml and setup.py)

In addition to this, autoflake and mypy are offered as manual pre-commit commands. Autoflake is run manually because it
albeit very rarely, removes forward referencing types. When running hooks manually, the recommended order is

```
# 1. autoflake
pre-commit run --hook-stage manual autoflake
# 2. isort then black (configured in pre-commit-config.yaml already)
pre-commit run
# 3. mypy
pre-commit run --hook-stage manual mypy-local
```

Add `--files {files}` to only run the pre-commit hook on specific files. Autoflake is run first, so mypy can pick up if
a type has been removed and so that black fixes any unwanted formatting changes from autoflake.

To run a specific hook use `pre-commit run <hook-id> --files {file}`. 

This configuration is currently intended to run with CI pipelines only utilising black. 

