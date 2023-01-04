# Dapr administrators

## Charter

Administrators have access to credentials equivalent to members of the steering and technical commitee (STC) and are responsible to perform pre-approved routine maintenance duties and ad-hoc tasks delegated by the STC without making isolated decisions. This document outlines a list of pre-approved duties and some that require STC approval - when in doubt, the administrator should seek guidance from one STC member.

### Pre-approved duties

An administrator might perform the following duties without requiring approval from any STC member:

* Rotate credentials to services currently enrolled
* Update credentials on GitHub
* Rerun failed test runs
* Provision cloud resources to existing enrolled cloud providers
* Fix operational issues with existing services the project depends on (GitHub Actions, FOSSA, etc)
* Force merge a pull request upon request by repository's maintainer

### Duties that require STC approval

* Add or remove approvers, maintainers or administrators
* Create, graduate or archive projects in [dapr-sandbox](https://github.com/dapr-sandbox)
* Sign up to a new (free or paid) service, cloud provider or a service results in creating new credentials

## Process to become an administrator

0. As a pre-requisite, an administrator candidate **must first become a maintainer** of at least one repository in [Dapr](https://github.com/dapr). Being a maintainer in [dapr-sandbox](https://github.com/dapr-sandbox) does not qualify.

1. Then self-nominate via a [new issue in the community repository](https://github.com/dapr/community/issues/new) stating which repositories you currently maintain and the reasons why you want to be an administrator.

2. In addition, candidate should add a link to the new issue asking it to be voted in the next STC meeting. Agenda for STC meetings are discussed in [issues in the Community repository](https://github.com/dapr/community/issues). Alternatively, candidate can request one STC member to seek approval via e-mail instead of waiting for the next STC meeting.

3. Finally, a maintainer will become an administrator after STC approves the request with a 3/5 majority.

## Limits and Expiration

The administrator role expires 6 months from the date it was approved. The process for renewal is the same as to become an administrator in the first place.

To minimize the number of people with access to shared credentials, there can only be 3 active or suspended administrators. Adding one more requires the STC to remove another.

## Removal

The administrator role is permanently removed in case any of the following:
* Expiration of the 6 months term as administrator
* Administrator is no longer a maintainer in Dapr
* STC votes with 3/5 majority to remove administrator
* Administrator joins as an STC member

## Suspension

In order to de-risk potential misuse of power or suspicion of leaked credentials, at any moment, any STC member can temporarily suspend administrator role from any individual - revoking all prioviledge access - for any reason, without requiring an STC meeting. Reinstating administrator role requires the same process as becoming one in the first place.

## Current Administrators

| Name | Handle | Company | Status | Timezone | Term Start | Term End |
| - | - | -  | - | - | - | -

### Statuses
   * Active: has full access and can perform administrator duties.
   * Suspended: holds an administrator position but access has been temporarily revoked.