# Role configuration

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Input Variables Validation settings

--8<--
roles/eos_cli_config_gen/docs/tables/role-input-validation.md
--8<--

## Extensibility with Custom Templates

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommenended to use a `!` delimiter at the top of each custom template.

!!! tip
    The templates will have any host or group variable available to it.
    If adding custom keys to an existing AVD data model, start the key with an underscore `_`, so it will be ignored by schema validation.

--8<--
roles/eos_cli_config_gen/docs/tables/custom-templates.md
--8<--

### eos_cli_config_gen configuration

--8<--
roles/eos_cli_config_gen/docs/tables/eos-cli-config-gen-configuration.md
--8<--

### eos_cli_config_gen documentation

--8<--
roles/eos_cli_config_gen/docs/tables/eos-cli-config-gen-documentation.md
--8<--

### Generate default config

The `generate_default_config` knob allows to omit default EOS configuration.
This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

The following commands will be omitted when `generate_default_config` is set to `false`:

- RANCID Content Type
- Hostname
- Default configuration for `aaa`
- Default configuration for `enable password`
- Transceiver qsfp default mode
- End of configuration delimiter

--8<--
roles/eos_cli_config_gen/docs/tables/generate-default-config.md
--8<--

### Generate device documentation

--8<--
roles/eos_cli_config_gen/docs/tables/generate-device-documentation.md
--8<--
