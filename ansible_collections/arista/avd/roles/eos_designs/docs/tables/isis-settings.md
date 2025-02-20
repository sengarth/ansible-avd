=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | `False` |  |  |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | `49.0001` |  |  |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level. |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | `50` |  | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level. |
    | [<samp>isis_maximum_paths</samp>](## "isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | `10000` |  | Local convergence delay in milliseconds. |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  | Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls. |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool>
    isis_area_id: <str>
    isis_default_circuit_type: <str>
    isis_default_is_type: <str>
    isis_default_metric: <int>
    isis_maximum_paths: <int>
    isis_ti_lfa:
      enabled: <bool>
      protection: <str>
      local_convergence_delay: <int>
    underlay_isis_instance_name: <str>
    ```
