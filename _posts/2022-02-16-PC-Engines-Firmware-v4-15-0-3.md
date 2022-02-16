---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.15.0.3"
date:   2022-02-16
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.15.0.3

## Key changes

Mainline:

### Changed
- **Rebased** with official coreboot repository **commit** 36425312ee
- **Added checking** hardware matrix before regression tests
- Fixed the **hard disk** not **visible** in the Seabios Boot Menu

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/Jdqko3waRfydFbC/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 36425312ee ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`112 files changed, 4069 insertions(+), 213 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/mDP5AaXCP5aBFRc/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.
##### FIXME!!!!!!!!!!
![Mainline test results](https://cloud.3mdeb.com/index.php/s/4TM24EyBWPJxHjK/preview)
##### FIXME!!!!!!!!!!
* Mainline:
  * PASSED: **687** (-5)
  * FAILED: **16** (+5)
  * PASSED [%]: **97.72** (-0.72%)
##### FIXME!!!!!!!!!!
Fails are related to wakeonlan, USB and Xen.

## Binaries

### Mainline

* [apu1 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.3.zip)

  [apu1 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.3.SHA256.sig)

* [apu2 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.3.zip)

  [apu2 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.3.SHA256.sig)

* [apu3 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.3.zip)

  [apu3 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.3.SHA256.sig)

* [apu4 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.3.zip)

  [apu4 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.3.SHA256.sig)

* [apu5 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.3.zip)

  [apu5 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.3.SHA256.sig)

* [apu6 v4.15.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.3.zip)

  [apu6 v4.15.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/452881)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.15.0.3.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
