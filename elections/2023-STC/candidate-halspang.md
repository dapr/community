-------------------------------------------------------------
name: Hal Spang
ID: halspang
info:
  - employer: Microsoft
  - discord: Pundil
-------------------------------------------------------------

#### Name
Hal Spang

#### Company Affiliation
Microsoft

#### Your work and/or contributions to Dapr
I have been working on the Dapr project since before the initial 1.0 release, starting at 0.11. Initially starting off with whatever was needed to help get Dapr to its first stable release, 
I transitioned to focus primarily on two main areas. 

First, being the actor space in general where I worked on bugs/issues across the space and added in the Reentrancy feature. This work included implementing/assisting in the implementation of Reentrancy across several SDKs. Following that, I also added in the ability to specify actor configuration on a per actor type basis.

Following my work on Actors, my next major transition was into the Resiliency space. Having worked on that from the design phase through to the implementation. 
This work touched almost all of the Dapr runtime as it applied to almost everything Dapr does (aside from some of the management that the control plane does).

Admist this, I was also working with the former .NET SDK maintainer to ramp-up and take over responsibilities there. I became an official maintainer in early 2022 and have continued to keep the SDK up to date with modern features as well as bringing in additional people to work on the SDK. The SDK is currently one of the most used SDKs.

Outside of the OSS world, I have also been working on how Dapr interacts with Azure. Working directly with various Azure teams to help make sure that the Dapr experience is good when using Azure infrastructure and helping to bring modern Dapr features to more users.

I have also long been active in the Discord, focusing primarily on helping people with questions in the .NET channel or anywhere else I may have some expertise.

#### Why you are running
To me, Dapr provides an important functionality in that it helps developers adhere to best practices without them having to think directly about it. From abstractions to security and resiliency, there is already a wide net that Dapr casts and I think that it can only get better from here. By providing these building blocks for developers, they can focus on their business logic without necessarily worrying about what the underlying infrastructure, security, or networking may be. This unlocks the broadest set of possibilities for them which will lead to an overall better experience.

Apart from Dapr's ability to provide a developer with these fundamentals, I also think that the high level functionality it provides are very attractive. By continuing to build off of what Dapr has already established, we can offer an advanced set of functionality with confidence due to the foundation set by Dapr. 

From the above, my focuses here for Dapr would be:
1. Driving fundamentals
   1. Enhancements to the actor subsystem
   1. Additional tests around performance/integrations
1. Higher level functionalities (what else can we build like workflows) and new APIs (blob/document store, etc)
1. Improvements to Resiliency (new features like rate limiting, fundamentals like dynamic loading)
1. Easing the developer onboarding process
   1. SDK consistency
   1. PaaS integrations
   1. Metrics and tracing improvements
