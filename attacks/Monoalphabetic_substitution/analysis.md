## Cryptanalysis Decision Table

| Step | Observation | Possible Substitution | Substitution Tested | Result | Decision |
|---|---|---|---|---|---|
| 1 | Most frequent ciphertext symbol was `O` | `O → E` | Candidate mapping inferred from frequency analysis | Partial plaintext became more meaningful | Accepted |
| 2 | Repeated three-letter word `FMO` appeared 20 times | `FMO → THE` | `F → T`, `M → H`, `O → E` | Common English word pattern identified | Accepted |
| 3 | Repeated two-letter word `LY` appeared 11 times | `LY → IN` | `L → I`, `Y → N` | Recognizable word fragment appeared | Accepted |
| 4 | Repeated two-letter word `UW` appeared 10 times | `UW → OF` | `U → O`, `W → F` | Partial plaintext improved | Accepted |
| 5 | Pattern `VLZZ → 0122` suggested a word such as `WILL` | `VLZZ → WILL` | `V → W`, `L → I`, `Z → L` | Repeated-letter word became readable | Accepted |
| 6 | Remaining letters were resolved using frequency and word-pattern analysis | Remaining mappings | Full substitution key | Complete plaintext recovered | Accepted |
| 7 | Recovered plaintext was encrypted again | Recovered key | Full key applied | Ciphertext matched the original | Verified |

### Recovered Key

```text
JGATOWHMLBQZCYUDKNPFREVXIS