# WB_Blog_API

## An API for simple blog built with Django, Django Rest Framework with Postgres database.

## Clone project

```sh
$ git clone git@github.com:daelynum/WB_DRF_Blog.git
```

***Install all dependencies with `pip3 install -r requirements.txt`***

## API routes

Functionality

- [Registration](#registration)<br>
- [Auth](#auth)<br>
- [Show users](#all-users)<br>
- [Adding post](#post-add)<br>
- [View all posts](#list-posts)<br>
- [Subscriptions ](#subscription)<br>
- [Read post ](#read-post)<br>
- [Posts from favorite users ](#fav-users-posts)<br>
- [Readed posts ](#readed-posts)<br>

Routes

> `/api/v1/auth/user/` [<span style=color:#2EFF00>POST</span>]<br>
> `/api/v1/auth/user/login/` [<span style=color:#2EFF00>POST</span>]<br>
> `/api/v1/auth/users/` [<span style=color:#00D4FF>GET</span>] <br>
> `/api/v1/auth/users/?count_of_posts` [<span style=color:#00D4FF>GET</span>] <br>
> `/api/v1/posts/add/` [<span style=color:#2EFF00>POST</span>]<br>
> `/api/v1/posts/all/` [<span style=color:#00D4FF>GET</span>]<br>
> `/api/v1/auth/users/favorite_user/` [<span style=color:#2EFF00>POST</span>]<br>
> `/api/v1/auth/users/favorite_user/update/` [<span style=color:#00D4FF>PATCH</span>]<br>
> `/api/v1/posts/flag_post_as_readed/` [<span style=color:#2EFF00>POST</span>]<br>
> `/api/v1/posts/posts_from_fav_users/` [<span style=color:#00D4FF>GET</span>]<br>
> `/api/v1/posts/readed_posts/?read_posts` [<span style=color:#00D4FF>GET</span>]<br>
> `/api/v1/posts/readed_posts/` [<span style=color:#00D4FF>GET</span>]<br>

## Registration/Auth

<a id="registration" name="registration">#</a> **Registration** [<span style=color:#2EFF00>POST</span>]

### Route: `/api/v1/auth/user/`<br><br>

request:<br>

```json
{
  "user": {
    "username": "user",
    "email": "user@user.user",
    "password": "qweasdzxc"
  }
}
```

response:<br>

```json
{
  'email': 'user@user.user',
  'username': 'user'
}
```

<a id="auth" name="auth">#</a> **Login** [<span style=color:#2EFF00>POST</span>]<br>

### Route: `/api/v1/auth/user/login/`<br><br>

request:<br>

```json
{
  "user": {
    "email": "user4@user.user",
    "password": "qweasdzxc"
  }
}
```

response:<br>

```json
{
  'user': {
    'email': 'user@user.user',
    'username': 'user',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUwNjMzMTc2fQ.7pRLozXUJk6FdgIeCKrxprnurcosfaqRoU1bRkkWkak'
  }
}
```

<a id="all-users" name="all-users">#</a> **Show users** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/v1/auth/users/`<br><br>

You can configure the filter of users with count of posts by setting the `count_of_posts` parameter in the URL<br>
*Example: `/api/v1/auth/users/?count_of_posts`*

response:<br>

```json
{
  'count': 11,
  'next': None,
  'previous': None,
  'results': [
    {
      'username': 'vladimir',
      'email': 'vladimir@mail.ru',
      'count_of_posts': 8
    },
    {
      'username': 'v',
      'email': 'v@mail.ru',
      'count_of_posts': 1
    }
  ]
}
```

## Posts

<a id="post-add" name="post-add">#</a> **Add post** [<span style=color:#2EFF00>POST</span>]<br>

### Route: `/api/v1/posts/add/`<br><br>

request:<br>

```json
{
  "title": "7 post",
  "text": "7 text"
}
```

Also you should add token to your headers<br>

```json
{
  'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUxMjIxMzAzfQ.IMpoJYXv8iYdM9kWma8a_cdgOWB7VIIxiaSv0FcmYf4'
}
```

response:<br>

```json
{
  'success': "Post {'post': {'title': 'second post', 'text': 'second text'}, 'user': 1} created successfully"
}
```

<a id="list-posts" name="list-posts">#</a> **View all posts** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/v1/posts/all/`<br><br>

response:<br>

```json
{
  'posts': [
    {
      'id': 8,
      'created': '2022-04-22T10:45:22.824821Z',
      'title': 'third post',
      'text': 'third text',
      'user': 1
    }
  ]
}
```

<a id="subscriptions" name="subscriptions">#</a> **
Subscriptions** [<span style=color:#2EFF00>POST</span>] [<span style=color:#00D4FF>PATCH</span>]<br>

### Route: `/api/v1/auth/users/favorite_user/`[<span style=color:#2EFF00>POST</span>]<br><br>

### Route: `/api/v1/auth/users/favorite_user/update/`[<span style=color:#00D4FF>PATCH</span>]<br><br>

request:<br>

```json
{
  "secondary_user": 2,
  "favorite_user": True
}
```

Also you should add token to your headers<br>

```json
{
  'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUxMjIxMzAzfQ.IMpoJYXv8iYdM9kWma8a_cdgOWB7VIIxiaSv0FcmYf4'
}
```

response:<br>

```json
{
  'id': 12,
  'favorite_user': True,
  'secondary_user': 2
}
```

<a id="read-post" name="read-post">#</a> **Read post** [<span style=color:#2EFF00>POST</span>] <br>

### Route: `/api/v1/posts/flag_post_as_readed/`<br><br>

request:<br>

```json
{
  "post": 1,
  "flagged_post": True
}
```

Also you should add token to your headers<br>

```json
{
  'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUxMjIxMzAzfQ.IMpoJYXv8iYdM9kWma8a_cdgOWB7VIIxiaSv0FcmYf4'
}
```

response:<br>

```json
{
  'id': 1,
  'flagged_post': True,
  'post': 1
}
```

<a id="fav-users-posts" name="fav-users-posts">#</a> **Posts from favorite users (10 posts per
page)** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/v1/posts/posts_from_fav_users/`<br><br>

You should add token to your headers<br>

```json
{
  'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUxMjIxMzAzfQ.IMpoJYXv8iYdM9kWma8a_cdgOWB7VIIxiaSv0FcmYf4'
}
```

response:<br>

```json
{
  'count': 35,
  'next': 'http://127.0.0.1:8000/api/v1/posts/posts_from_fav_users/?limit=10&offset=10',
  'previous': None,
  'results': [
    {
      'created': '2022-04-28T08:56:15.182829Z',
      'title': '123',
      'text': '123',
      'user_id': 3
    },
    {
      'created': '2022-04-28T08:26:43.850968Z',
      'title': '',
      'text': '',
      'user_id': 1
    },
    {
      'created': '2022-04-28T08:26:43.841572Z',
      'title': '',
      'text': '',
      'user_id': 1
    },
    {
      'created': '2022-04-28T08:26:15.340785Z',
      'title': '',
      'text': '',
      'user_id': 1
    },
    {
      'created': '2022-04-28T08:26:02.030470Z',
      'title': '',
      'text': '',
      'user_id': 1
    },
    {
      'created': '2022-04-27T15:17:25.103001Z',
      'title': '7 post',
      'text': '7 text',
      'user_id': 1
    },
    {
      'created': '2022-04-22T13:02:55.903508Z',
      'title': '7 post',
      'text': '7 text',
      'user_id': 1
    },
    {
      'created': '2022-04-22T12:48:07.304581Z',
      'title': '7 post',
      'text': '7 text',
      'user_id': 1
    },
    {
      'created': '2022-04-22T11:33:38.857745Z',
      'title': '7 post',
      'text': '7 text',
      'user_id': 1
    },
    {
      'created': '2022-04-22T11:25:23.414689Z',
      'title': '7 post',
      'text': '7 text',
      'user_id': 1
    }
  ]
}
```

<a id="readed-posts" name="readed-posts">#</a> **Readed posts** [<span style=color:#00D4FF>GET</span>]<br>

### Route: `/api/v1/posts/readed_posts/?read_posts`<br><br>

You should add token to your headers<br>

```json
{
  'Authorization': 'token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUxMjIxMzAzfQ.IMpoJYXv8iYdM9kWma8a_cdgOWB7VIIxiaSv0FcmYf4'
}
```

response:<br>

```json
{
  'count': 2,
  'next': None,
  'previous': None,
  'results': [
    {
      'created': '2022-04-22T11:10:12.454027Z',
      'title': '7 post',
      'text': '7 text'
    },
    {
      'created': '2022-04-22T11:12:00.894412Z',
      'title': '7 post',
      'text': '7 text'
    }
  ]
}
```