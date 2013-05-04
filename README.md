# Pouët API

Awesome ! Welcome dude !

For now, the API lives at http://pouet-api.herokuapp.com/

## Use this stuff

### Get some demo info

`GET /prod/:id`

Returns:

```json
{
    "name": "Awesome Stuff",
    "download": "http://www.scene.org/this/is/leet.zip"
}
```

Example: http://pouet-api.herokuapp.com/prod/1221

## Contribute to this shit

Yes, help me !

### Setup a working env

```bash
git clone git@github.com:lra/pouet-api.git
git remote add heroku git@heroku.com:pouet-api.git
brew install heroku-toolbelt
brew install python
pip install -r pouet-api/requirements.txt
```

### Push the source code

```bash
git push
```

### Deploy a new version

```bash
git push heroku master
```

Obviously you can't do it without being allowed to
