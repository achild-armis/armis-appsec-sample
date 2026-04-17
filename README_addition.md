## Additional vulnerable sample files

This repo now includes a small multi-language sample pack intended to exercise AppSec detections across less common ecosystems.

### Included files

| File | Language | Classification |
|---|---|---|
| `samples/perl/sample-vuln.pl` | Perl | `command_injection` |
| `samples/java/SamplePathTraversal.java` | Java | `path_traversal` |
| `samples/cobol/sample_vuln.cob` | COBOL | `hardcoded_secret_exposure` |
| `samples/raku/sample_vuln.raku` | Raku | `xss` |
| `samples/nim/sample_vuln.nim` | Nim | `sql_injection` |

### Purpose

These files are intentionally vulnerable and are included only for testing, demo, and detection-validation purposes.

### Notes

- The examples are small by design so detections are easy to explain in demos.
- Each file maps to one of the platform classification labels shown in product screenshots and collateral.
- The code should not be reused in production systems.
