# VillaFleurie rental site

[![Netlify Status](https://api.netlify.com/api/v1/badges/aa5c29ee-eced-46dd-ad53-1e0822001364/deploy-status)](https://app.netlify.com/sites/villafleurie-site/deploys)

## Static Site Generator

The entry point is located in the [main file](./lib/main.py). It should not be modified.

The templates files must be located in the [templates](./templates) directory.
You can use template inheritance but not yet data injection.
### Configuration

The configuration file ([config.json](./config.json)) is mandatory and should resemble:

```json
{
  "name": "VillaFleurie",
  "templates": [
    "index.html",
    "t2-corail.html",
    "t3-azur.html",
    "contact.html",
    "reservation.html"
  ],
  "outDir": "dist"
}
```

### Site Generation

You can generate the site by running:

```shell
python -m lib.main
```

### How to run the website

It will generate the final files in the [dist](./dist) folder.
You can run the output files using a simple python server:

```shell
cd dist && python -m http.server
```

### Deployment

You can then deploy the site on any platform supporting static sites (Netlify,…) or your own VPS.

## TODO

- [X] Create a base template for the header and footer
- [X] Build index page
- [X] Build room pages
    - [x] T2
    - [x] T3
- [X] Build contact pages
- [X] Use netlify form for the contact form
- [x] Deploy to VillaFleurie's domain
- [ ] Find attractions for landing page
- [x] Pick real reviews from AirBnB and Booking
- [ ] Optimize images
- [ ] Automate the file search
- [ ] Extract data out of the template
- [ ] Create a 'all' key for data available in all templates
- [ ] Create a template for the rooms
- [ ] Build script before commit
- [ ] Lit parapluie, barbecue et machine à laver

## Excluded

* The article page
* The language switcher

## Built with

- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - fast, expressive, extensible templating
  engine
- [Netlify](https://www.netlify.com/) - Develop and deploy websites and apps in record time