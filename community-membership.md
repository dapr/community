
# Community membership

This doc outlines the responsibilities of contributor roles in Dapr. The Dapr project is subdivided into sub-projects under (predominantly, but not exclusively) runtime (dapr), components-contrib, CLI, quickstarts, docs and language-specific SDKs. Responsibilities for roles are scoped to these sub-projects (repos).

| **Role**   | **Responsibilities**                                  | **Requirements**                                             | **Defined by**                                               |
| ---------- | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Member     | Active contributor in the community.  Reviewer of PRs | Sponsored by two approvers or maintainers. Multiple contributions to the project. | Dapr GitHub org member                           |
| Approver   | Approve accepting contributions                       | Highly experienced and active reviewer and contributor to a subproject. | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners) in GitHub |
| Core-Maintainer | Set direction and priorities for a subproject         | Demonstrated responsibility and excellent technical judgement for the subproject. | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners), GitHub Team and repo ownership in GitHub |
| Feature-Maintainer | Set direction and priorities for a subarea of project/repo         | Demonstrated responsibility and excellent technical judgement for the subarea. | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners), GitHub Team and repo ownership in GitHub |

> Note: The Steering & Technical Committee (STC) referred to in this document is described [here](./steering-and-technical-committee-charter.md)

## New contributors

New contributors should be welcomed to the community by existing members, helped
with PR workflow, and directed to relevant documentation and communication
channels.

## Established community members

Established community members are expected to demonstrate their adherence to the
principles in this document, familiarity with project organization, roles, policies, procedures, conventions, etc., and technical and/or writing ability.
Role-specific expectations, responsibilities, and requirements are enumerated
below.

## Member

Members are continuously active contributors in the community. They can have issues and PRs assigned to them. Members are expected to participate in community discussions and remain active contributors to the community.  

Defined by: Member of the Dapr GitHub organization

### Requirements

