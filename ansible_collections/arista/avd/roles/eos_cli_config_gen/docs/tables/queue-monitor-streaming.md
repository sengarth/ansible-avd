=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>queue_monitor_streaming</samp>](## "queue_monitor_streaming") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "queue_monitor_streaming.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ip_access_group</samp>](## "queue_monitor_streaming.ip_access_group") | String |  |  |  | Name of IP ACL |
    | [<samp>&nbsp;&nbsp;ipv6_access_group</samp>](## "queue_monitor_streaming.ipv6_access_group") | String |  |  |  | Name of IPv6 ACL |
    | [<samp>&nbsp;&nbsp;max_connections</samp>](## "queue_monitor_streaming.max_connections") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "queue_monitor_streaming.vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    queue_monitor_streaming:
      enable: <bool>
      ip_access_group: <str>
      ipv6_access_group: <str>
      max_connections: <int>
      vrf: <str>
    ```
