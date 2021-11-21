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

```console
 ✘ user@ubuntu  ~/workspaces/pre-commit-pdb-vars   main ✚  pre-commit run --all-files
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
mypy.....................................................................Passed
flake8...................................................................Passed
pdb-vars.................................................................Failed
- hook id: pdb-vars
- exit code: 1

Prohibited PDB Command name `q` at: /home/si/workspaces/pre-commit-pdb-vars/test_files/fail.py:1:0.
Prohibited PDB Command name `s` at: /home/si/workspaces/pre-commit-pdb-vars/test_files/fail.py:3:0.
Prohibited PDB Command name `enable` at: /home/si/workspaces/pre-commit-pdb-vars/test_files/fail.py:5:0.
Prohibited PDB Command function def `alias` at: /home/si/workspaces/pre-commit-pdb-vars/test_files/fail.py:8:0.
Prohibited PDB Command function def `disable` at: /home/si/workspaces/pre-commit-pdb-vars/test_files/fail.py:13:4.
```
