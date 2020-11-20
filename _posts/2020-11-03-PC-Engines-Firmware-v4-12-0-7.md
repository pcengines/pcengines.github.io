---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.7"
date:   2020-11-27
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.7

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 957a363.

## coreboot community

Patches merged by community:

* [cpu/intel/model_206ax: Get CPU frequencies for SMBIOS type 4](https://review.coreboot.org/c/coreboot/+/47058)

**Total:**

* 20 lines added,
* 0 lines removed,

## Statistics

```
git diff --stat 957a363 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`119 files changed, 4520 insertions(+), 574 deletions(-)`

## Testing

## Binaries

### Mainline

* [apu1 v4.12.0.7.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.7.zip)

  [apu1 v4.12.0.7.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.7.SHA256.sig)

* [apu2 v4.12.0.7.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.7.zip)

  [apu2 v4.12.0.7.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.7.SHA256.sig)

* [apu3 v4.12.0.7.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.7.zip)

  [apu3 v4.12.0.7.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.7.SHA256.sig)

* [apu4 v4.12.0.7.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.7.zip)

  [apu4 v4.12.0.7.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.7.SHA256.sig)

* [apu5 v4.12.0.7.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.7.zip)

  [apu5 v4.12.0.7.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.7.SHA256.sig)

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
