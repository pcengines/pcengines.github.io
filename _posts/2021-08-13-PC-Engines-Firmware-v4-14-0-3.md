---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.14.0.3"
date:   2021-08-13
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.14.0.3

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** c049c80.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/BFZsWbDyyCqyypQ/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat c049c80 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`110 files changed, 4256 insertions(+), 340 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/GeRboni6D9jNnqP/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/zYHKdEKjdgAgx9o/preview)

* Mainline:
  * PASSED: **664** (-22)
  * FAILED: **21** (+3)
  * PASSED [%]: **96.93** (−0.51%)

Debian network installers have problems to install themselves on apu4 and apu6.
Tests that depend on the successful installation of Debian have not been
conducted, which is why the PASS number is lower. Failures also occur around
the USB sticks.

### Key Changes in testing

## Binaries

### Mainline

* [apu1 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.3.zip)

  [apu1 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.3.SHA256.sig)

* [apu2 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.3.zip)

  [apu2 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.3.SHA256.sig)

* [apu3 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.3.zip)

  [apu3 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.3.SHA256.sig)

* [apu4 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.3.zip)

  [apu4 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.3.SHA256.sig)

* [apu5 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.3.zip)

  [apu5 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.3.SHA256.sig)

* [apu6 v4.14.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.3.zip)

  [apu6 v4.14.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/417462)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.14.0.3.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
