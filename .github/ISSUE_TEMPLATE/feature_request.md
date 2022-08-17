---
name: Feature request
about: Suggest an idea for Trino Python client
title: ''
labels: enhancement
assignees: ''
body:
- type: textarea
  attributes:
  label: Describe the feature
  description: Describe what happened.
  placeholder: >
  A clear and concise description of what you want to happen
  and what problem it would solve.
  Who will benefit from this feature?
  Please be specific and provide examples.
  validations:
  required: true
- type: textarea
  attributes:
  label: Describe alternatives you've considered
  description: What do you think went wrong?
  placeholder: >
  A clear and concise description of any alternative solutions or features you've considered.
- type: checkboxes
  attributes:
  label: Are you willing to submit PR?
  description: >
  This is absolutely not required, but we are happy to guide you in the contribution process
  especially if you already have a good understanding of how to implement the feature.
  options:
  - label: Yes I am willing to submit a PR!
- type: markdown
  attributes:
  value: "Thanks for completing our form!"
