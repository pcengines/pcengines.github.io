---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.8"
date:   2019-08-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.8

## Key changes

Mainline:

### Changed

- **Rebased** with official coreboot repository **commit** df721bd

## Statistics


![Files Changed]( LINK-HERE )

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat df721bd ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`117 files changed, 4246 insertions(+), 219 deletions(-)`

![Process of mainlining]( LINK-HERE )

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix]( LINK-HERE ) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results]( LINK-HERE ) -
  please note there are separate sheets for each board-release.

![Mainline test results]( LINK-HERE )

* Mainline:
  * PASSED: TODO
  * FAILED: TODO
  * PASSED [%]: TODO

Fails are related to
TODO

## Binaries

### Mainline