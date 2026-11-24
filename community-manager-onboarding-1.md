## Community Manager Onboarding (for maintainers)

These are actions that need to be performed by a Dapr project maintainer to give access to a new community manager.

The following information is needed from the new community manager:

- Full name
- Company name
- Email address
- GitHub username
- Discord username

### Update the Dapr Maintainers & Community Managers doc

Add the community manager to the [_Dapr Maintainers & Community Managers_ document](https://docs.google.com/document/d/1FRTKgEih_lWlTM5e5ZeTSwPxIwvWyWZhtWr8KCx8CXo) on the Dapr Google Drive.

### Update the Maintainers.md

Add the community manager to the [MAINTAINERS.md](MAINTAINERS.md) file.

The format should be:

```
<First name> <Last name> (<Company>) <GitHub username> (non voting)
```

### Update the Dapr maintainers.yaml

In order to get access to the CNCF service desk and receive emails from CNCF, two actions need to be done:

1. The community manager needs to be added to [maintainers.yaml](https://github.com/dapr/.project/blob/main/maintainers.yaml) in the _dapr/.project_ repository.

    - Create a PR that adds the community manager's GitHub username to the `project-maintainers` team in that file.

    CNCF automation syncs this file into the CNCF maintainer list, so there is no PR to make against the _cncf/foundation_ repository.

    The community manager's name, email address and company come from their LFID profile, so ask them to link their GitHub handle on [openprofile.dev](https://openprofile.dev).

2. Create a ticket at the [CNCF Service Desk](https://cncfservicedesk.atlassian.net/servicedesk/customer/portals), select the Program Management category and submit the name and email of the new community manager.

### 1Password

The community manager requires access to the Community Outreach vault in 1Password.

- Send an invite to the new Community Manager to join the Dapr 1Password account:
  - In the 1Password menu go to Invitations -> Invite by email.

### GitHub access

The community manager requires maintainer access to the [community](https://github.com/dapr/community) and [blog](https://github.com/dapr/blog) repositories.

Add the community manager to these Dapr org teams on GitHub:

- maintainers-community
- maintainers-blog

The community manager is mostly likely not a member of the Dapr org on GitHub. By adding them to the above org teams they will receive an invite to join the Dapr org.

### Discord

The community manager requires access to perform management and moderation tasks on the Dapr Discord server.

- [Invite](https://bit.ly/dapr-discord) the community manager to the Dapr Discord server.
- Add the community manager to the _Community Manager_, _release observers_, and _maintainers_ roles on Discord:

  - In Discord go to Server Settings -> Roles -> [Role] ->  Manage Members -> Add Member.

- Add the community manager to the _Community Sync_ DM group on Discord.
