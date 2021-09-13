# Search Recipes

Api that register a chef and a recipe that consults the recipes created.

## System Requirements

- Python 3.8+

## Dependencies

```http
See requirements.txt
```
## Installation

First clone the project:

```http
git clone https://github.com/lucasluk3/search-recipes.git
```

Create a virtualenv:

```http
(Windows)
 python3 -m venv env

(Linux)
$ virtualenv env
```

Install the dependencies:

```http
pip install -r requirements.txt
```

Run the project:

```http
python manage.py runserver
```

### The database is already fulfilled

## API Reference

#### Create chef

```http
  POST /recipes/chef
```
| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name for the creation of chef |

#### Create Recipes

```http
  POST /recipes/chef/recipe
```
| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of the recipe. |
| `short_description`|`string`|**Required**. Short description of the recipe. |
| `method`|`text`|**Required**. Method for the realization of the recipe. | 
| `ingredients`|`text`|**Required**. Ingredients of the recipe. |
| `difficulty`|`choices`|**Required**. Difficulty demarked as 1 to 3. |
| `chef`|`foreign_key`|**Required**. Chef who created the recipe.| 
| `time`|`integer`|**Required**. Time until the dish is ready.| 

#### List recipes

```http
  GET /recipes?name=&difficulty=&chef=
```

| Query Params | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Search by name. |
| `difficulty`| `string` | **Required**. Search by difficulty. |
| `chef`      | `string` | **Required**. Search by chef name. |

#### Get recipe

```http
  GET /recipes/chef/recipe/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |

#### Update recipe

```http
  PUT /recipes/chef/recipe/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of the recipe. |
| `short_description`|`string`|**Required**. Short description of the recipe. |
| `method`|`text`|**Required**. Method for the realization of the recipe. | 
| `ingredients`|`text`|**Required**. Ingredients of the recipe. |
| `difficulty`|`choices`|**Required**. Difficulty demarked as 1 to 3. |
| `chef`|`foreign_key`|**Required**. Chef who created the recipe.| 
| `time`|`integer`|**Required**. Time until the dish is ready.| 

#### Delete recipe

```http
  DELETE /recipes/chef/recipe/{id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |




  