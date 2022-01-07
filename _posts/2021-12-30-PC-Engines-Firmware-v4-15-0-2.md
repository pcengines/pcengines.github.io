---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.15.0.2"
date:   2021-12-30
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.15.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 3990da0b.
2. Disabled SMM
3. Enabled parallel AP initialization for apu2-6 for **faster boot time**
4. Added **documentation** about **[runtime configuration](https://github.com/pcengines/apu2-documentation/blob/master/docs/runtime-configuration.md)**.
   It is now possible to **change the coreboot options from operating system**
   using flashrom and [cb-order](https://github.com/pcengines/cb-order).

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/eYnrfg3wKrJHbkg/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 3990da0b ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`110 files changed, 4051 insertions(+), 213 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/pnK29P7G4d6AG3d/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/4TM24EyBWPJxHjK/preview)

* Mainline:
  * PASSED: **687** (-5)
  * FAILED: **16** (+5)
  * PASSED [%]: **97.72** (-0.72%)

Fails are related to wakeonlan, USB and Xen.
A regression related to SATA detection on coldboot has been detected. If you
encounter this issue, it's recommended to roll back to version v4.14.0.6.

## Binaries

### Mainline

* [apu1 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.2.zip)

  [apu1 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.15.0.2.SHA256.sig)

* [apu2 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.2.zip)

  [apu2 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.15.0.2.SHA256.sig)

* [apu3 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.2.zip)

  [apu3 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.15.0.2.SHA256.sig)

* [apu4 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.2.zip)

  [apu4 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.15.0.2.SHA256.sig)

* [apu5 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.2.zip)

  [apu5 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.15.0.2.SHA256.sig)

* [apu6 v4.15.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.2.zip)

  [apu6 v4.15.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.15.0.2.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/452881)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.15.0.2.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
