# PID Scrapper

## Installation

This project requires certain Python packages to function properly. To install them, run:

```console
$ pip install requests bs4 python-telegram-bot python-dotenv
```

## Running

To start the app, run the following command from project root directory:

```console
[user@device zapocet]$ python src/index.py
```

After that the bot will run in terminal until termination.

## Environment

This app uses `python-dotenv` package to store environment variables. It is necessary that file `.env` is created in the project root directory and these variables are declared:

```javascript
TELEGRAM_TOKEN=...
```

## File structure

The file structure is as follows:

```console
.
├── README.md
└── src
    ├── class_connection_detail.py
    ├── class_connections_list.py
    ├── class_day_time.py
    ├── class_route.py
    ├── class_search_query.py
    ├── class_time_location.py
    ├── cmd_help.py
    ├── cmd_inline.py
    ├── cmd_next.py
    ├── cmd_routes.py
    ├── cmd_search_params.py
    ├── cmd_search.py
    ├── cmd_start.py
    ├── index.py
    ├── module_request_builder.py
    ├── module_routes_manager.py
    ├── module_state.py
    ├── module_stops_manager.py
    └── data
        ├── points.json
        ├── routes.json
        ├── _sources.json
        └── stops.json
```

All python files are located in `/src` directory. `index.py` is the core file. All other `.py` files belong to one of three categories:

- **Class** (`class_<class_name>.py`) - Class definition.
- **Module** (`module_<module_name>.py`) - Module. Module is an object of some class. There can only be on instance of this class per app and therefore it is created in the file itself and then can be imported and used in other files.
- **Command** (`cmd_<command_name>.py`) - Command definition. Command is a function with two parameters: `update` and `context` (see `python-telegram-bot` docs).

Data about public transport the app uses is stored in `src/data`. There are three core JSON files:

- **Routes** (`routes.json`) - Data about public transport routes (eg. Tram 1: Sídliště Petřiny - Spojovací)

- **Stops** (`stops.json`) - Data about stops. The app only uses the names to check them against user input

- **Points** (`points.json`) - Data about location of stops. Not really used in app, but it is present just in case.

These JSON files are fetched from `https://pid.cz/<endpoint>.json`, as can be seen in meta file `_source.json`

## User interface

User interface of the app is provided by Telegram App. This bot only receives commands (user messages) and responds to them accordingly.

Although it is possible to implement more advanced ways to interact with the app, this app only implements commands in the form of `/<command>`. The commands it implements are:

- **`/start`** - Starts the communication with the bot
- **`/help`** - Display list of commands
- **`/routes`** - Display list of routes
- **`/search`** - Start a connection search dialog

### Routes

Furthermore command **`/routes`** only displays a list of more specific commands that users can use to display routes of particular mean of transport:

- **`/routes_tram`** for tram routes,
- **`/routes_bus`** for bus routes,
- **`/routes_metro`** for metro routes,
- **`/routes_train`** for train routes.

Since there are many routes, pagination is implemented to ensure that the list of routes is not too long. The limit of the number of routes has been set to 10. Optional parameter page can be specified when calling command: **`/routes_<mean> <page>`**. For example, command **`/routes_bus 8`** will display routes 71-80 from a list of bus routes ordered by their numbers (IDs). The default value of `<page>` parameter is 1 (first page).

### Search

Command **`/search`** is used to initiate search dialog. After that, the user will be asked to input the departure stop. User input will lead to one of two outcomes:

1. Either the stop exists and the dialog continues

or

2. The stop does not exist and user is asked to provide the departure stop again

After providing a correct (existing) departure stop, the user is asked to provide the arrival stop. The same error handling is implemented here, as is in the departure stop input.

When both departure and arrival stops are specified by the user, first connection is displayed (or message informing the user that no connections were found). After that, the user can use command **`/next`** to display the next connection. After viewing all connections, the user is informed that the bot is able to provide only so many connections.

## Fetching and storing connections

After the bot receives the **`/search`** command, a new `SearchQuery` instance is created for the effective user. This instance is stored in the `state` module using a dictionary where user ID is the key and instance of `SearchQuery` is the value.

The `SearchQuery` instance stores search parameters (from and to), list of `ConnectionDetail` instances (which is empty before calling `fetchConnections()`), cursor which indicates which `ConnectionDetail` instance is next; and message which should be displayed to the user. This message is generated inside the `next_connection()` method and then just fed to the user.

When both departure and arrival stops are specified, a new `ConnectionsList` instance is created, connections are fetched using `request_builder` module and then parsed using regex. `ConnectionsList` finds connections and creates a new `ConnectionDetail` instance for each. A new instance of `ConnectionDetail` contains a link to a page with more details. These details can be fetched and parsed using the `fetch()` method of `ConnectionDetail`. Once again `request_builder` module is used here to fetch raw HTML which is parsed using regex.
