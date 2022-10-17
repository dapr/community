# Release cycle and cadence 
The Dapr project aims to release four updates in a yearly time period, typically one in each quarter (every 3 months). For example in 2022 the minor releases were Jan (1.6.0), April (1.7.0), July (1.8.0), Oct (1.9.0) and the same is expected for 2023.


<img src="images/release-cycle-diagram.png?raw=true">


This cadence provides a balance between regular feature releases and bug fixes, giving end users time to adopt a release and providing contributors clarity on releases they can contribute towards. By having a regular “train” of releases end users and contributors can plan ahead. 

## Release milestone
The Dapr project is under continuous development addressing issues for both bugs on existing features and new features. Features go through a lifecycle from proposal, design, code, test, docs, and often quickstart and SDKs deliverables. Feature proposals can be raised and reviewed by the community and maintainers at any time. 

Dapr is an open source and agile project, with feature planning and implementation happening at all times. Given the project scale and globally distributed developer base, it is critical to project velocity to not solely rely on a stabilization phase and rather have continuous integration testing which ensures the project is always stable so that individual commits can be flagged as having broken something. This includes continuous feature tests suites, performance tests and end-to-end testing for integration.

Each release goes through three phases in a 13 week (3 month) period.
-	Feature definition (~ 2 weeks)
-	Feature implementation and bug fixing (~ 9 weeks)
-	Stabilization and release (~ 2 weeks)


<img src="images/feature-definition-diagram.png?raw=true">


Most significant features take at least 2 releases to become included in a release, and through the preview feature process often more. Therefore as a release comes to a close, it is not unusual to move a complex feature to the next milestone to give it time to complete the requirements of the feature lifecycle.

## Release team
At the start of a milestone a release team is chosen. The release team has the responsibility of enforcing processes to ensure the release is successfully delivered. The release team consists of the following roles:

-	**Release lead.** This role oversees enforcing the processes for a release and ensuring communication to all contributors and community on the ongoing status of the release. This role requires to have at least been a release team shadow previously.
-	**Release lead shadow(s).** This role is identical to the lead and is interchangeable. The only difference is that the lead can delegate activities to the shadow to share distribution of work. There needs to be at least one shadow for a release, preferably two.
-	**Release performance test lead.** This role is responsible for overseeing the continuous monitoring of the performance tests, ensuring new tests are added when needed and reporting on them weekly.
-	**Release long-haul test lead.** This role is responsible for overseeing the continuous monitoring of the end-to-end tests, ensuring new tests are added for new features in this release and reporting on them weekly.
-	**Build manager.** This role applies in the stabilization phase and is responsible for creating the RC releases, the final build/testing and release branches.
  
