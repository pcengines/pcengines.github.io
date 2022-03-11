---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.16.0.1"
date:   2022-03-08
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.16.0.1

## Key changes

Mainline:

### Changed
- **Rebased** with official coreboot repository **commit** b4ba289fa5
- Disabled **loglevel prefixes** introduced in coreboot 4.16
- Disabled **ANSI escape** sequences introduced in coreboot 4.16
- Fixed AMD PSP CCP as **entropy source**

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/HMo8NLf9CeHXpyF/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat b4ba289fa5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`114 files changed, 4102 insertions(+), 213 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/WamPXTwN9iYgpiw/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/TrwJQab8EZ7rfzF/preview)

* Mainline:
  * PASSED: **692** (-1)
  * FAILED: **12** (-1)
  * PASSED [%]: **98.30** (+0.15%)

Fails are related to *wakeonlan, *USB and *Xen.


## Binaries

### Mainline

* [apu1 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.1.zip)

  [apu1 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.16.0.1.SHA256.sig)

* [apu2 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.1.zip)

  [apu2 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.16.0.1.SHA256.sig)

* [apu3 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.1.zip)

  [apu3 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.16.0.1.SHA256.sig)

* [apu4 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.1.zip)

  [apu4 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.16.0.1.SHA256.sig)

* [apu5 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.1.zip)

  [apu5 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.16.0.1.SHA256.sig)

* [apu6 v4.16.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.1.zip)

  [apu6 v4.16.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.16.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/475909)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.16.0.1.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
