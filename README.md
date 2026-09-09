Betta fish blog on GitHub Pages.

## Setup

```bash
npm install
(cd docs && bundle install)
./setup.sh
```

## Development

```bash
cd docs && bundle exec jekyll serve --livereload
```

## Quality checks

```bash
npm run lint
npm run format
npm test
```

## Notes

- Source files live in `docs/`.
- `setup.sh` installs dependencies and optional pre-commit hooks.
- GitHub Actions builds the site and runs the HTML test.

## License

See [LICENSE.txt](LICENSE.txt)
