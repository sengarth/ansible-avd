=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_root</samp>](## "aaa_root") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "aaa_root.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_root.secret.sha512_password") | String |  |  |  |  |

=== "YAML"

    ```yaml
    aaa_root:
      secret:
        sha512_password: <str>
    ```
