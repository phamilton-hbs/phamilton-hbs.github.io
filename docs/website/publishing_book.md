# Publishing Book Content

After making changes to the book locally, the final step is to push your local build of the book to the dsm.business site.

---

Once you are finished making changes, make sure you build the book in its entirety using the following command:

```
jupyter-book build --all dsm_website
```

Be sure to include `--all` so that all recent changes you made are captured in the build. Once you have done this, the compiled version of the book will be saved in your local `dsm_website\_build` directory.

## Transfer Files

Using an FTP client, connect to the server with the following credentials:

+ **Host:** ftp.dsm.business
+ **Username:** admin@dsm.business
+ **Password:** hF8D9^Vs7!kMs
+ **Port:** 21

To push the updated version of the book to the server, copy the entire contents of your local `dsm_website\_build\html` directory to the remote site. 

**Note:** There have been issues connecting to the server with `FileZilla`, so it is recommended you use `Core FTP LE` to connect.