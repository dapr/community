# Dapr Roadmap

This document outlines the high-level roadmap for the Dapr project. The roadmap is subject to change and is not a commitment to deliver any specific features or timelines. The roadmap is updated every quarter, after a release.

## Releases

[GitHub milestones](https://github.com/dapr/dapr/milestones) are created for each release and are named after the release version. GitHub issues are assigned to a milestone to track the scope and progress of a release.

### Current Release

The current Dapr release is v1.13. Details can be found in the [release notes](https://github.com/dapr/dapr/releases/tag/v1.13.0).

### Next Release

The next release is v1.14. This release is currently in development. The [release planning](https://github.com/dapr/dapr/issues/7605) issue contains milestone dates, and the features and enhancements planned for this release.

### Future Releases

Features or important changes for future releases include:

- Extend the State Management (K/V) API with a `list` operation to list keys based on a prefix.
- Introduce a document store API that supports querying.
- Introduce a blob store API.

New ideas and improvements are always welcome. Please check the existing issues in the relevant Dapr repositories before submitting a new issue with your idea. New APIs or breaking changes to the Dapr runtime should be submitted as proposals in the [dapr/proposals](https://github.com/dapr/proposals) repository.

## Release process

The release cycle and cadence for Dapr is described in [Release Process](release-process.md).
