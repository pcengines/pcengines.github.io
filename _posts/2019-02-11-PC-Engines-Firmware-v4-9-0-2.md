---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.2"
date:   2019-02-11
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.2

## Key changes

Mainline:

1. **Enabled** CPB feature.
2. **Corrected AGESA headers**, which were for newer AGESA version than used in
   coreboot.
3. [Reproducible builds limiation](https://github.com/pcengines/coreboot/issues/267) -
   currently set **iPXE** and **Memtest86**+ master revisions do not guarantee
   the build reproducibility in long term. Correct revisions will be set in
   **v4.9.0.3**.
4. Performed an **analysis** how to **safely reboot** platform after firmware
   upgrade using available reset methods:
   https://github.com/pcengines/apu2-documentation/pull/131
   https://github.com/pcengines/apu2-documentation/pull/108
5. pcengines.github.io page has been **updated** with **newsletter**
   **subscription** option and a **blog** with release reports containing key
   changes, test statistics/charts etc.

Legacy:

1. **Enabled** CPB feature.
2. [Reproducible builds limiation](https://github.com/pcengines/coreboot/issues/267) -
   currently set **iPXE** and **Memtest86**+ master revisions do not guarantee
   the build reproducibility in long term. Correct revisions will be set in
   **v4.0.25**.

## Statistics

![Files Changed](https://gallery.mailchimp.com/fce95b885fc13fbf1db611816/images/3a8427b8-98dc-4316-883c-a28728f34d7c.png)

The chart shows the total files changed from release tag against the rebase point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml excluded from statistics). Check the statistics with:

```
git diff --stat <rebase_point_sha> ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

![Addition and Deletion](https://gallery.mailchimp.com/fce95b885fc13fbf1db611816/images/7d99ca25-985b-4839-a72e-76d7e3aaa4fc.png)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for given release. Check the statistics
with:

```
git diff --stat <rebase_point_sha> ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree. The difference has grown a little since some
patches have not yet been merged and/or sent (AGESA headers).

## coreboot community

Patches merged:

* [Enable LPC TPM on apu1](https://review.coreboot.org/c/coreboot/+/30354)

* [Enable CPB](https://review.coreboot.org/c/coreboot/+/31229)

## Testing

* [PC Engines hardware configuration matrix](https://3mdeb.com/wp-content/uploads/2019/02/3mdeb-lab-hw-matrix.png) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

* **Added** 2 new test-cases: Serial output redirection enable/disable.
* **Improved** network interface tests.
* **Improved** HUAWEI modem detection tests.
* **Fixed** OS installation tests for configs with WLE900VX modem.

![Mainline test results](https://gallery.mailchimp.com/fce95b885fc13fbf1db611816/images/fb10bb89-9625-4465-ae1d-206c86e367d3.png)

![Legacy test results](https://gallery.mailchimp.com/fce95b885fc13fbf1db611816/images/b41875ae-8b34-4e7f-ae29-5cf090cf2cbf.png)

We have updated some tests reults after re-testing, therefore some statistics
may not match with the information from the previous newsletter.

* Mainline:
  * PASSED: 306 (+12)
  * FAILED: 16 (-2)
  * PASSED [%]: 95,03% (+0.8%)
* Legacy:
  * PASSED: 286 (+10)
  * FAILED: 23 (0)
  * PASSED [%]: 92,56% (+0.25%)

## Binaries

### Mainline

* [apu1 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/XTGTbRnkQCMoGrK/download)

  SHA256: 21618e83de50e87eb6f0cacf95e6e62c8d8d453a82b0fbeffa0b6fde8eed0e6d

* [apu2 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/Yjx7PqAqFeQQCyC/download)

  SHA256: 4d64c5b7875b9877b4f149e0a0f082a614ae5572cfd7346b0c45d5378f887b75

* [apu3 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/Qf3oF4AqydiAxdr/download)

  SHA256: abc47e2c3db3e1e3189912076f9973771c184eb14397d85cea9067794d0fd8c7

* [apu4 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/4zg6LH2X9NM6wrL/download)

  SHA256: fa4f1c1763ec918457ba22e57c3ff8fb19fc32cd0634ac9d7472b612cea806ae

* [apu5 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/WsjAj6AQTDTByYH/download)
  
  SHA256: e31e952dfcb549f3144d30eb25b2bcb2ddaeb9ed89372d2e548c0d3902cf14c5

### Legacy

* [apu2 v4.0.24](https://cloud.3mdeb.com/index.php/s/MDSaP8CnWEQrKC3/download)

  SHA256: 43880c9566cbafca1874bb66dcc0444186a89c4a5408696b432f3fdf01e1b267

* [apu3v4.0.24](https://cloud.3mdeb.com/index.php/s/fBefFydWbMTaFHg/download)

  SHA256: f26f9744a12b971605bd9b954e8fc5252c4789d95d86e615bc3a0df66630d59d

* [apu4 v4.0.24](https://cloud.3mdeb.com/index.php/s/ef5jSRw3rfZgocJ/download)

  SHA256: 262dceb5408d6ba8f14477465adc5c0313bb85bdc0c1a8722f52c28b09f9aa05

* [apu5 v4.0.24](https://cloud.3mdeb.com/index.php/s/XRi7K2LDaJryqJF/download)

  SHA256: fadca94b5618b6e93a6f5b8f5ff96e8ff1128b7d5d117fa91dd941a4180a4557