On assignment, the release team lead and shadow(s) are included into the Github release team group. They are responsible for;
- [ ] Creating and updating the milestone tracking issue (For example https://github.com/dapr/dapr/issues/4898) with the proposed delivery dates.
- [ ] Coordinating with maintainers to create milestones in each repo.
- [ ] Schedule and run the weekly release meetings for each phase.
- [ ] Communicating status to the community on an on-going basis.


[
- Read about the K8s release team selection [here](https://github.com/kubernetes/sig-release/blob/master/release-team/release-team-selection.md#selection-criteria)]

## Feature definition phase (~2 weeks)
With ongoing feature definition, some set of issues will bubble up as targeting a given release. In this phase, a set of feature proposals and significant design changes to existing features are reviewed where contributors are able to dedicate time to completing the issue or starting an issue for a future release. 

For a feature to be considered for implementation it must have a feature proposal issue, tagged appropriately. The proposal must include;
- [ ] A design in an implementable state that has design reviewed and commented by approvers/maintainers
- [ ] A test plan
- [ ] A linked open issue for the current milestone

Maintainers are responsible for triaging issues into the milestone in this phase.

### Communication & meetings
During this phase there is a community meeting each week to discuss feature proposals and issues that different users would like to see in this release. This is to enable discussions on issues raised on Discord especially on priorities and scenarios. It is not intended for deep design discussion, which should be held separately and updated into the proposal.

The Discord channel called “proposal & issue discussion” is used to discuss feature proposals and issues.

During this phase the release lead is responsible for: 
- [ ] Posting on the Discord “announcements” and “proposal & issue discussion” channels the start of the milestone and the feature definition phase 
- [ ] Schedules the weekly release discussion meetings

   
### Feature definition phase checklist
At the conclusion of this phase, the release lead, working with maintainers and contributors, is responsible for;

**Adding to the milestone tracking issue;**
  - [ ] Any notes on specific goals for the release (for example focus on completing SDK APIs)
  - [ ] The list of milestone issues for feature proposals and significant design changes to existing features
  - [ ] The list of milestones projects for each repo.
  - [ ] Will any preview features be made stable in this release? (requires all SDKs to have implementation)
  - [ ] Will alpha APIs be made stable in this release?
- [ ] Each repo must have been triaged by the maintainers during this phase and all the intended work has been tagged with the milestone, a priority and assigned to owners were possible. 
- [ ] Each maintainer acknowledges this to the release lead.
- [ ] Communicating the final decisions for this release on Discord channels. 
   
## Feature implementation and bug fixing (~9 weeks)
This is the feature implementation and bug fixing phase and culminates in a code freeze period. 
During this phase maintainers and approvers do continuous triages on their repos assigning or removing issues from the milestone and communicating any decisions that may affect other repos. It is recommended to triage on Monday’s before the Tuesday release meeting.

### Communication & meetings
The release lead schedules weekly meetings

- [ ] Every Tuesday at 9 a.m. PST, one-hour release meetings are held. These meetings are led by the release lead and release lead shadow and cover the following topics.
 

| Topic    | Description |         Owner    |
| :----------- | :----------- | :----------- |
| Feature and issue update | Review any progress, risks or blockers on each feature | Feature owners |
| Long-haul   | Review current long hauls test status and updates  | Long-haul test lead  |
| Performance  | Review current performance test status and updates  | Performance test lead |   
|Issues/PRs related to release |Opportunity for maintainers to raise and discuss specific issues/PRs related to the release based on their triage. This is on a per repo basis. | Maintainers  |
|Milestone progress | Review code freeze and release date based on progress and priorities. The release lead has the responsibility of altering any dates. Decide on moving any PRs |Release lead and maintainers|
   

- [ ] **TBD** Every Thursday at 9am PST, one-hour feature proposal design meetings are held. These are opportunities for feature owners to discuss design decisions with the community that are then updated into the proposals.

### Removal of items from the milestone
Members of the release team may remove issues from the milestone if the maintainers determine that the issue is not actually blocking the release and is unlikely to be resolved in a timely fashion.
Members of the release team may remove PRs from the milestone for any of the following, or similar, reasons:
- PR is potentially destabilizing and is not needed to resolve a blocking issue.
- PR is a new, late feature PR and has not gone through the feature process 
- There is no responsible contributor willing to take ownership of the PR and resolve any follow-up issues with it
- PR is not correctly labeled
- Work has visibly halted on the PR and delivery dates are uncertain or late
   
### Code Freeze (~week 9)
After code freeze, only critical bug fixes are accepted into the release codebase.  

All features going into the release must be code-complete, including tests, and have docs PRs open. The docs PRs don't have to be ready to merge, but it should be clear what the topic will be and an owner is assigned. It’s incredibly important that documentation work gets completed as quickly as possible.

There are approximately two weeks following Code Freeze, and preceding release, during which all remaining critical issues must be resolved before release. This also gives time for documentation finalization.

At code freeze the release lead is responsible for;
- [ ] Announcing on the Discord “announcements” channel the code freeze. 
- [ ] Create an endgame issue task list, copied from the previous endgame milestone. For example https://github.com/dapr/dapr/issues/4814
- [ ] Assigns a release manager for the release
- [ ] Schedules daily 1 hour release meetings for the following 2 weeks at 9 a.m. PST.
- [ ] Tells maintainers to create repo specific endgame issues (if needed)

## Stabilization and release (~ 2 weeks)
This is the endgame phase of the release. The release lead manages this through the endgame task list. At the first daily release meeting, people are assigned to each of the endgame release tasks. 

RC builds are created by the release manager.

The final build is published when all endgame issues are signed off.

### Communication & meetings
- [ ] The release lead schedules daily meetings
- [ ] Each RC build is announced on the “announcements” channel to inform the community for validation testing.

## Post Release
Within 3 days of the release, the release lead and release shadow are responsible for;
- [ ] Facilitating a 1-hour community meeting to evaluate the release. This discussion should cover:
   - [ ] What worked well for this release.
   - [ ] What could be improved for the next release.
- [ ] Update the release documentation and processes to capture improvements.  

## Patch Releases (hot fixes)
Patch releases are described here. https://docs.dapr.io/operations/support/support-release-policy/

The release team for a given release remains on point for all future patch releases for that release. If a patch is needed the release lead;
- [ ] Creates a hotfix checklist list issue and assigns owners to tasks. For example https://github.com/dapr/dapr/issues/4995
- [ ] Assigns a contributor(s) to fix the issue(s).
- [ ] The release manager is responsible for releasing the patch.
- [ ] Announcing on the Discord “announcements” channel the patch availability. 

