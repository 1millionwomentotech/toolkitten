# 1 Million Women To Tech #SummerOfCode

## Week 12 GitHub - A gentle introduction to collaboration using GitHub

## Day 4

## Diffing. The hard part.

When a given file differs between two version we will get merge conflicts. These have to be resolved before we can make a commit.

Today we will be diving into the differences or diffing the two versions.

We can resolve the conflicts on file level, or a line level.

On the file level, you can choose either `theirs` or `yours` and commit that. The other one will be discarded. It's not a problem however, because that version will still exist in the previous snapshot (commit).

Sometimes you want to accept some parts of theirs, and keep some of yours. This can be done by `hunks`.

Once you are happy with the resulting version, commit it, and if you were pulling or merging there will also be a merge completion.

## Workflow

That’s all there is to it. The fundamentals are:
1. Fork the project & clone locally.
2. Create an upstream remote and sync your local copy before you branch.
3. Branch for each separate piece of work.
4. Do the work, write good commit messages, and read the CONTRIBUTING file if there is one. - I recommend to commit every 15 minutes. Then use `git squash` when you are ready to push.
5. Push to your origin repository.
6. Create a new PR in GitHub.
7. Respond to any code review feedback.

If you want to contribute to an open source project, the best one to pick is one that you are using yourself. The maintainers will appreciate it!
