=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>spanning_tree</samp>](## "spanning_tree") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;root_super</samp>](## "spanning_tree.root_super") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;edge_port</samp>](## "spanning_tree.edge_port") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpdufilter_default</samp>](## "spanning_tree.edge_port.bpdufilter_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard_default</samp>](## "spanning_tree.edge_port.bpduguard_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "spanning_tree.mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;bpduguard_rate_limit</samp>](## "spanning_tree.bpduguard_rate_limit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "spanning_tree.bpduguard_rate_limit.default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "spanning_tree.bpduguard_rate_limit.count") | Integer |  |  |  | Maximum number of BPDUs per timer interval |
    | [<samp>&nbsp;&nbsp;rstp_priority</samp>](## "spanning_tree.rstp_priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mst</samp>](## "spanning_tree.mst") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvst_border</samp>](## "spanning_tree.mst.pvst_border") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;configuration</samp>](## "spanning_tree.mst.configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "spanning_tree.mst.configuration.name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revision</samp>](## "spanning_tree.mst.configuration.revision") | Integer |  |  |  | 0-65535 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;instances</samp>](## "spanning_tree.mst.configuration.instances") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst.configuration.instances.[].id") | Integer | Required, Unique |  |  | Instance ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "spanning_tree.mst.configuration.instances.[].vlans") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18<br> |
    | [<samp>&nbsp;&nbsp;mst_instances</samp>](## "spanning_tree.mst_instances") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst_instances.[].id") | String | Required, Unique |  |  | Instance ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.mst_instances.[].priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;no_spanning_tree_vlan</samp>](## "spanning_tree.no_spanning_tree_vlan") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
    | [<samp>&nbsp;&nbsp;rapid_pvst_instances</samp>](## "spanning_tree.rapid_pvst_instances") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.rapid_pvst_instances.[].id") | String | Required, Unique |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.rapid_pvst_instances.[].priority") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    spanning_tree:
      root_super: <bool>
      edge_port:
        bpdufilter_default: <bool>
        bpduguard_default: <bool>
      mode: <str>
      bpduguard_rate_limit:
        default: <bool>
        count: <int>
      rstp_priority: <int>
      mst:
        pvst_border: <bool>
        configuration:
          name: <str>
          revision: <int>
          instances:
            - id: <int>
              vlans: <str>
      mst_instances:
        - id: <str>
          priority: <int>
      no_spanning_tree_vlan: <str>
      rapid_pvst_instances:
        - id: <str>
          priority: <int>
    ```
