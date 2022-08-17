---
name: Bug report
about: Report a bug or an issue you've found with Trino Python client
title: ''
labels: bug
assignees: ''

---
---
name: Feature request
about: Suggest an idea for Trino Python client
title: ''
labels: enhancement
assignees: ''
body:
- type: textarea
  attributes:
  label: Expected behavior
  description: Describe what happened.
  placeholder: >
  A clear and concise description of what you expected to happen.
  validations:
  required: true
- type: textarea
  attributes:
  label: Actual behavior
  description: What do you think went wrong?
  placeholder: >
  A clear and concise description of any alternative solutions or features you've considered.
- type: textarea
  attributes:
  label: Steps To Reproduce
  description: What do you think went wrong?
  placeholder: >
  In as much detail as possible, please provide steps to reproduce the issue. 
  Sample code that triggers the issue, relevant server settings, etc is all very helpful here.
- type: textarea
  attributes:
  label: Screenshots and log output
  description: What do you think went wrong?
  placeholder: >
  If applicable, add screenshots or log output to help explain your problem.
- type: checkboxes
  attributes:
  label: Are you willing to submit PR?
  description: >
  This is absolutely not required, but we are happy to guide you in the contribution process
  especially if you already have a good understanding of how to implement the fix.
  options:
    - label: Yes I am willing to submit a PR!
- type: input
  attributes:
  label: Operating System
  description: What Operating System are you using?
  placeholder: "You can get it via `cat /etc/os-release` for example"
  validations:
  required: true
- type: input
  attributes:
  label: Trino Python client version
  description: What Operating System are you using?
  placeholder: "You can get it via executing `import trino; print(trino.__version__)` in your Python environment"
  validations:
  required: true
- type: input
  attributes:
  label: Trino Server version
  description: What Operating System are you using?
  placeholder: "You can get it via executing `SELECT VERSION();` on your Trino server"
  validations:
  required: true
- type: input
  attributes:
  label: Python version
  description: What Operating System are you using?
  placeholder: "You can get it via executing `python --version`"
  validations:
  required: true
- type: markdown
  attributes:
