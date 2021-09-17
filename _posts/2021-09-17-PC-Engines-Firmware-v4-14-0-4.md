---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.14.0.4"
date:   2021-09-17
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.14.0.4

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** d9f5d90.
1. Enabled EHCI controller by default on apu3-apu6 platforms
1. Updated sortbootorder to v4.6.22
1. Added safeguard against setting too low watchdog timeout

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/2CkEG3SkBkFoqLD/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat d9f5d90 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`111 files changed, 4263 insertions(+), 341 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/5g8G9WsAGejRA5P/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/6fwW8oPdDGKwW7A/preview)

* Mainline:
  * PASSED: **686** (+22)
  * FAILED: **20** (-1)
  * PASSED [%]: **97.17** (+0.23%)

Detected regression in wakeonlan. Other fails re related to USB and Xen.

### Key Changes in testing

* bumped Debian stable version to Debian 11 which fixes installation of Debian
  on previously failing platforms

## Binaries

### Mainline

* [apu1 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.4.zip)

  [apu1 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.4.SHA256.sig)

* [apu2 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.4.zip)

  [apu2 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.4.SHA256.sig)

* [apu3 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.4.zip)

  [apu3 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.4.SHA256.sig)

* [apu4 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.4.zip)

  [apu4 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.4.SHA256.sig)

* [apu5 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.4.zip)

  [apu5 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.4.SHA256.sig)

* [apu6 v4.14.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.4.zip)

  [apu6 v4.14.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.4.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/417462)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.14.0.4.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
