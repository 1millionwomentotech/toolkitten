# 1 Million Women To Tech 

## Week 12 GitHub - A gentle introduction to collaboration using GitHub

Has this ever happened to you? Trying to use Git but not so clear on how to learn?

In the words of a GitHub Labs learner:

> I have been trying to learn Git + GitHub to start teaching at the school. Without understanding the correct use, and potential problems that we could face when using this technology I am not so confident to do it.
> Yet, I have finished the Udacity course, a course with a campus expert, and again and again the problem is the nature of the examples. At some point, they lose attention to the learning curve and start using complex examples that does not make any sense at all, thus the problem is not about using GitHub but to figure out where an error or diff is present.

Therefore this week we will go through every click, every screen, from the moment of signing up for a GitHub account to setting up our Git software, to contributing regularly. I will be demoing using the following:
- Mac
- GitHub account
- iTerm2
- git (comes with XCode)
- gitKraken

## Setup

1. Sign up for a GitHub account
2. Install gitKraken
3. Make sure you have git installed on your machine

## Workflow

That’s all there is to it. The fundamentals are:
1. Fork the project & clone locally.
2. Create an upstream remote and sync your local copy before you branch.
3. Branch for each separate piece of work.
4. Do the work, write good commit messages, and read the CONTRIBUTING file if there is one.
5. Push to your origin repository.
6. Create a new PR in GitHub.
7. Respond to any code review feedback.

If you want to contribute to an open source project, the best one to pick is one that you are using yourself. The maintainers will appreciate it!

## Day 1

### How to Write Good Commit Messages

A commit message consists of 3 parts:
- shortlog
- commit body
- issue reference

Usually the Git book is referenced: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project but I prefer Angular style where you DON'T capitalize.

Angular's commit message conventions are nice and detailed: 
- https://gist.github.com/stephenparish/9941e89d80e2bc58a153

Contribution guidelines include a bot to sign license agreement:
- https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-signing-the-cla

React's are not
- https://reactjs.org/docs/how-to-contribute.html

### 1MWTT Contribution Guidelines

- [contribution guidelines](../../howto/contribute.md)

### Core workflow

Pull. Push. Repeat.

![Git in a nutshell](./git-fork-clone-flow.png)

Clone
Commit changes
Push changes
Pull changes
Handle merge conflicts

Inspired by: 
- https://akrabat.com/
- https://chris.beams.io/posts/git-commit/
- referenced by The Git Book: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.htmlthe-beginners-guide-to-contributing-to-a-github-project/

### GitHub Learning Lab

https://lab.github.com/
https://lab.github.com/githubtraining/introduction-to-github


## Day 2

Notifications
- turn off

Issues
- creating
- commenting
- referencing

### Core Workflow

Pull. Merge. Push. Repeat.

## Day 3

### Never rebase

I'm opinionated. Deal with it.

### Core Workflow

Pull. Resolve. Merge. Push. Repeat.

## Day 4

Diffing. The hard part.

### Core Workflow

Pull. Push. Repeat.

## Where to go from here

### Semantic versioning

It sounds fancier than it is.