- Enabled [two-factor authentication](https://help.github.com/articles/about-two-factor-authentication) on their GitHub account
- Have made multiple contributions to the project or community. Contributions may include, but is not limited to:
  - Authoring or reviewing PRs on GitHub
  - Filing or commenting on issues on GitHub
  - Contributing to sub-projects, or community discussions (e.g. meetings,
    chat, etc.)
- [Joined the Discord server](https://aka.ms/dapr-discord)
- Have read the [contributor
  guide](https://github.com/dapr/dapr/blob/master/CONTRIBUTING.md)
- Actively contributing to 1 or more sub-projects
- Sponsored by two approvers or maintainers (sponsors). Note the following requirements for sponsors:
  - Sponsors must have close interactions with the prospective member - e.g. code/design/proposal review, coordinating on issues, etc
  - Sponsors must be approvers or maintainers in at least one CODEOWNERS file in any repo in the Dapr org
- [Open an
  issue](https://github.com/dapr/community/issues/new?template=membership.md&title=REQUEST%3A%20New%20membership%20for%20%3Cyour-GH-handle%3E)
  against the
  [Dapr/community](https://github.com/dapr/community) repo
  - Ensure your sponsors are `@mentioned` on the issue
  - Complete every item on the checklist ([preview the current version of the
    template](https://github.com/dapr/community/blob/master/.github/ISSUE_TEMPLATE/membership.md))
  - Make sure that the list of contributions included is representative of your work on the project
- Have your sponsoring reviewers reply confirmation of sponsorship: `+1`
- Once your sponsors have responded, your request will be reviewed by the Steering & Technical Committee (STC). Any member of the Steering & Technical Committee can review the requirements and add Members to the GitHub org

### Responsibilities and privileges

- Responsive to issues and PRs assigned to them
- Active owner of code contributed by them (unless ownership is explicitly
  transferred)
  - Code is well tested
  - Tests consistently pass
  - Addresses bugs or issues discovered after code is accepted
  - Members are encouraged to review and approve via the GitHub workflow. This review work, while not sufficient to merge a PR, does accrue toward the Member becoming an Approver. Merge approval and final review are performed by an Approver
- Members can be assigned to issues and PRs, and people can ask members for reviews with a `/cc @username`

> Note: members who frequently contribute code are expected to proactively perform code reviews and work towards becoming an *approver* for the sub-projects in which they are active.  Acceptance of code contributions requires at least one approver in addition to the reviews by *members.*

## Approver

Code approvers are able to both review and approve code contributions, as well as help maintainers triage issues and do project management.

While code review is focused on code quality and correctness, approval is
focused on holistic acceptance of a contribution including: backwards/forwards
compatibility, adhering to API and conventions, performance and correctness issues, interactions with other sub-projects, etc.

Defined by: [CODEOWNERS
workflow](https://help.github.com/en/articles/about-code-owners).

Approver status can be scoped to a part of the codebase. For example, critical core components may have higher bar for becoming an approver.

### Requirements

The following apply to the part of the codebase for which one would be an approver in the `CODEOWNERS` files:
- Reviewer of the codebase for at least 1 month
- Reviewer for, or author of, at least 5 substantial PRs to the codebase,
  with the definition of substantial area to the maintainer's discretion
  (e.g. refactors/adds new functionality rather than one-line pulls)
- Nominated by a maintainer from the repository in which the nomination is applied to:
  - With an approving vote of at least 2 maintainers from the repository maintainers. In the case of a repository with a solo maintainer, a single vote suffices
  - With no objections from other repository maintainers for a period of one week
  - Steering committee acts as the final resolution to any escalation
  - Done through PR to update the `CODEOWNERS` 

### Responsibilities and privileges

The following apply to the part of the codebase for which one would be an approver in the `CODEOWNERS` files.

- Approver status may be a precondition to accepting large code contributions
- Demonstrate sound technical judgement (may be asked to step down by a maintainer if they lose confidence of the maintainers)
- Responsible for project quality control via code reviews
  - Focus on holistic acceptance of contribution such as dependencies with other
    features, backwards / forwards compatibility, API and conventions, etc
- Expected to be responsive to review requests (inactivity for more than 1 month may result in suspension until active again)
- Mentor contributors and reviewers
- May approve code contributions for acceptance
- Inactivity for more than 3 months leads to a removal vote by other maintainers/approvers and not an automatic removal

## Core-Maintainer

Core-Maintainers are the technical authority for a subproject in the Dapr org. They *MUST* have demonstrated both good judgement and responsibility towards the health of that subproject. Core Maintainers *MUST* set technical direction and make or approve design decisions for their subproject - either directly or through delegation of these responsibilities.

Defined by: GitHub organization ownership, permissions and entry in `CODEOWNERS`
files.

### Requirements

The following apply to the subproject for which one would be an owner:

- Deep understanding of the technical goals and direction of the subproject
- Deep understanding of the technical domain (specifically the language) of the
  subproject
- Sustained contributions to design and direction by doing all of:
  - Authoring and reviewing proposals
  - Initiating, contributing and resolving discussions (e.g. emails, GitHub issues, meetings)
  - Identifying subtle or complex issues in designs and implementation PRs
- Directly contributed to the subproject through implementation and / or review
- Aligning with the overall project goals, specifications and design principles defined by the Technical & Steering Committee. Bringing general questions and requests to the discussions as part of specifications project
- Must have been active for 3 months or more for the given sub-project
- Inactivity for more than 3 months leads to a removal vote by other maintainers and not an automatic removal

### Acceptance

New Core-maintainers can be added to the project by a super-majority (two-thirds / 66.66%) vote. Only the Core-maintainers of the repository in which the nomination is applied to have a binding vote, while Core-maintainers from other repositories are on an informed basis via a separate email thread. A potential Core-maintainer may be nominated by an existing Core-maintainer from the repository in which the nomination is applied to. A vote is conducted in private between the current Core-maintainers over the course of a one week voting period. At the end of the week, votes are counted and a pull request is made on the repo adding the new core-maintainer to the CODEOWNERS file.

Core-maintainers for new repositories can be nominated by any member of the steering committee and voted on in a steering committee meeting.
Single Core-maintainers of a repository can nominate a new Core-maintainer and *MUST* inform the steering committee of their intention. The Core-maintainer can be approved if no objections have been raised in a period of one week.

A Core-maintainer may step down by submitting an issue stating their intent.

### Responsibilities and privileges

The following apply to the subproject(repos) for which one would be an owner:

- Make and approve technical design decisions for the subproject
- Set technical direction and priorities for the subproject
- Define milestones and releases
  - Decides on when PRs are merged to control the release scope
- Mentor and guide approvers and contributors to the subproject
- Escalate *approver* and *maintainer* workflow concerns (i.e. responsiveness, availability, and general contributor community health) to the TC
- Ensure continued health of subproject:
  - Adequate test coverage to confidently release
  - Tests are passing reliably (i.e. not flaky) and are fixed when they fail
- Ensure a healthy process for discussion and decision making is in place
- Work with other maintainers to maintain the project's overall health and success holistically

Core-Maintainers *MUST* remain active. If they are unresponsive for >3 months, they will be automatically removed unless a super-majority of the other repository maintainers agrees to extend the period to be greater than 3 months.

## Feature-Maintainer

Feature-Maintainers are the technical authority for a subarea of the project/repo in the Dapr org. They *MUST* have demonstrated both good judgement and responsibility towards the health of that subarea. Feature-maintainers can set technical direction and make or approve design decisions for their subarea - either directly or through delegation of these responsibilities.

Defined by: GitHub organization ownership, permissions and entry in `CODEOWNERS`
files.

### Requirements

The following apply to the sub area(ex: building block API/ Control plane service/ Component provider) for which one would be a Feature-maintainer:

- Deep understanding of the technical goals and direction of the sub area.
- Deep understanding of the technical domain (specifically the language) of the sub area
- Sustained contributions to design and direction by doing all of:
  - Authoring and reviewing proposals
  - Initiating, contributing and resolving discussions  For example Discord discussions,  GitHub issues, meetings)
  - Identifying subtle or complex issues in designs and implementation PRs
- Directly contributed to the subarea through implementation and / or review
- Must have been active for 3 months or more for the given sub-area
- Inactivity for more than 3 months leads to a removal vote by the repo maintainers and not an automatic removal


### Acceptance

  New Feature-Maintainers can be added to the project by a super-majority (two-thirds / 66.66%) vote. Only the maintainers of the repository in which the nomination is applied have a binding vote, while maintainers from other repositories are on an informed basis via a separate email thread.

  A potential feature-maintainer may be nominated by an existing maintainer from the repository in which the nomination is applied to. A vote is conducted in private between the current maintainers over the course of a one week voting period. At the end of the week, votes are counted, and a pull request is made on the repo adding the new feature-maintainer to the feature-maintainers.md file.

  Feature-maintainers MUST remain active. If they are unresponsive for >3 months, they will be automatically removed unless a super-majority of the other repository maintainers agrees to extend the period to be greater than 3 months.

  A feature-maintainer may step down by submitting an issue stating their intent.

### Example of Feature Maintainers in DAPR Runtime repo:
Sub Area
Person Name
Workflow
Chris Gillum
Control Plane Service(mTLS)
Josh V

| **Subarea**   | **Name**                                  |
| ---------- | ---------------------------------------------| 
| Workflow    | Chris Gilum                                 | 
| Control Plane Service(mTLS)| Josh V |

### Responsibilities and privileges

The following applies to the sub area(ex: building block API/ Control plane service/ Component provider) for which the feature-maintainer would be an owner:

- Make and approve technical design decisions for the sub area
- Set technical direction and priorities for the sub area.
- Define milestones and releases working along with the maintainers
- Decides on when PRs are merged to control the release scope
- Mentor and guide approvers and contributors of the sub area
- Escalate approver and maintainer workflow concerns. (For example responsiveness, availability, and general contributor community health) to the STC
- Ensure continued health of sub area:
- Adequate test coverage to confidently release
- Tests are passing reliably (not flaky) and are fixed when they fail.
- Work with other feature-maintainers & Core-maintainers to maintain the project's overall health and success holistically.
- Membership tracked in feature-maintainer.md entry and scoped to a sub area.
- MUST maintain components, review, and approve proposals for enhancing areas falling under the user sub area.
- Actively participate in issue triages and PR reviews
- Set milestone priorities for the sub areas or delegate the responsibility to repo maintainers.
- Ensure a healthy process for discussion and decision making is in place
