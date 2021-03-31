---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.13.0.5"
date:   2021-04-02
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.13.0.5

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** e7a68ec.

## Statistics


```
git diff --stat e7a68ec ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`106 files changed, 4422 insertions(+), 404 deletions(-)`

## Testing

### Key Changes in testing

## Binaries

### Mainline

* [apu1 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.5.zip)

  [apu1 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.5.SHA256.sig)

* [apu2 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.5.zip)

  [apu2 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.5.SHA256.sig)

* [apu3 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.5.zip)

  [apu3 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.5.SHA256.sig)

* [apu4 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.5.zip)

  [apu4 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.5.SHA256.sig)

* [apu5 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.5.zip)

  [apu5 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.5.SHA256.sig)

* [apu6 v4.13.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.5.zip)

  [apu6 v4.13.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.5.SHA256.sig)

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

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
