# purrcafe.

backend for purrshare

## usage

> [!IMPORTANT]
> all instructions here are for *unix platforms

### installation

1. get yourself python 3.12
2. clone this repo and `cd` into it
3. make a venv with `python3.12 -m venv venv` and activate it with `source venv/bin/activate`
4. then install requirements with `pip install -r requirements.txt`
5. deactivate venv with `deactivate`

### launching

1. activate venv (`source venv/bin/activate`)
2. launch with `python -m purrcafe` (or `env <ENVVARS> python -m purrcafe` if you want to override config)
3. to close press `CTRL + C`
4. deactivate venv (`deactivate`)

## configuration

### env vars

- `PURRCAFE_LISTEN` - run on `0.0.0.0` if set to `1` else `127.0.0.1` (ie localhost)
- `PURRCAFE_PORT` - what port to listen on (default is `8080`)
- `PURRCAFE_LOGLEVEL` - log level of backend [default INFO]
- `PURRCAFE_UVICORN_LOGLEVEL` - log level of underlying backend framework [default ERROR]
- `PURRCAFE_EXPIRED_CHECK_DELAY` - how often to check for expired files (in hours) [default 1]
- `PURRCAFE_FUCK_OFF_CORS` - "1" to disable CORS (allow everything), else restrict to PURRCAFE_ORIGIN and http://localhost:5173 [default <not 1>]
- `PURRCAFE_ORIGIN` - what else to allow with CORS [default https://purrshare.net]
- `PURRCAFE_ADMIN_PASSWORD` - password for logging in to admin acc (do not set to disable admin acc) [default <nothing>]
- `PURRCAFE_LIFETIME_GUEST` - max lifetime of files uploaded by guest in seconds [default 604800 (1 week)]
- `PURRCAFE_LIFETIME` - max lifetime of files uploaded by registered users in seconds [default 2419200 (4 weeks)]
- `PURRCAFE_MAXSIZE_GUEST` - max filesize of the files uploaded by guest in bytes [default 31457280 (30 MiB)]
- `PURRCAFE_MAXSIZE` - max filesize of the files uploaded by registered users in bytes [default 73400320 (70 MiB)]