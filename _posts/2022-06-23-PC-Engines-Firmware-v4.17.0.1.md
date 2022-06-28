---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.17.0.1"
date:   2022-05-27
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.17.0.1

## Key changes

Mainline:

### Added

- Support for APU7 (APU3 variant with 2.5GbE i225 NICs)

### Changed

- **Rebased** with official coreboot repository **commit** 5eda52a
- **Updated sortbootorder** to **v4.6.24** adding support for APU7

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/NFcsWDEGYde6anA/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 5eda52a ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`116 files changed, 4237 insertions(+), 217 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/6yR5a3sTC8Xot5W/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/GYecq2SHidoFZ8A/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/qSxoPobkE46JFib/preview)

* Mainline:
  * PASSED: **754** (+62)
  * FAILED: **12** (+0)
  * PASSED [%]: **98.43** (+0.13%)

Fails are related to
[wakeonlan](https://github.com/pcengines/apu2-documentation/issues/282),
[USB](https://github.com/pcengines/apu2-documentation/issues/277) and
[Xen](https://github.com/pcengines/apu2-documentation/issues/109).

## Binaries

### Mainline

* [apu1 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.1.zip)

  [apu1 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.1.SHA256.sig)

* [apu2 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.1.zip)

  [apu2 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.1.SHA256.sig)

* [apu3 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.1.zip)

  [apu3 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.1.SHA256.sig)

* [apu4 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.1.zip)

  [apu4 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.1.SHA256.sig)

* [apu5 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.1.zip)

  [apu5 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.1.SHA256.sig)

* [apu6 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.1.zip)

  [apu6 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.1.SHA256.sig)

* [apu7 v4.17.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.1.zip)

  [apu7 v4.17.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/475909)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.17.0.1.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
