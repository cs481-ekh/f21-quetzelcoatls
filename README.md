# capstone-template
![example workflow](https://github.com/cs481-ekh/f21-quetzelcoatls/actions/workflows/python-app.yml/badge.svg)


### Testing

Two testing-related caveats:

1. We are not using `build.sh` and `test.sh`; rather, everything is handled in the GitHub Actions workflow (for the pretty checkmarks, mostly).
2. We don't currently have a Hello World application to test against, since we'll need to determine what GUI library we're using first (a Spring 1 task). For now, there's a placeholder testing class & target, which confirms addition works as expected.