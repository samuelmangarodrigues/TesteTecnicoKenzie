# TesteTecnicoKenzie
Teste técnico Kenzie Academy Brazil.
Essa aplicação permite criar tarefas, completar tarefas, editar e excluir.

## EndPoints

## Todo

## Post | Todo

`https://test-kenzie.herokuapp.com/api/todo/`

O usuário deve passar a descrição da tarefa e receberá um status 201 CREATED

`Requisição `

```json
{
  "description": "Tomar água",
}
```

`Resposta | 201 CREATED`


```json
{
	"id": 3,
	"description": "tomar água",
	"completed": false
}

```

## Get | Todo

`https://test-kenzie.herokuapp.com/api/todo/`

Requisição para listar as tarefas.

`Requisição `

> Não tem corpo na requisição.

`Resposta | status 200 OK`

Retorna uma lista com todas as tasks criadas, status 200 OK.

```json
[
	{
		"id": 3,
		"description": "tomar água",
		"completed": false
	},
	{
		"id": 4,
		"description": "comprar cerveja",
		"completed": false
	},
	{
		"id": 5,
		"description": "beber remédio",
		"completed": false
	}
]
```
## Get | Todo

`https://test-kenzie.herokuapp.com/api/todo/3`

O usuário deve passar o id para listar a tarefa específica.

`Requisição `

> Não tem corpo na requisição.

`Resposta | status 200 OK`

Retorna a tarefa específica de acordo com o Id da task, status 200 OK.

```json
{
	"id": 3,
	"description": "tomar água",
	"completed": false
}
```

## Put | Todo

`https://test-kenzie.herokuapp.com/api/todo/3/`

O usuário deve passar o id da task para completa-lá, status 200 OK.

`Requisição `

> Sem corpo na requisição

`Resposta | 200 OK`

Atualiza a chave completed, colocando-a como true.

```json
{
	"id": 3,
	"description": "tomar água",
	"completed": true
}

```


## Patch | Todo

`https://test-kenzie.herokuapp.com/api/todo/3/`

O usuário deve passar o id da task e a nova descrição da tarefa, status 200 OK.

`Requisição `

```json
{
	"description":"tomar café"
}
```

`Resposta | 200 OK`

```json
{
	"id": 3,
	"description": "tomar café",
	"completed": true
}

```

## Delete | Todo

`https://test-kenzie.herokuapp.com/api/todo/3/`

O usuário deve passar o id da task para deleta-lá, status 200 OK.

`Requisição `

> Sem corpo na requisição

`Resposta | 200 OK`

```json
{
	"message":"deleted"
}

```
