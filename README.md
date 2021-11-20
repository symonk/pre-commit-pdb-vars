# pre-commit-pdb-vars
A pre-commit framework hook that prevents variable names matching pdb shortcuts

# How to use it:

```yaml
# Add to your .pre-commit-config.yaml
  - repo: https://github.com/symonk/pre-commit-pdb-vars.git
    rev: 0.1.0
    hooks:
      - id: pdb-vars
```

```shell
isort....................................................................Passed
mypy.................................................(no files to check)Skipped
flake8...................................................................Passed
pdb-vars.................................................................Failed
- hook id: pdb-vars
- exit code: 1

Variable named: `s` mirrors a pdb command, rename it.

```
