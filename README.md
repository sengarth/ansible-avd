# Arista Validated Designs

![Arista AVD](https://img.shields.io/badge/Arista-AVD%20Automation-blue) ![collection version](https://img.shields.io/github/v/release/aristanetworks/ansible-avd) ![License](https://img.shields.io/github/license/aristanetworks/ansible-avd)

<center><img src="ansible_collections/arista/avd/media/avd-logo.png" alt="Arista AVD Overview" width="800"/></center>

Arista Validated Designs (AVD) is an extensible data model that defines Arista's Unified Cloud Network architecture as "code".

AVD Documentation:

- [Stable version](https://avd.arista.com/stable/)
- [Development version](https://www.avd.sh/en/devel/)

## Features

- **Flexibility with Open Data Models:** Extensible fabric-wide network models, simplifying configuration, delivering consistency, and reducing errors
- **Simplification through Multi-Domain Automation:** A framework that can automate the data center, campus or wide area network, enabled by a consistent EOS software image and management platform
- **Comprehensive Workflows:** Automating the full life cycle of network provisioning from config generation to pre and post-deployment validation, and self-documentation of the network

## Reference designs

- [L3LS VXLAN-EVPN, L2LS, and MPLS](https://avd.arista.com/stable/roles/eos_designs/index.html)

## AVD Ansible Collection

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running Arista's **Extensible Operating System (EOS)** natively through it's **EOS API (eAPI)** or [**CloudVision Portal (CVP)**](https://www.arista.com/en/products/eos/eos-cloudvision). The collection includes a set of Ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs.

### Examples

- [Getting started](https://avd.arista.com/stable/docs/getting-started/intro-to-ansible-and-avd.html)
- [Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

### Additional resources

- Ansible [EOS modules](https://docs.ansible.com/ansible/latest/collections/arista/eos/index.html) on Ansible documentation
- Ansible [CloudVision modules](https://cvp.avd.sh/en/stable/)
- [CloudVision Portal](https://www.arista.com/en/products/eos/eos-cloudvision)
- [Arista Design and Deployment Guides](https://www.arista.com/en/solutions/design-guides)

## Ask a question

Support for this `arista.avd` collection is provided by the community directly in this repository. If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it. Please see [contribution guide](./ansible_collections/arista/avd/docs/contribution/overview.md) for additional details.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problems or submit requests for enhancements.

## License

The project is published under [Apache 2.0 License](./LICENSE)
