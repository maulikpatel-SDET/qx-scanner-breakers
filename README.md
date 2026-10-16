# qx-scanner-breakers  

Adversarial repo. Goal: make the scanner give a WRONG answer, crash, hang, or be fooled.
These go past "does it detect X" into resilience and trust: parser edge cases, misattribution,
wrong-data traps, resource pressure and confusable paths. For each file the EXPECTED result is
in the test sheet; many 'passes' mean "did NOT break and reported the real algorithm".
ALL KEYS ARE TEST KEYS. Nothing here is malicious; it only stresses a static scanner.
