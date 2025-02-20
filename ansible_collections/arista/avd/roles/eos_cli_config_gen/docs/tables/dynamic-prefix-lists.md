=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dynamic_prefix_lists</samp>](## "dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "dynamic_prefix_lists.[].match_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "dynamic_prefix_lists.[].prefix_list") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv4") | String |  |  |  | Prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv6") | String |  |  |  | Prefix-list name |

=== "YAML"

    ```yaml
    dynamic_prefix_lists:
      - name: <str>
        match_map: <str>
        prefix_list:
          ipv4: <str>
          ipv6: <str>
    ```
