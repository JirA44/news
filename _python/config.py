name: "fundamental_issue"
on:
  push:
    branches:
      - master
jobs:
  fundamental_issue:
    runs-on: ubuntu-latest
    steps:
      - name: "Run code"
        script: python3.10 solution.py