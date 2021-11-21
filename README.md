# pre-commit-pdb-vars
A pre-commit framework hook that prevents variable names matching pdb shortcuts

# How to use it:

```yaml
# Add to your .pre-commit-config.yaml
  - repo: https://github.com/symonk/pre-commit-pdb-vars.git
    rev: 0.2.0
    hooks:
      - id: pdb-vars
```

```shell
[INFO] This may take a few minutes...
black....................................................................Passed
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for case conflicts.................................................Passed
Check docstring is first.................................................Passed
Debug Statements (Python)................................................Passed
Detect Private Key.......................................................Passed
Fix requirements.txt.................................(no files to check)Skipped
isort....................................................................Passed
mypy.................................................(no files to check)Skipped
flake8...................................................................Passed
pdb-vars.................................................................Failed
- hook id: pdb-vars
- exit code: 1

Prohibited PDB Command variable `s` at: /home/si/workspaces/pre-commit-pdb-vars/foo.py:1

```
