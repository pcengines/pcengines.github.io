---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.16.0.4"
date:   2022-05-27
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.16.0.4

## Key changes

Mainline:

### Changed

- **Rebased** with official coreboot repository **commit** 9686ac2261

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/zqRSB8Tj6Dcan2r/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 9686ac2261 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`117 files changed, 4097 insertions(+), 217 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/nynFwrwrqLqeSrN/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/4bnRHPXn8GH7gZA/preview)

* Mainline:
  * PASSED: **692** (+0)
  * FAILED: **12** (+0)
  * PASSED [%]: **98.30** (+0.00%)

Fails are related to
[wakeonlan](https://github.com/pcengines/apu2-documentation/issues/282),
[USB](https://github.com/pcengines/apu2-documentation/issues/277) and
[Xen](https://github.com/pcengines/apu2-documentation/issues/109).

## Binaries

### Mainline

* [apu1 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.4.zip)

  [apu1 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.4.SHA256.sig)

* [apu2 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.4.zip)

  [apu2 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.4.SHA256.sig)

* [apu3 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.4.zip)

  [apu3 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.4.SHA256.sig)

* [apu4 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.4.zip)

  [apu4 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.4.SHA256.sig)

* [apu5 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.4.zip)

  [apu5 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.4.SHA256.sig)

* [apu6 v4.16.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.4.zip)

  [apu6 v4.16.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.4.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/475909)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.16.0.4.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
