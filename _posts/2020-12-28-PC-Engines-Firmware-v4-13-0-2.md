---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.13.0.2"
date:   2020-12-28
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.13.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 8edb48b.
2. **Fixed** [serial number calculation on APU1](https://github.com/pcengines/coreboot/issues/436). Before, APUs1 had serial number incorrectly set to -64. Now, the serial number is correctly calculated from the MAC address of the first NIC as shown [here](https://www.pcengines.ch/ht_macid.htm).

## coreboot community

Patches merged by community:

* [util/cbfstool/fit.c: Add support for adding Boot Guard manifests](https://review.coreboot.org/c/coreboot/+/48469)

**Total:**

* 45 lines added,
* 2 lines removed,

in official coreboot repository.

## Statistics

```
git diff --stat 8edb48b ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`106 files changed, 4328 insertions(+), 422 deletions(-)`


## Testing


## Binaries

### Mainline

* [apu1 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.2.zip)

  [apu1 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.2.SHA256.sig)

* [apu2 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.2.zip)

  [apu2 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.2.SHA256.sig)

* [apu3 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.2.zip)

  [apu3 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.2.SHA256.sig)

* [apu4 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.2.zip)

  [apu4 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.2.SHA256.sig)

* [apu5 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.2.zip)

  [apu5 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.2.SHA256.sig)

* [apu6 v4.13.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.2.zip)

  [apu6 v4.13.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.2.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/376207)

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
