---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.3"
date:   2020-07-29
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.3

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 8d5cedf.
2. **Fixed** memory speed values in the DMI table. Previous values were the 
speed of the bus not the memory thus it was 2 times smaller.
3. **Fixed** cbmem error caused by wrong ACPI table.
4. **Updated** sortbootorder to version 4.6.19 with an option in the runtime 
configuration allowing to reverse PCI addressing order. Previously, if a new PCI
device was added to the PCIe slot, all other devices' addresses were incremented, 
which could result in renaming the internet interfaces.

Legacy:
1. **Updated** sortbootorder to version 4.6.19 with an option in the runtime 
configuration allowing to reverse PCI addressing order. Previously, if a new PCI
device was added to the PCIe slot, all other devices' addresses were incremented, 
which could result in renaming the internet interfaces.

## coreboot community

Patches merged by community:

* [mb/protectli/vault_kbl: Enable Intel PTT](https://review.coreboot.org/c/coreboot/+/42565)


**Total:**

* 6 lines added

in official coreboot repository.

## Statistics


```
git diff --stat 8d5cedf ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`103 files changed, 4043 insertions(+), 422 deletions(-)`




## Testing




## Binaries

### Mainline

* [apu1 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.zip)

  [apu1 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.SHA256.sig)

* [apu2 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.zip)

  [apu2 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.SHA256.sig)

* [apu3 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.zip)

  [apu3 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.SHA256.sig)

* [apu4 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.zip)

  [apu4 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.SHA256.sig)

* [apu5 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.zip)

  [apu5 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.SHA256.sig)

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
