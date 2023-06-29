# VillaFleurie rental site

[![Netlify Status](https://api.netlify.com/api/v1/badges/aa5c29ee-eced-46dd-ad53-1e0822001364/deploy-status)](https://app.netlify.com/sites/villafleurie-site/deploys)

## How to use

You can build the site using the built-in static site generator included.
The entry point is located in the [main file](./lib/main.py). It should not be modified.

### Add a page

To add a page, create a `HTML` file in the `pages` directory.

Optionally, you can inject data in the template. To do so you should create a `TOML` file with the same name as the
template.

Any fields will become available in the template.
For instance the  `index.toml` for `index.html` could contain the following fields:

```toml
name = "index"
template = "index.html"
```

### Layouts

You can use template inheritance. The layouts must be in the `pages/layouts` subdirectory.

### Configuration

The configuration file ([config.toml](./config.toml)) is mandatory and should resemble:

```toml
name = "VillaFleurie"
```

## Build site

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

## Deployment

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
- [x] Optimize images
- [x] Automate the file search
- [x] Extract data out of the template
- [ ] Create a 'all' key for data available in all templates
- [ ] Create a template for the rooms
- [ ] Build script before commit
- [ ] Lit parapluie, barbecue et machine à laver

## Excluded

* The language switcher

## Built with

- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - fast, expressive, extensible templating
  engine
- [Netlify](https://www.netlify.com/) - Develop and deploy websites and apps in record time