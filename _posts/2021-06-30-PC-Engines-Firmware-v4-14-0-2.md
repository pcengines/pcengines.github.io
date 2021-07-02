---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.14.0.2"
date:   2021-06-30
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.14.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 1c43d92.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/xMsKHiN8ES8asDr/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 1c43d92 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`110 files changed, 4202 insertions(+), 340 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/TTCmsDkey6Q4yLN/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/4n9rT4yMsKezHsR/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/KJE4bWzQBok47rP/preview)

* Mainline:
  * PASSED: **686** (+7)
  * FAILED: **18** (+0)
  * PASSED [%]: **97.44** (+0,02%)

Debian network installers have problems to install themselves on apu4 and apu6
when a preseed file is passed for unattended installation. Manual installation
doesn't show these problems. Issue is still under investigation.

### Key Changes in testing

* Fixed the Debian installation tests by correcting the preseed files.
* Added test for iPXE HTTPS support.
* Corrected tests for UART C/D enabling after changes in the firmware.
* Corrected IOMMU test configuration on apu3 and apu4.
* Corrected command execution in iPXE which was generating many false negative
  test results.
* Increased timeouts when verifying checkpoints in OS installation. Some
  storage drives are slower and need more time for certain installation phases.
* Fixed the paths to control GPIOs under Linux system on other platforms than
  apu2.
* Fixed the description of SD cards behind USB bridge that cause incorrect
  qualification for SD performance tests on apu1 and apu5.
* Fixed IOMMU not being enabled during Xen IOMMU test.
* Improved reliability sign of life checks using regexps.
* Improved extraction of SeaBIOS boot menu entries.
* Corrected power cycling routines.
* Fixed sending keys containing escape sequences to iPXE which caused the
  sequences to break and send unwanted characters to serial console.
* Added additional checks for command failures in MBR deletion and wakeonlan.
* Fixed the SPI write protection being accidentally set without block
  protection.
* Improved the reliability of the serial enable/disable with S1 button.

## Binaries

### Mainline

* [apu1 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.zip)

  [apu1 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.SHA256.sig)

* [apu2 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.zip)

  [apu2 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.SHA256.sig)

* [apu3 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.zip)

  [apu3 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.SHA256.sig)

* [apu4 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.zip)

  [apu4 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.SHA256.sig)

* [apu5 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.zip)

  [apu5 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.SHA256.sig)

* [apu6 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.zip)

  [apu6 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/417462)

**IMPORTANT**

To update the firmware and keep the runtime configuration unchanged please
use the following command:

```
flashrom -p internal -w apuX_v4.14.0.2.rom --fmap -i COREBOOT
```

The persistent runtime configuration works only when migrating from versions
v4.14.0.1 and later. The feature is not yet supported on apu1. Flashrom version
needs to be v1.1 or newer.
