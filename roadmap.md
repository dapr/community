# Dapr Roadmap

This document outlines the high-level roadmap for the Dapr project. The roadmap is subject to change and is not a commitment to deliver any specific features or timelines. The roadmap is updated every quarter, after a release and during the planning phase.

## Releases

[GitHub milestones](https://github.com/dapr/dapr/milestones) are created for each release and are named after the release version. GitHub issues are assigned to a milestone to track the scope and progress of a release.
Community members and users are encouraged to look through each release milestone and see issues that might be relevant to them. We encourage comments from everyone.

#### Criteria for Change Inclusion

At the beginning of each release, the Dapr project undergoes a feature definition stage of 2 weeks where maintainers triage their respective repositories. This triage process results in looking at issues and labeling them as P0 (must do), P1 (important), and P2 (nice to have). This is decided on two factors: comments and feedback from the community, and the maintainer's technical knowledge of the issue. If a maintainer has decided that an issue is going into the upcoming milestone, the issue will be assigned to the corresponding milestone. Maintainers may ask the community for feedback about certain features or ascertain the importance of fixing bugs and resolving low-key security issues.

In general, the following changes are considered as milestone deliverables:

1. Feature requests - These are viewed as an end-user facing feature that is aligned to the project's goals and technical vision. Feature requests improve the Dapr's projects ability to assist developers in meeting cloud native development challenges, and items that are highly requested by the community will be prioritized higher.
2. Bug fixes - These are viewed as a quality of life improvement for Dapr users. Bug fixes will be prioritized based on the assessed level of impact and criticality.
3. Security issues - Critical security fixes have [their own process](https://docs.dapr.io/operations/support/support-security-issues/) and will often result in a patch release. However, not all issues in Dapr related to security resolve around the project's security itself. Many Dapr features are aimed at improving the security of Dapr-enabled apps, and maintainers are constantly on the lookout for including these in a release as an overall effort to make our ecosystem more secure.

The guidelines above are true for every repository in the Dapr org. The main deliverable in Dapr is the binary produced from the build pipelines in the [Dapr Runtime repo](https://github.com/dapr/dapr) and includes imported [components](https://docs.dapr.io/concepts/components-concept/) from the [components-contrib repo](https://github.com/dapr/components-contrib). New components are added based on community requests. Since components are essentially integrations with 3rd party infrastructure, the project encourages users to contribute components that are used within their organization. When an issue and/or PR for a new component is opened, maintainers will engage with the author and make the decision to include a component based on the following criteria:

1. Usefulness to the broader Dapr community - Dapr maintainers will audit the component to see if this is a niche component or a well known, well tested and properly maintained integration
2. Security requirements - Dapr maintainers will audit the component to make sure all dependencies are aligned with our FOSSA requirements
3. License requirements - Dapr maintainers will audit the component to ensure it has a compatible license that passes the project's license checks

#### Feature removal for components

A Dapr component may be removed if one or more of the following conditions are made true:

1. The SDK supporting the component changes its license to a non-compatible one
2. The component has a critical security vulnerability and is no longer maintained or has no clear roadmap for a fix, AND Dapr maintainers cannot mitigate this on their own without the involvement of the SDK maintainers

#### Feature removal for Dapr APIs (Building Blocks)

Stable APIs are guaranteed to not be removed. During the transition from Alpha to Beta and eventually to Stable (see API lifecycle info [here](https://github.com/dapr/proposals/blob/main/templates/lifecycle.md)), maintainers assess the long term viability of all APIs. Alpha and Beta APIs are subject for removal based on community feedback and examination of the community involvement of an API based on both contributions and adoption.

### Current Release

The current Dapr release is v1.14. Details can be found in the [release notes](https://github.com/dapr/dapr/releases/tag/v1.14.0).

### Next Release

The next release is v1.15. This release is currently in development. The [release planning](https://github.com/dapr/dapr/issues/8017) issue contains milestone dates, and the features and enhancements planned for this release.

### Future Releases

New ideas and improvements are always welcome. Please check the existing issues in the relevant Dapr repositories before submitting a new issue with your idea. New APIs or breaking changes to the Dapr runtime should be submitted as proposals in the [dapr/proposals](https://github.com/dapr/proposals) repository. These proposals are reviewed and voted upon by the relevant maintainers of the repository concerning the proposal.

## Release process

The release cycle and cadence for Dapr is described in [Release Process](release-process.md).
