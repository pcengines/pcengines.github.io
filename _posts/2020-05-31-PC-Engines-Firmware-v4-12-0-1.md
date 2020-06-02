---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.1"
date:   2020-05-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.1

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 8952d1c.
2. **Fixed** [random coreboot hangs on apu1](https://github.com/pcengines/coreboot/issues/394).
3. **Fixed** [AGESA assertion errors on apu1](https://github.com/pcengines/coreboot/issues/397).
4. We tried to look into **USB 3.0 link calibration setting** to find possible
   **workarounds for issues with USB 3.0 sticks detection**. However, modifying
   any of them had **no impact on the detection rate**. Further investigation
   in progress.
5. **Changed Memtest86plus revision** to newer commit
   0b756257276729c1a12bc1d95e7a1f044894bda2 that support both apu1 and apu2
   platforms. Previous revisions had problem with SMBus interface and SPD
   retrieval.
6. With the new release of coreboot 4.12 **3mdeb has a new key used for signing
   release images**: [PC Engines Open Source Firmware Release 4.12 Signing Key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/pcengines/release-keys/pcengines-open-source-firmware-release-4.12-key.asc).
   Remember to import it to your GPG (or other key management software) before
   signature verification

## coreboot community

Patches merged by community:

* [mb/pcengines/apu1/platform_cfg.h: Unset UsbRxMode to avoid platform reset issue](https://review.coreboot.org/c/coreboot/+/41627)

**Total:**

* 14 lines added,
* 0 lines removed,

in official coreboot repository.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/CYFjZBmYx6zZ6Pw/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 8952d1c ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`94 files changed, 3283 insertions(+), 381 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/9SSoC6BFBMdfy7t/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. 

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes slightly increased, because we did not yet upstream all
fixes for apu1.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/LMfrmjTgXc9tdxR/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/45snkiHepeJDTKf/preview)


* Mainline:
  * PASSED: **443** (+7)
  * FAILED: **9** (-6)
  * PASSED [%]: **98.23** (+1.33%)


No particular changes in tests in this release. Regression didn't detect new
bugs. Increased pass ratio has been caused by avoiding [USB detection bug](https://github.com/pcengines/coreboot/issues/264)

## Binaries

### Mainline

* [apu1 v4.12.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.1.zip)

  [apu1 v4.12.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.1.SHA256.sig)

* [apu2 v4.12.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.1.zip)

  [apu2 v4.12.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.1.SHA256.sig)

* [apu3 v4.12.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.1.zip)

  [apu3 v4.12.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.1.SHA256.sig)

* [apu4 v4.12.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.1.zip)

  [apu4 v4.12.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.1.SHA256.sig)

* [apu5 v4.12.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.1.zip)

  [apu5 v4.12.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/335785)

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **VERIFICATION**

3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.

   **VERIFICATION**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.
