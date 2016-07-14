# multi-project docs
Documentation for NSLS-II DAQ and Analysis

## Developer Documentation

This repo and others build the sphinx on Travis-CI and force-push the build
products to the repo NSLS-II/NSLS-II.github.io.

To set this up:

```
ssh-keygen -t rsa -C "bluesky-docs-deploy"
travis encrypt-file bluesky-docs-deploy --repo NSLS-II/bluesky
git add bluesky-docs-deploy.enc
```

Copy the `openssl ...` line output from the `travis...` command above and use
it in the `.travis.yml`.

Add the public key, bluesky-docs-deploy.pub, as a "Deploy Key" in the
settings of the NSLS-II.github.io repository.

